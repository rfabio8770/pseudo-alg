# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudocodigoParser import PseudocodigoParser
else:
    from PseudocodigoParser import PseudocodigoParser

# This class defines a complete listener for a parse tree produced by PseudocodigoParser.
class PseudocodigoListener(ParseTreeListener):

    # Enter a parse tree produced by PseudocodigoParser#programa.
    def enterPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#programa.
    def exitPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sec_decl.
    def enterSec_decl(self, ctx:PseudocodigoParser.Sec_declContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sec_decl.
    def exitSec_decl(self, ctx:PseudocodigoParser.Sec_declContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#dec_variables.
    def enterDec_variables(self, ctx:PseudocodigoParser.Dec_variablesContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#dec_variables.
    def exitDec_variables(self, ctx:PseudocodigoParser.Dec_variablesContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#declaraciones.
    def enterDeclaraciones(self, ctx:PseudocodigoParser.DeclaracionesContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#declaraciones.
    def exitDeclaraciones(self, ctx:PseudocodigoParser.DeclaracionesContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#declaracion.
    def enterDeclaracion(self, ctx:PseudocodigoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#declaracion.
    def exitDeclaracion(self, ctx:PseudocodigoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#tipo.
    def enterTipo(self, ctx:PseudocodigoParser.TipoContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#tipo.
    def exitTipo(self, ctx:PseudocodigoParser.TipoContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#listadec_id.
    def enterListadec_id(self, ctx:PseudocodigoParser.Listadec_idContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#listadec_id.
    def exitListadec_id(self, ctx:PseudocodigoParser.Listadec_idContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#es_arreglo.
    def enterEs_arreglo(self, ctx:PseudocodigoParser.Es_arregloContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#es_arreglo.
    def exitEs_arreglo(self, ctx:PseudocodigoParser.Es_arregloContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_indices.
    def enterLista_indices(self, ctx:PseudocodigoParser.Lista_indicesContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_indices.
    def exitLista_indices(self, ctx:PseudocodigoParser.Lista_indicesContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#cuerpo.
    def enterCuerpo(self, ctx:PseudocodigoParser.CuerpoContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#cuerpo.
    def exitCuerpo(self, ctx:PseudocodigoParser.CuerpoContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_sentencias.
    def enterLista_sentencias(self, ctx:PseudocodigoParser.Lista_sentenciasContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_sentencias.
    def exitLista_sentencias(self, ctx:PseudocodigoParser.Lista_sentenciasContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sentencia.
    def enterSentencia(self, ctx:PseudocodigoParser.SentenciaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sentencia.
    def exitSentencia(self, ctx:PseudocodigoParser.SentenciaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_asig.
    def enterSent_asig(self, ctx:PseudocodigoParser.Sent_asigContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_asig.
    def exitSent_asig(self, ctx:PseudocodigoParser.Sent_asigContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_lectura.
    def enterSent_lectura(self, ctx:PseudocodigoParser.Sent_lecturaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_lectura.
    def exitSent_lectura(self, ctx:PseudocodigoParser.Sent_lecturaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_impresion.
    def enterSent_impresion(self, ctx:PseudocodigoParser.Sent_impresionContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_impresion.
    def exitSent_impresion(self, ctx:PseudocodigoParser.Sent_impresionContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_id.
    def enterLista_id(self, ctx:PseudocodigoParser.Lista_idContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_id.
    def exitLista_id(self, ctx:PseudocodigoParser.Lista_idContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_condicional.
    def enterSent_condicional(self, ctx:PseudocodigoParser.Sent_condicionalContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_condicional.
    def exitSent_condicional(self, ctx:PseudocodigoParser.Sent_condicionalContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_mientras.
    def enterSent_mientras(self, ctx:PseudocodigoParser.Sent_mientrasContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_mientras.
    def exitSent_mientras(self, ctx:PseudocodigoParser.Sent_mientrasContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_desde.
    def enterSent_desde(self, ctx:PseudocodigoParser.Sent_desdeContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_desde.
    def exitSent_desde(self, ctx:PseudocodigoParser.Sent_desdeContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#paso.
    def enterPaso(self, ctx:PseudocodigoParser.PasoContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#paso.
    def exitPaso(self, ctx:PseudocodigoParser.PasoContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_repetir.
    def enterSent_repetir(self, ctx:PseudocodigoParser.Sent_repetirContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_repetir.
    def exitSent_repetir(self, ctx:PseudocodigoParser.Sent_repetirContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_caso.
    def enterSent_caso(self, ctx:PseudocodigoParser.Sent_casoContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_caso.
    def exitSent_caso(self, ctx:PseudocodigoParser.Sent_casoContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_casos.
    def enterLista_casos(self, ctx:PseudocodigoParser.Lista_casosContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_casos.
    def exitLista_casos(self, ctx:PseudocodigoParser.Lista_casosContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#uncaso.
    def enterUncaso(self, ctx:PseudocodigoParser.UncasoContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#uncaso.
    def exitUncaso(self, ctx:PseudocodigoParser.UncasoContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_iterar.
    def enterSent_iterar(self, ctx:PseudocodigoParser.Sent_iterarContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_iterar.
    def exitSent_iterar(self, ctx:PseudocodigoParser.Sent_iterarContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#sent_salir_si.
    def enterSent_salir_si(self, ctx:PseudocodigoParser.Sent_salir_siContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#sent_salir_si.
    def exitSent_salir_si(self, ctx:PseudocodigoParser.Sent_salir_siContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#const_num.
    def enterConst_num(self, ctx:PseudocodigoParser.Const_numContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#const_num.
    def exitConst_num(self, ctx:PseudocodigoParser.Const_numContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#expresion.
    def enterExpresion(self, ctx:PseudocodigoParser.ExpresionContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#expresion.
    def exitExpresion(self, ctx:PseudocodigoParser.ExpresionContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#factor.
    def enterFactor(self, ctx:PseudocodigoParser.FactorContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#factor.
    def exitFactor(self, ctx:PseudocodigoParser.FactorContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#primario.
    def enterPrimario(self, ctx:PseudocodigoParser.PrimarioContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#primario.
    def exitPrimario(self, ctx:PseudocodigoParser.PrimarioContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#arreglo.
    def enterArreglo(self, ctx:PseudocodigoParser.ArregloContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#arreglo.
    def exitArreglo(self, ctx:PseudocodigoParser.ArregloContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_ind.
    def enterLista_ind(self, ctx:PseudocodigoParser.Lista_indContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_ind.
    def exitLista_ind(self, ctx:PseudocodigoParser.Lista_indContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#lista_expr.
    def enterLista_expr(self, ctx:PseudocodigoParser.Lista_exprContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#lista_expr.
    def exitLista_expr(self, ctx:PseudocodigoParser.Lista_exprContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#constante.
    def enterConstante(self, ctx:PseudocodigoParser.ConstanteContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#constante.
    def exitConstante(self, ctx:PseudocodigoParser.ConstanteContext):
        pass



del PseudocodigoParser