import sys
from PseudocodigoVisitor import PseudocodigoVisitor
from PseudocodigoParser import PseudocodigoParser

class BreakException(Exception):
    """Excepción para manejar la instrucción SALIR_SI o romper bucles."""
    pass

class InterpreterVisitor(PseudocodigoVisitor):
    def __init__(self):
        # Memoria o tabla de símbolos para almacenar variables y sus valores
        self.memory = {}
        # Pila para manejar ámbitos o contextos si fuera necesario (aquí usamos uno global plano)

    # programa: ALGORITMO ID sec_decl cuerpo PUNTO ;
    def visitPrograma(self, ctx: PseudocodigoParser.ProgramaContext):
        print(f"--- Ejecutando algoritmo: {ctx.ID().getText()} ---")
        return self.visit(ctx.cuerpo())

    # cuerpo: INICIO lista_sentencias FIN ;
    def visitCuerpo(self, ctx: PseudocodigoParser.CuerpoContext):
        return self.visit(ctx.lista_sentencias())

    # lista_sentencias: lista_sentencias sentencia | sentencia ;
    def visitLista_sentencias(self, ctx: PseudocodigoParser.Lista_sentenciasContext):
        if ctx.getChildCount() == 2:
            self.visit(ctx.lista_sentencias())
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.sentencia())

    # sent_asig: ID arreglo ASIG expresion ;
    def visitSent_asig(self, ctx: PseudocodigoParser.Sent_asigContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        
        # Manejo simple (si tiene arreglo, se podria extender el índice)
        if ctx.arreglo().getText() != "":
            indices = self.visit(ctx.arreglo())
            if var_name not in self.memory or not isinstance(self.memory[var_name], list):
                self.memory[var_name] = {} # o estructura para arreglos multidimensionales
            # Simplificación para una dimensión
            self.memory[var_name][tuple(indices)] = value
        else:
            self.memory[var_name] = value
        return value

    # sent_impresion: IMPRIMIR PAR_AB lista_expr PAR_CE ;
    def visitSent_impresion(self, ctx: PseudocodigoParser.Sent_impresionContext):
        # Como lista_expr puede ser múltiple, evaluamos y mostramos
        val = self.visit(ctx.lista_expr())
        print(val)
        return val

    # sent_lectura: LEER PAR_AB lista_id PAR_CE ;
    def visitSent_lectura(self, ctx: PseudocodigoParser.Sent_lecturaContext):
        # Aquí recorremos o evaluamos la lista de IDs para capturar input del usuario
        # Por simplicidad, implementamos la captura por consola para el primer ID o lista
        ids = self.obtener_nombres_ids(ctx.lista_id())
        for var_name in ids:
            val_str = input(f"Ingrese valor para {var_name}: ")
            # Intentamos convertir automáticamente a número o dejar como texto
            try:
                if '.' in val_str:
                    val = float(val_str)
                else:
                    val = int(val_str)
            except ValueError:
                val = val_str
            self.memory[var_name] = val

    def obtener_nombres_ids(self, ctx):
        # Extrae los nombres de variables de la regla lista_id recursivamente
        if ctx.getChildCount() == 4: # lista_id COMA ID arreglo
            return self.obtener_nombres_ids(ctx.lista_id()) + [ctx.ID().getText()]
        else: # ID arreglo
            return [ctx.ID().getText()]

    # sent_condicional: SI expresion ENTONCES lista_sentencias FINSI 
    #                 | SI expresion ENTONCES lista_sentencias SINO lista_sentencias FINSI ;
    def visitSent_condicional(self, ctx: PseudocodigoParser.Sent_condicionalContext):
        condicion = self.visit(ctx.expresion())
        if condicion:
            return self.visit(ctx.lista_sentencias(0))
        elif ctx.SINO():
            return self.visit(ctx.lista_sentencias(1))

    # sent_mientras: MIENTRAS expresion lista_sentencias FINMIENTRAS ;
    def visitSent_mientras(self, ctx: PseudocodigoParser.Sent_mientrasContext):
        while self.visit(ctx.expresion()):
            self.visit(ctx.lista_sentencias())

    # Expresiones aritméticas y lógicas
    def visitExpresion(self, ctx: PseudocodigoParser.ExpresionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        
        left = self.visit(ctx.expresion())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.factor())

        return self.calcular_operacion(left, op, right)

    def visitFactor(self, ctx: PseudocodigoParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primario())
        
        left = self.visit(ctx.factor())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.primario())

        return self.calcular_operacion(left, op, right)

    def visitPrimario(self, ctx: PseudocodigoParser.PrimarioContext):
        if ctx.PAR_AB():
            return self.visit(ctx.expresion())
        elif ctx.constante():
            return self.visit(ctx.constante())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise Exception(f"Error semántico: Variable '{var_name}' no declarada o sin inicializar.")
        elif ctx.NO() or ctx.OPSR():
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.primario())
            if op == '-':
                return -val
            elif op.lower() in ['no', 'not']:
                return not val
        return None

    def visitConstante(self, ctx: PseudocodigoParser.ConstanteContext):
        texto = ctx.getText()
        if ctx.NUMERO_ENTERO():
            return int(texto)
        elif ctx.NUMERO_REAL():
            return float(texto)
        elif ctx.CONSTANTE_BOOLEANA():
            return True if texto.lower() in ['verdadero', 'true'] else False
        elif ctx.CONSTANTE_STRING():
            return texto[1:-1] # Remover comillas
        elif ctx.CONSTANTE_CARACTER():
            return texto[1]
        return texto

    def calcular_operacion(self, left, op, right):
        op = op.lower()
        # Aritméticos
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right if right != 0 else ZeroDivisionError("División por cero")
        elif op in ['mod']: return left % right
        
        # Relacionales
        elif op == '==': return left == right
        elif op == '<>': return left != right
        elif op == '<': return left < right
        elif op == '<=': return left <= right
        elif op == '>': return left > right
        elif op == '>=': return left >= right
        
        # Lógicos
        elif op in ['y', 'and']: return left and right
        elif op in ['o', 'or']: return left or right
        
        return None
    # 1. Bucle DESDE (equivalente a un FOR)
    # sent_desde: DESDE sent_asig HASTA primario paso lista_sentencias FINDESDE ;
    # paso: PASO NUMERO_ENTERO | /* epsilon */ ;
    def visitSent_desde(self, ctx: PseudocodigoParser.Sent_desdeContext):
        # Ejecutamos la asignación inicial (ej: i <- 1)
        self.visit(ctx.sent_asig())
        
        # Extraemos la variable de control de la asignación inicial para evaluarla
        var_name = ctx.sent_asig().ID().getText()
        
        # Evaluamos el límite superior (hasta dónde debe llegar)
        limite = self.visit(ctx.primario())
        
        # Evaluamos el paso (por defecto es 1 si no está especificado)
        paso_val = 1
        if ctx.paso() and ctx.paso().NUMERO_ENTERO():
            paso_val = int(ctx.paso().NUMERO_ENTERO().getText())

        while True:
            valor_actual = self.memory[var_name]
            
            # Verificamos la condición del bucle (asumiendo incremento positivo)
            if valor_actual > limite:
                break
                
            try:
                # Ejecutamos las sentencias internas del desde
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
                
            # Incrementamos la variable según el paso
            self.memory[var_name] = self.memory[var_name] + paso_val
        
        return None

    # 2. Bucle REPETIR...HASTA_QUE (equivalente a REPEAT...UNTIL)
    # sent_repetir: REPETIR lista_sentencias HASTA_QUE expresion ;
    def visitSent_repetir(self, ctx: PseudocodigoParser.Sent_repetirContext):
        while True:
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
                
            # En repetir...hasta_que, el bloque se ejecuta al menos una vez 
            # y se repite MIENTRAS la condición sea FALSA (termina cuando es True)
            condicion = self.visit(ctx.expresion())
            #print(f"[DEBUG] Valor de c / Condición hasta_que: {condicion}") # <-- Añade esto para ver qué evalúa
            if condicion:
                break
                
        return None

    # 3. Estructura de Selección Múltiple CASO (SEGUN / EN_CASO)
    # sent_caso: EN_CASO expresion SEA lista_casos FINCASO ;
    # lista_casos: lista_casos uncaso | uncaso ;
    # uncaso: const_num DP lista_sentencias | OTRO DP lista_sentencias ;
    def visitSent_caso(self, ctx: PseudocodigoParser.Sent_casoContext):
        valor_selector = self.visit(ctx.expresion())
        lista_casos_ctx = ctx.lista_casos()
        
        # Aplanamos o recorremos los casos para evaluarlos
        casos = self._obtener_lista_casos(lista_casos_ctx)
        
        ejecutado = False
        caso_otro = None

        for const_val, sentencias_ctx, es_otro in casos:
            if es_otro:
                caso_otro = sentencias_ctx
            elif valor_selector == const_val:
                self.visit(sentencias_ctx)
                ejecutado = True
                break
        
        # Si no coincidió con ninguno y hay un "otro", lo ejecutamos
        if not ejecutado and caso_otro:
            self.visit(caso_otro)
            
        return None

    def _obtener_lista_casos(self, ctx):
        """Método auxiliar para recorrer recursivamente la regla lista_casos"""
        if ctx.getChildCount() == 2:
            # lista_casos uncaso
            anteriores = self._obtener_lista_casos(ctx.lista_casos())
            actual = self._procesar_uncaso(ctx.uncaso())
            return anteriores + [actual]
        else:
            # uncaso
            return [self._procesar_uncaso(ctx.uncaso())]

    def _procesar_uncaso(self, ctx):
        if ctx.OTRO():
            return (None, ctx.lista_sentencias(), True)
        else:
            const_val = self.visit(ctx.const_num())
            return (const_val, ctx.lista_sentencias(), False)

    # 4. Bucle ITERAR (Bucle infinito controlado internamente por SALIR_SI)
    # sent_iterar: ITERAR lista_sentencias FINITERAR ;
    def visitSent_iterar(self, ctx: PseudocodigoParser.Sent_iterarContext):
        while True:
            try:
                self.visit(ctx.lista_sentencias())
            except BreakException:
                break
        return None

    # 5. Instrucción SALIR_SI (Rompe el bucle actual si la condición es verdadera)
    # sent_salir_si: SALIR_SI expresion ;
    def visitSent_salir_si(self, ctx: PseudocodigoParser.Sent_salir_siContext):
        condicion = self.visit(ctx.expresion())
        if condicion:
            raise BreakException()
        return None

    