import sys
from PseudocodigoVisitor import PseudocodigoVisitor
from PseudocodigoParser import PseudocodigoParser

class BreakException(Exception):
    """Excepción para manejar la instrucción SALIR_SI o ruptura de bucles."""
    pass

class ReturnException(Exception):
    """Excepción para manejar el retorno de valores en funciones."""
    def __init__(self, value):
        self.value = value

class InterpreterVisitor(PseudocodigoVisitor):
    def __init__(self):
        # Memoria principal plana (diccionario único)
        self.memory = {}
    
    def visitCuerpo(self, ctx: PseudocodigoParser.CuerpoContext):
        return self.visit(ctx.lista_sentencias())

    def visitLista_sentencias(self, ctx: PseudocodigoParser.Lista_sentenciasContext):
        if ctx.getChildCount() == 2:
            self.visit(ctx.lista_sentencias())
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.sentencia())

    # --- DECLARACIÓN DE VARIABLES (Escalares simples) ---
    def visitListadec_id(self, ctx: PseudocodigoParser.Listadec_idContext):
        var_name = ctx.ID().getText()
        # Se inicializan todas en 0 por defecto
        self.memory[var_name] = 0
        return None

    # --- ASIGNACIÓN SIMPLE ---
    def visitSent_asig(self, ctx: PseudocodigoParser.Sent_asigContext):
        var_name = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memory[var_name] = valor
        return valor

    # --- ENTRADA Y SALIDA ---
    def visitSent_impresion(self, ctx: PseudocodigoParser.Sent_impresionContext):
        val = self.visit(ctx.lista_expr())
        print(val)
        return val

    def visitSent_lectura(self, ctx: PseudocodigoParser.Sent_lecturaContext):
        ids = self.obtener_nombres_ids(ctx.lista_id())
        for var_name in ids:
            val_str = input(f"Ingrese valor para {var_name}: ")
            try:
                if '.' in val_str:
                    val = float(val_str)
                else:
                    val = int(val_str)
            except ValueError:
                val = val_str
            self.memory[var_name] = val

    def obtener_nombres_ids(self, ctx):
        if ctx.getChildCount() == 4:
            return self.obtener_nombres_ids(ctx.lista_id()) + [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()]

    # --- ESTRUCTURAS DE CONTROL ---
    def visitSent_condicional(self, ctx: PseudocodigoParser.Sent_condicionalContext):
        condicion = self.visit(ctx.expresion())
        if condicion:
            return self.visit(ctx.lista_sentencias(0))
        elif ctx.SINO():
            return self.visit(ctx.lista_sentencias(1))

    def visitSent_mientras(self, ctx: PseudocodigoParser.Sent_mientrasContext):
        while self.visit(ctx.expresion()):
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
        return None

    def visitSent_desde(self, ctx: PseudocodigoParser.Sent_desdeContext):
        self.visit(ctx.sent_asig())
        var_name = ctx.sent_asig().ID().getText()
        limite = self.visit(ctx.expresion())
        
        paso_val = 1
        if ctx.paso() and ctx.paso().NUMERO_ENTERO():
            paso_val = int(ctx.paso().NUMERO_ENTERO().getText())

        while True:
            valor_actual = self.memory[var_name]
            if valor_actual > limite:
                break
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
            self.memory[var_name] = self.memory[var_name] + paso_val
        return None

    def visitSent_repetir(self, ctx: PseudocodigoParser.Sent_repetirContext):
        while True:
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
            
            condicion = self.visit(ctx.expresion())
            if condicion:
                break
        return None

    def visitSent_iterar(self, ctx: PseudocodigoParser.Sent_iterarContext):
        while True:
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
        return None

    def visitSent_salir_si(self, ctx: PseudocodigoParser.Sent_salir_siContext):
        condicion = self.visit(ctx.expresion())
        if condicion:
            raise BreakException()
        return None

    def visitSent_caso(self, ctx: PseudocodigoParser.Sent_casoContext):
        valor_selector = self.visit(ctx.expresion())
        casos = self._obtener_lista_casos(ctx.lista_casos())
        
        ejecutado = False
        caso_otro = None

        for const_val, sentencias_ctx, es_otro in casos:
            if es_otro:
                caso_otro = sentencias_ctx
            elif valor_selector == const_val:
                self.visit(sentencias_ctx)
                ejecutado = True
                break
        
        if not ejecutado and caso_otro:
            self.visit(caso_otro)
        return None

    def _obtener_lista_casos(self, ctx):
        if ctx.getChildCount() == 2:
            anteriores = self._obtener_lista_casos(ctx.lista_casos())
            actual = self._procesar_uncaso(ctx.uncaso())
            return anteriores + [actual]
        else:
            return [self._procesar_uncaso(ctx.uncaso())]

    def _procesar_uncaso(self, ctx):
        if ctx.OTRO():
            return (None, ctx.lista_sentencias(), True)
        else:
            const_val = self.visit(ctx.const_num())
            return (const_val, ctx.lista_sentencias(), False)

    # --- EVALUACIÓN DE EXPRESIONES ---
    def visitExpresion(self, ctx: PseudocodigoParser.ExpresionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expresion_logica())
        
        left = self.visit(ctx.expresion())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.expresion_logica())
        return self.calcular_operacion(left, op, right)

    def visitExpresion_logica(self, ctx: PseudocodigoParser.Expresion_logicaContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relacion())
        
        left = self.visit(ctx.expresion_logica())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.relacion())
        return self.calcular_operacion(left, op, right)

    def visitRelacion(self, ctx: PseudocodigoParser.RelacionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.simple_expr())
        
        left = self.visit(ctx.relacion())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.simple_expr())
        return self.calcular_operacion(left, op, right)

    def visitSimple_expr(self, ctx: PseudocodigoParser.Simple_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termino())
        
        left = self.visit(ctx.simple_expr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.termino())
        return self.calcular_operacion(left, op, right)

    def visitTermino(self, ctx: PseudocodigoParser.TerminoContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        
        left = self.visit(ctx.termino())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.factor())
        return self.calcular_operacion(left, op, right)

    def visitFactor(self, ctx: PseudocodigoParser.FactorContext):
        if ctx.PAR_AB():
            return self.visit(ctx.expresion())
        elif ctx.constante():
            return self.visit(ctx.constante())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.memory:
                raise Exception(f"Variable '{var_name}' no declarada.")
            return self.memory[var_name]
        elif ctx.NO() or ctx.OPSR():
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.factor())
            if op == '-':
                return -val
            elif op.lower() in ['no', 'not']:
                return not bool(val)
        return None

    def visitConst_num(self, ctx: PseudocodigoParser.Const_numContext):
        return float(ctx.getText()) if '.' in ctx.getText() else int(ctx.getText())

    def visitConstante(self, ctx: PseudocodigoParser.ConstanteContext):
        texto = ctx.getText()
        if ctx.NUMERO_ENTERO():
            return int(texto)
        elif ctx.NUMERO_REAL():
            return float(texto)
        elif ctx.CONSTANTE_BOOLEANA():
            return True if texto.lower() in ['verdadero', 'true'] else False
        elif ctx.CONSTANTE_STRING():
            return texto[1:-1]
        elif ctx.CONSTANTE_CARACTER():
            return texto[1]
        return texto

    def visitLista_expr(self, ctx: PseudocodigoParser.Lista_exprContext):
        if ctx.getChildCount() == 3:
            self.visit(ctx.lista_expr())
            return self.visit(ctx.expresion())
        else:
            return self.visit(ctx.expresion())

    # --- UNIFICADOR DE OPERACIONES ---
    def calcular_operacion(self, left, op, right):
        if op is None:
            return None
        op = str(op).lower()
        
        # Aritméticos
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right if right != 0 else ZeroDivisionError("División por cero")
        elif op == 'mod': return left % right
        
        # Relacionales
        elif op == '=': return left == right
        elif op == '<>': return left != right
        elif op == '<': return left < right
        elif op == '<=': return left <= right
        elif op == '>': return left > right
        elif op == '>=': return left >= right
        
        # Lógicos
        elif op in ['y', 'and']: return bool(left) and bool(right)
        elif op in ['o', 'or']: return bool(left) or bool(right)
        
        return None