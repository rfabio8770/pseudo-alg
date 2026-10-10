# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudocodigoParser import PseudocodigoParser
else:
    from PseudocodigoParser import PseudocodigoParser

# This class defines a complete generic visitor for a parse tree produced by PseudocodigoParser.

class PseudocodigoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PseudocodigoParser#programa.
    def visitPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sec_decl.
    def visitSec_decl(self, ctx:PseudocodigoParser.Sec_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#dec_variables.
    def visitDec_variables(self, ctx:PseudocodigoParser.Dec_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#declaraciones.
    def visitDeclaraciones(self, ctx:PseudocodigoParser.DeclaracionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#declaracion.
    def visitDeclaracion(self, ctx:PseudocodigoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#tipo.
    def visitTipo(self, ctx:PseudocodigoParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#listadec_id.
    def visitListadec_id(self, ctx:PseudocodigoParser.Listadec_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#es_arreglo.
    def visitEs_arreglo(self, ctx:PseudocodigoParser.Es_arregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_indices.
    def visitLista_indices(self, ctx:PseudocodigoParser.Lista_indicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#cuerpo.
    def visitCuerpo(self, ctx:PseudocodigoParser.CuerpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_sentencias.
    def visitLista_sentencias(self, ctx:PseudocodigoParser.Lista_sentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sentencia.
    def visitSentencia(self, ctx:PseudocodigoParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_asig.
    def visitSent_asig(self, ctx:PseudocodigoParser.Sent_asigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_lectura.
    def visitSent_lectura(self, ctx:PseudocodigoParser.Sent_lecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_impresion.
    def visitSent_impresion(self, ctx:PseudocodigoParser.Sent_impresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_id.
    def visitLista_id(self, ctx:PseudocodigoParser.Lista_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_condicional.
    def visitSent_condicional(self, ctx:PseudocodigoParser.Sent_condicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_mientras.
    def visitSent_mientras(self, ctx:PseudocodigoParser.Sent_mientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_desde.
    def visitSent_desde(self, ctx:PseudocodigoParser.Sent_desdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#paso.
    def visitPaso(self, ctx:PseudocodigoParser.PasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_repetir.
    def visitSent_repetir(self, ctx:PseudocodigoParser.Sent_repetirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_caso.
    def visitSent_caso(self, ctx:PseudocodigoParser.Sent_casoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_casos.
    def visitLista_casos(self, ctx:PseudocodigoParser.Lista_casosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#uncaso.
    def visitUncaso(self, ctx:PseudocodigoParser.UncasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_iterar.
    def visitSent_iterar(self, ctx:PseudocodigoParser.Sent_iterarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#sent_salir_si.
    def visitSent_salir_si(self, ctx:PseudocodigoParser.Sent_salir_siContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#const_num.
    def visitConst_num(self, ctx:PseudocodigoParser.Const_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#expresion.
    def visitExpresion(self, ctx:PseudocodigoParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#expresion_logica.
    def visitExpresion_logica(self, ctx:PseudocodigoParser.Expresion_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#relacion.
    def visitRelacion(self, ctx:PseudocodigoParser.RelacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#simple_expr.
    def visitSimple_expr(self, ctx:PseudocodigoParser.Simple_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#termino.
    def visitTermino(self, ctx:PseudocodigoParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#factor.
    def visitFactor(self, ctx:PseudocodigoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#arreglo.
    def visitArreglo(self, ctx:PseudocodigoParser.ArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_ind.
    def visitLista_ind(self, ctx:PseudocodigoParser.Lista_indContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#lista_expr.
    def visitLista_expr(self, ctx:PseudocodigoParser.Lista_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#constante.
    def visitConstante(self, ctx:PseudocodigoParser.ConstanteContext):
        return self.visitChildren(ctx)



del PseudocodigoParser