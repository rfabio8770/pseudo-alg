# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,331,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,5,3,85,8,3,10,3,12,3,88,9,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,7,1,7,1,7,1,
        7,1,7,3,7,113,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,121,8,8,10,8,12,8,
        124,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,135,8,10,10,
        10,12,10,138,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,150,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,5,15,175,8,15,10,15,12,15,178,9,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,194,8,16,1,17,1,
        17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,
        19,1,19,3,19,212,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,5,22,230,8,22,10,22,12,22,
        233,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,242,8,23,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,5,27,268,8,27,10,
        27,12,27,271,9,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,
        28,282,8,28,10,28,12,28,285,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,3,29,298,8,29,1,30,1,30,1,30,1,30,1,30,3,
        30,305,8,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,313,8,31,10,31,12,
        31,316,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,324,8,32,10,32,12,
        32,327,9,32,1,33,1,33,1,33,0,10,6,12,16,20,30,44,54,56,62,64,34,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,0,3,1,0,2,6,1,0,40,41,1,0,39,43,
        328,0,68,1,0,0,0,2,74,1,0,0,0,4,76,1,0,0,0,6,79,1,0,0,0,8,89,1,0,
        0,0,10,92,1,0,0,0,12,94,1,0,0,0,14,112,1,0,0,0,16,114,1,0,0,0,18,
        125,1,0,0,0,20,129,1,0,0,0,22,149,1,0,0,0,24,151,1,0,0,0,26,156,
        1,0,0,0,28,161,1,0,0,0,30,166,1,0,0,0,32,193,1,0,0,0,34,195,1,0,
        0,0,36,200,1,0,0,0,38,211,1,0,0,0,40,213,1,0,0,0,42,218,1,0,0,0,
        44,224,1,0,0,0,46,241,1,0,0,0,48,243,1,0,0,0,50,247,1,0,0,0,52,250,
        1,0,0,0,54,252,1,0,0,0,56,272,1,0,0,0,58,297,1,0,0,0,60,304,1,0,
        0,0,62,306,1,0,0,0,64,317,1,0,0,0,66,328,1,0,0,0,68,69,5,1,0,0,69,
        70,5,51,0,0,70,71,3,2,1,0,71,72,3,18,9,0,72,73,5,38,0,0,73,1,1,0,
        0,0,74,75,3,4,2,0,75,3,1,0,0,0,76,77,5,31,0,0,77,78,3,6,3,0,78,5,
        1,0,0,0,79,80,6,3,-1,0,80,81,3,8,4,0,81,86,1,0,0,0,82,83,10,2,0,
        0,83,85,3,8,4,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,
        1,0,0,0,87,7,1,0,0,0,88,86,1,0,0,0,89,90,3,10,5,0,90,91,3,12,6,0,
        91,9,1,0,0,0,92,93,7,0,0,0,93,11,1,0,0,0,94,95,6,6,-1,0,95,96,5,
        51,0,0,96,97,3,14,7,0,97,104,1,0,0,0,98,99,10,2,0,0,99,100,5,33,
        0,0,100,101,5,51,0,0,101,103,3,14,7,0,102,98,1,0,0,0,103,106,1,0,
        0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,13,1,0,0,0,106,104,1,0,0,
        0,107,108,5,36,0,0,108,109,3,16,8,0,109,110,5,37,0,0,110,113,1,0,
        0,0,111,113,1,0,0,0,112,107,1,0,0,0,112,111,1,0,0,0,113,15,1,0,0,
        0,114,115,6,8,-1,0,115,116,5,40,0,0,116,122,1,0,0,0,117,118,10,2,
        0,0,118,119,5,33,0,0,119,121,5,40,0,0,120,117,1,0,0,0,121,124,1,
        0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,17,1,0,0,0,124,122,1,0,
        0,0,125,126,5,7,0,0,126,127,3,20,10,0,127,128,5,8,0,0,128,19,1,0,
        0,0,129,130,6,10,-1,0,130,131,3,22,11,0,131,136,1,0,0,0,132,133,
        10,2,0,0,133,135,3,22,11,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,21,1,0,0,0,138,136,1,0,0,0,139,150,3,
        24,12,0,140,150,3,26,13,0,141,150,3,28,14,0,142,150,3,32,16,0,143,
        150,3,34,17,0,144,150,3,36,18,0,145,150,3,40,20,0,146,150,3,42,21,
        0,147,150,3,48,24,0,148,150,3,50,25,0,149,139,1,0,0,0,149,140,1,
        0,0,0,149,141,1,0,0,0,149,142,1,0,0,0,149,143,1,0,0,0,149,144,1,
        0,0,0,149,145,1,0,0,0,149,146,1,0,0,0,149,147,1,0,0,0,149,148,1,
        0,0,0,150,23,1,0,0,0,151,152,5,51,0,0,152,153,3,60,30,0,153,154,
        5,32,0,0,154,155,3,54,27,0,155,25,1,0,0,0,156,157,5,16,0,0,157,158,
        5,34,0,0,158,159,3,30,15,0,159,160,5,35,0,0,160,27,1,0,0,0,161,162,
        5,17,0,0,162,163,5,34,0,0,163,164,3,64,32,0,164,165,5,35,0,0,165,
        29,1,0,0,0,166,167,6,15,-1,0,167,168,5,51,0,0,168,169,3,60,30,0,
        169,176,1,0,0,0,170,171,10,2,0,0,171,172,5,33,0,0,172,173,5,51,0,
        0,173,175,3,60,30,0,174,170,1,0,0,0,175,178,1,0,0,0,176,174,1,0,
        0,0,176,177,1,0,0,0,177,31,1,0,0,0,178,176,1,0,0,0,179,180,5,9,0,
        0,180,181,3,54,27,0,181,182,5,10,0,0,182,183,3,20,10,0,183,184,5,
        12,0,0,184,194,1,0,0,0,185,186,5,9,0,0,186,187,3,54,27,0,187,188,
        5,10,0,0,188,189,3,20,10,0,189,190,5,11,0,0,190,191,3,20,10,0,191,
        192,5,12,0,0,192,194,1,0,0,0,193,179,1,0,0,0,193,185,1,0,0,0,194,
        33,1,0,0,0,195,196,5,14,0,0,196,197,3,54,27,0,197,198,3,20,10,0,
        198,199,5,15,0,0,199,35,1,0,0,0,200,201,5,18,0,0,201,202,3,24,12,
        0,202,203,5,20,0,0,203,204,3,58,29,0,204,205,3,38,19,0,205,206,3,
        20,10,0,206,207,5,19,0,0,207,37,1,0,0,0,208,209,5,13,0,0,209,212,
        5,40,0,0,210,212,1,0,0,0,211,208,1,0,0,0,211,210,1,0,0,0,212,39,
        1,0,0,0,213,214,5,21,0,0,214,215,3,20,10,0,215,216,5,22,0,0,216,
        217,3,54,27,0,217,41,1,0,0,0,218,219,5,26,0,0,219,220,3,54,27,0,
        220,221,5,30,0,0,221,222,3,44,22,0,222,223,5,28,0,0,223,43,1,0,0,
        0,224,225,6,22,-1,0,225,226,3,46,23,0,226,231,1,0,0,0,227,228,10,
        2,0,0,228,230,3,46,23,0,229,227,1,0,0,0,230,233,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,45,1,0,0,0,233,231,1,0,0,0,234,235,3,
        52,26,0,235,236,5,27,0,0,236,237,3,20,10,0,237,242,1,0,0,0,238,239,
        5,29,0,0,239,240,5,27,0,0,240,242,3,20,10,0,241,234,1,0,0,0,241,
        238,1,0,0,0,242,47,1,0,0,0,243,244,5,23,0,0,244,245,3,20,10,0,245,
        246,5,25,0,0,246,49,1,0,0,0,247,248,5,24,0,0,248,249,3,54,27,0,249,
        51,1,0,0,0,250,251,7,1,0,0,251,53,1,0,0,0,252,253,6,27,-1,0,253,
        254,3,56,28,0,254,269,1,0,0,0,255,256,10,5,0,0,256,257,5,44,0,0,
        257,268,3,56,28,0,258,259,10,4,0,0,259,260,5,45,0,0,260,268,3,56,
        28,0,261,262,10,3,0,0,262,263,5,46,0,0,263,268,3,56,28,0,264,265,
        10,2,0,0,265,266,5,47,0,0,266,268,3,56,28,0,267,255,1,0,0,0,267,
        258,1,0,0,0,267,261,1,0,0,0,267,264,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,55,1,0,0,0,271,269,1,0,0,0,272,273,
        6,28,-1,0,273,274,3,58,29,0,274,283,1,0,0,0,275,276,10,3,0,0,276,
        277,5,49,0,0,277,282,3,58,29,0,278,279,10,2,0,0,279,280,5,48,0,0,
        280,282,3,58,29,0,281,275,1,0,0,0,281,278,1,0,0,0,282,285,1,0,0,
        0,283,281,1,0,0,0,283,284,1,0,0,0,284,57,1,0,0,0,285,283,1,0,0,0,
        286,287,5,34,0,0,287,288,3,54,27,0,288,289,5,35,0,0,289,298,1,0,
        0,0,290,291,5,44,0,0,291,298,3,58,29,0,292,293,5,50,0,0,293,298,
        3,58,29,0,294,298,3,66,33,0,295,296,5,51,0,0,296,298,3,60,30,0,297,
        286,1,0,0,0,297,290,1,0,0,0,297,292,1,0,0,0,297,294,1,0,0,0,297,
        295,1,0,0,0,298,59,1,0,0,0,299,300,5,36,0,0,300,301,3,62,31,0,301,
        302,5,37,0,0,302,305,1,0,0,0,303,305,1,0,0,0,304,299,1,0,0,0,304,
        303,1,0,0,0,305,61,1,0,0,0,306,307,6,31,-1,0,307,308,3,54,27,0,308,
        314,1,0,0,0,309,310,10,2,0,0,310,311,5,33,0,0,311,313,3,54,27,0,
        312,309,1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,
        315,63,1,0,0,0,316,314,1,0,0,0,317,318,6,32,-1,0,318,319,3,54,27,
        0,319,325,1,0,0,0,320,321,10,2,0,0,321,322,5,33,0,0,322,324,3,54,
        27,0,323,320,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,0,325,326,1,0,
        0,0,326,65,1,0,0,0,327,325,1,0,0,0,328,329,7,2,0,0,329,67,1,0,0,
        0,19,86,104,112,122,136,149,176,193,211,231,241,267,269,281,283,
        297,304,314,325
    ]

class PseudocodigoParser ( Parser ):

    grammarFileName = "Pseudocodigo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "','", "'('", "')'", "'['", "']'", "'.'" ]

    symbolicNames = [ "<INVALID>", "ALGORITMO", "ENTERO", "CARACTER", "REAL", 
                      "BOOLEANO", "STRING", "INICIO", "FIN", "SI", "ENTONCES", 
                      "SINO", "FINSI", "PASO", "MIENTRAS", "FINMIENTRAS", 
                      "LEER", "IMPRIMIR", "DESDE", "FINDESDE", "HASTA", 
                      "REPETIR", "HASTA_QUE", "ITERAR", "SALIR_SI", "FINITERAR", 
                      "EN_CASO", "DP", "FINCASO", "OTRO", "SEA", "VAR", 
                      "ASIG", "COMA", "PAR_AB", "PAR_CE", "COR_AB", "COR_CE", 
                      "PUNTO", "CONSTANTE_BOOLEANA", "NUMERO_ENTERO", "NUMERO_REAL", 
                      "CONSTANTE_CARACTER", "CONSTANTE_STRING", "OPSR", 
                      "OP_MOD", "OPREL", "OPO", "OPY", "OPMD", "NO", "ID", 
                      "WS" ]

    RULE_programa = 0
    RULE_sec_decl = 1
    RULE_dec_variables = 2
    RULE_declaraciones = 3
    RULE_declaracion = 4
    RULE_tipo = 5
    RULE_listadec_id = 6
    RULE_es_arreglo = 7
    RULE_lista_indices = 8
    RULE_cuerpo = 9
    RULE_lista_sentencias = 10
    RULE_sentencia = 11
    RULE_sent_asig = 12
    RULE_sent_lectura = 13
    RULE_sent_impresion = 14
    RULE_lista_id = 15
    RULE_sent_condicional = 16
    RULE_sent_mientras = 17
    RULE_sent_desde = 18
    RULE_paso = 19
    RULE_sent_repetir = 20
    RULE_sent_caso = 21
    RULE_lista_casos = 22
    RULE_uncaso = 23
    RULE_sent_iterar = 24
    RULE_sent_salir_si = 25
    RULE_const_num = 26
    RULE_expresion = 27
    RULE_factor = 28
    RULE_primario = 29
    RULE_arreglo = 30
    RULE_lista_ind = 31
    RULE_lista_expr = 32
    RULE_constante = 33

    ruleNames =  [ "programa", "sec_decl", "dec_variables", "declaraciones", 
                   "declaracion", "tipo", "listadec_id", "es_arreglo", "lista_indices", 
                   "cuerpo", "lista_sentencias", "sentencia", "sent_asig", 
                   "sent_lectura", "sent_impresion", "lista_id", "sent_condicional", 
                   "sent_mientras", "sent_desde", "paso", "sent_repetir", 
                   "sent_caso", "lista_casos", "uncaso", "sent_iterar", 
                   "sent_salir_si", "const_num", "expresion", "factor", 
                   "primario", "arreglo", "lista_ind", "lista_expr", "constante" ]

    EOF = Token.EOF
    ALGORITMO=1
    ENTERO=2
    CARACTER=3
    REAL=4
    BOOLEANO=5
    STRING=6
    INICIO=7
    FIN=8
    SI=9
    ENTONCES=10
    SINO=11
    FINSI=12
    PASO=13
    MIENTRAS=14
    FINMIENTRAS=15
    LEER=16
    IMPRIMIR=17
    DESDE=18
    FINDESDE=19
    HASTA=20
    REPETIR=21
    HASTA_QUE=22
    ITERAR=23
    SALIR_SI=24
    FINITERAR=25
    EN_CASO=26
    DP=27
    FINCASO=28
    OTRO=29
    SEA=30
    VAR=31
    ASIG=32
    COMA=33
    PAR_AB=34
    PAR_CE=35
    COR_AB=36
    COR_CE=37
    PUNTO=38
    CONSTANTE_BOOLEANA=39
    NUMERO_ENTERO=40
    NUMERO_REAL=41
    CONSTANTE_CARACTER=42
    CONSTANTE_STRING=43
    OPSR=44
    OP_MOD=45
    OPREL=46
    OPO=47
    OPY=48
    OPMD=49
    NO=50
    ID=51
    WS=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALGORITMO(self):
            return self.getToken(PseudocodigoParser.ALGORITMO, 0)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def sec_decl(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sec_declContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(PseudocodigoParser.CuerpoContext,0)


        def PUNTO(self):
            return self.getToken(PseudocodigoParser.PUNTO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PseudocodigoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PseudocodigoParser.ALGORITMO)
            self.state = 69
            self.match(PseudocodigoParser.ID)
            self.state = 70
            self.sec_decl()
            self.state = 71
            self.cuerpo()
            self.state = 72
            self.match(PseudocodigoParser.PUNTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sec_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_variables(self):
            return self.getTypedRuleContext(PseudocodigoParser.Dec_variablesContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sec_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSec_decl" ):
                listener.enterSec_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSec_decl" ):
                listener.exitSec_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSec_decl" ):
                return visitor.visitSec_decl(self)
            else:
                return visitor.visitChildren(self)




    def sec_decl(self):

        localctx = PseudocodigoParser.Sec_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sec_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.dec_variables()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_variablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PseudocodigoParser.VAR, 0)

        def declaraciones(self):
            return self.getTypedRuleContext(PseudocodigoParser.DeclaracionesContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_dec_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_variables" ):
                listener.enterDec_variables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_variables" ):
                listener.exitDec_variables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_variables" ):
                return visitor.visitDec_variables(self)
            else:
                return visitor.visitChildren(self)




    def dec_variables(self):

        localctx = PseudocodigoParser.Dec_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dec_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(PseudocodigoParser.VAR)
            self.state = 77
            self.declaraciones(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(PseudocodigoParser.DeclaracionContext,0)


        def declaraciones(self):
            return self.getTypedRuleContext(PseudocodigoParser.DeclaracionesContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_declaraciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraciones" ):
                listener.enterDeclaraciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraciones" ):
                listener.exitDeclaraciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraciones" ):
                return visitor.visitDeclaraciones(self)
            else:
                return visitor.visitChildren(self)



    def declaraciones(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.DeclaracionesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_declaraciones, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.declaracion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.DeclaracionesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declaraciones)
                    self.state = 82
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 83
                    self.declaracion() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(PseudocodigoParser.TipoContext,0)


        def listadec_id(self):
            return self.getTypedRuleContext(PseudocodigoParser.Listadec_idContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = PseudocodigoParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.tipo()
            self.state = 90
            self.listadec_id(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(PseudocodigoParser.ENTERO, 0)

        def CARACTER(self):
            return self.getToken(PseudocodigoParser.CARACTER, 0)

        def BOOLEANO(self):
            return self.getToken(PseudocodigoParser.BOOLEANO, 0)

        def REAL(self):
            return self.getToken(PseudocodigoParser.REAL, 0)

        def STRING(self):
            return self.getToken(PseudocodigoParser.STRING, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = PseudocodigoParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Listadec_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def es_arreglo(self):
            return self.getTypedRuleContext(PseudocodigoParser.Es_arregloContext,0)


        def listadec_id(self):
            return self.getTypedRuleContext(PseudocodigoParser.Listadec_idContext,0)


        def COMA(self):
            return self.getToken(PseudocodigoParser.COMA, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_listadec_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListadec_id" ):
                listener.enterListadec_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListadec_id" ):
                listener.exitListadec_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListadec_id" ):
                return visitor.visitListadec_id(self)
            else:
                return visitor.visitChildren(self)



    def listadec_id(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Listadec_idContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_listadec_id, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PseudocodigoParser.ID)
            self.state = 96
            self.es_arreglo()
            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Listadec_idContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listadec_id)
                    self.state = 98
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 99
                    self.match(PseudocodigoParser.COMA)
                    self.state = 100
                    self.match(PseudocodigoParser.ID)
                    self.state = 101
                    self.es_arreglo() 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Es_arregloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COR_AB(self):
            return self.getToken(PseudocodigoParser.COR_AB, 0)

        def lista_indices(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_indicesContext,0)


        def COR_CE(self):
            return self.getToken(PseudocodigoParser.COR_CE, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_es_arreglo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEs_arreglo" ):
                listener.enterEs_arreglo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEs_arreglo" ):
                listener.exitEs_arreglo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEs_arreglo" ):
                return visitor.visitEs_arreglo(self)
            else:
                return visitor.visitChildren(self)




    def es_arreglo(self):

        localctx = PseudocodigoParser.Es_arregloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_es_arreglo)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(PseudocodigoParser.COR_AB)
                self.state = 108
                self.lista_indices(0)
                self.state = 109
                self.match(PseudocodigoParser.COR_CE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_indicesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO_ENTERO(self):
            return self.getToken(PseudocodigoParser.NUMERO_ENTERO, 0)

        def lista_indices(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_indicesContext,0)


        def COMA(self):
            return self.getToken(PseudocodigoParser.COMA, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_indices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_indices" ):
                listener.enterLista_indices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_indices" ):
                listener.exitLista_indices(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_indices" ):
                return visitor.visitLista_indices(self)
            else:
                return visitor.visitChildren(self)



    def lista_indices(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_indicesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_lista_indices, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(PseudocodigoParser.NUMERO_ENTERO)
            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_indicesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_indices)
                    self.state = 117
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 118
                    self.match(PseudocodigoParser.COMA)
                    self.state = 119
                    self.match(PseudocodigoParser.NUMERO_ENTERO) 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(PseudocodigoParser.INICIO, 0)

        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def FIN(self):
            return self.getToken(PseudocodigoParser.FIN, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCuerpo" ):
                return visitor.visitCuerpo(self)
            else:
                return visitor.visitChildren(self)




    def cuerpo(self):

        localctx = PseudocodigoParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(PseudocodigoParser.INICIO)
            self.state = 126
            self.lista_sentencias(0)
            self.state = 127
            self.match(PseudocodigoParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_sentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self):
            return self.getTypedRuleContext(PseudocodigoParser.SentenciaContext,0)


        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_sentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_sentencias" ):
                listener.enterLista_sentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_sentencias" ):
                listener.exitLista_sentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_sentencias" ):
                return visitor.visitLista_sentencias(self)
            else:
                return visitor.visitChildren(self)



    def lista_sentencias(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_sentenciasContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_lista_sentencias, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.sentencia()
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_sentenciasContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_sentencias)
                    self.state = 132
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 133
                    self.sentencia() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sent_asig(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_asigContext,0)


        def sent_lectura(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_lecturaContext,0)


        def sent_impresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_impresionContext,0)


        def sent_condicional(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_condicionalContext,0)


        def sent_mientras(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_mientrasContext,0)


        def sent_desde(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_desdeContext,0)


        def sent_repetir(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_repetirContext,0)


        def sent_caso(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_casoContext,0)


        def sent_iterar(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_iterarContext,0)


        def sent_salir_si(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_salir_siContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = PseudocodigoParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sentencia)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.sent_asig()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.sent_lectura()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.sent_impresion()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.sent_condicional()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.sent_mientras()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.sent_desde()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.sent_repetir()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.sent_caso()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 9)
                self.state = 147
                self.sent_iterar()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 10)
                self.state = 148
                self.sent_salir_si()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_asigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def arreglo(self):
            return self.getTypedRuleContext(PseudocodigoParser.ArregloContext,0)


        def ASIG(self):
            return self.getToken(PseudocodigoParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_asig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_asig" ):
                listener.enterSent_asig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_asig" ):
                listener.exitSent_asig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_asig" ):
                return visitor.visitSent_asig(self)
            else:
                return visitor.visitChildren(self)




    def sent_asig(self):

        localctx = PseudocodigoParser.Sent_asigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sent_asig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(PseudocodigoParser.ID)
            self.state = 152
            self.arreglo()
            self.state = 153
            self.match(PseudocodigoParser.ASIG)
            self.state = 154
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_lecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(PseudocodigoParser.LEER, 0)

        def PAR_AB(self):
            return self.getToken(PseudocodigoParser.PAR_AB, 0)

        def lista_id(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_idContext,0)


        def PAR_CE(self):
            return self.getToken(PseudocodigoParser.PAR_CE, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_lectura" ):
                listener.enterSent_lectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_lectura" ):
                listener.exitSent_lectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_lectura" ):
                return visitor.visitSent_lectura(self)
            else:
                return visitor.visitChildren(self)




    def sent_lectura(self):

        localctx = PseudocodigoParser.Sent_lecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sent_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(PseudocodigoParser.LEER)
            self.state = 157
            self.match(PseudocodigoParser.PAR_AB)
            self.state = 158
            self.lista_id(0)
            self.state = 159
            self.match(PseudocodigoParser.PAR_CE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_impresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(PseudocodigoParser.IMPRIMIR, 0)

        def PAR_AB(self):
            return self.getToken(PseudocodigoParser.PAR_AB, 0)

        def lista_expr(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_exprContext,0)


        def PAR_CE(self):
            return self.getToken(PseudocodigoParser.PAR_CE, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_impresion" ):
                listener.enterSent_impresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_impresion" ):
                listener.exitSent_impresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_impresion" ):
                return visitor.visitSent_impresion(self)
            else:
                return visitor.visitChildren(self)




    def sent_impresion(self):

        localctx = PseudocodigoParser.Sent_impresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sent_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(PseudocodigoParser.IMPRIMIR)
            self.state = 162
            self.match(PseudocodigoParser.PAR_AB)
            self.state = 163
            self.lista_expr(0)
            self.state = 164
            self.match(PseudocodigoParser.PAR_CE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def arreglo(self):
            return self.getTypedRuleContext(PseudocodigoParser.ArregloContext,0)


        def lista_id(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_idContext,0)


        def COMA(self):
            return self.getToken(PseudocodigoParser.COMA, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_id" ):
                listener.enterLista_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_id" ):
                listener.exitLista_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_id" ):
                return visitor.visitLista_id(self)
            else:
                return visitor.visitChildren(self)



    def lista_id(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_idContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_lista_id, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(PseudocodigoParser.ID)
            self.state = 168
            self.arreglo()
            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_idContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_id)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    self.match(PseudocodigoParser.COMA)
                    self.state = 172
                    self.match(PseudocodigoParser.ID)
                    self.state = 173
                    self.arreglo() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sent_condicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(PseudocodigoParser.SI, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def ENTONCES(self):
            return self.getToken(PseudocodigoParser.ENTONCES, 0)

        def lista_sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.Lista_sentenciasContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,i)


        def FINSI(self):
            return self.getToken(PseudocodigoParser.FINSI, 0)

        def SINO(self):
            return self.getToken(PseudocodigoParser.SINO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_condicional" ):
                listener.enterSent_condicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_condicional" ):
                listener.exitSent_condicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_condicional" ):
                return visitor.visitSent_condicional(self)
            else:
                return visitor.visitChildren(self)




    def sent_condicional(self):

        localctx = PseudocodigoParser.Sent_condicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sent_condicional)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(PseudocodigoParser.SI)
                self.state = 180
                self.expresion(0)
                self.state = 181
                self.match(PseudocodigoParser.ENTONCES)
                self.state = 182
                self.lista_sentencias(0)
                self.state = 183
                self.match(PseudocodigoParser.FINSI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(PseudocodigoParser.SI)
                self.state = 186
                self.expresion(0)
                self.state = 187
                self.match(PseudocodigoParser.ENTONCES)
                self.state = 188
                self.lista_sentencias(0)
                self.state = 189
                self.match(PseudocodigoParser.SINO)
                self.state = 190
                self.lista_sentencias(0)
                self.state = 191
                self.match(PseudocodigoParser.FINSI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_mientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(PseudocodigoParser.MIENTRAS, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def FINMIENTRAS(self):
            return self.getToken(PseudocodigoParser.FINMIENTRAS, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_mientras" ):
                listener.enterSent_mientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_mientras" ):
                listener.exitSent_mientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_mientras" ):
                return visitor.visitSent_mientras(self)
            else:
                return visitor.visitChildren(self)




    def sent_mientras(self):

        localctx = PseudocodigoParser.Sent_mientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sent_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(PseudocodigoParser.MIENTRAS)
            self.state = 196
            self.expresion(0)
            self.state = 197
            self.lista_sentencias(0)
            self.state = 198
            self.match(PseudocodigoParser.FINMIENTRAS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_desdeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESDE(self):
            return self.getToken(PseudocodigoParser.DESDE, 0)

        def sent_asig(self):
            return self.getTypedRuleContext(PseudocodigoParser.Sent_asigContext,0)


        def HASTA(self):
            return self.getToken(PseudocodigoParser.HASTA, 0)

        def primario(self):
            return self.getTypedRuleContext(PseudocodigoParser.PrimarioContext,0)


        def paso(self):
            return self.getTypedRuleContext(PseudocodigoParser.PasoContext,0)


        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def FINDESDE(self):
            return self.getToken(PseudocodigoParser.FINDESDE, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_desde

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_desde" ):
                listener.enterSent_desde(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_desde" ):
                listener.exitSent_desde(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_desde" ):
                return visitor.visitSent_desde(self)
            else:
                return visitor.visitChildren(self)




    def sent_desde(self):

        localctx = PseudocodigoParser.Sent_desdeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_sent_desde)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(PseudocodigoParser.DESDE)
            self.state = 201
            self.sent_asig()
            self.state = 202
            self.match(PseudocodigoParser.HASTA)
            self.state = 203
            self.primario()
            self.state = 204
            self.paso()
            self.state = 205
            self.lista_sentencias(0)
            self.state = 206
            self.match(PseudocodigoParser.FINDESDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASO(self):
            return self.getToken(PseudocodigoParser.PASO, 0)

        def NUMERO_ENTERO(self):
            return self.getToken(PseudocodigoParser.NUMERO_ENTERO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_paso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaso" ):
                listener.enterPaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaso" ):
                listener.exitPaso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaso" ):
                return visitor.visitPaso(self)
            else:
                return visitor.visitChildren(self)




    def paso(self):

        localctx = PseudocodigoParser.PasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paso)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(PseudocodigoParser.PASO)
                self.state = 209
                self.match(PseudocodigoParser.NUMERO_ENTERO)
                pass
            elif token in [9, 14, 16, 17, 18, 21, 23, 24, 26, 51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_repetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPETIR(self):
            return self.getToken(PseudocodigoParser.REPETIR, 0)

        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def HASTA_QUE(self):
            return self.getToken(PseudocodigoParser.HASTA_QUE, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_repetir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_repetir" ):
                listener.enterSent_repetir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_repetir" ):
                listener.exitSent_repetir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_repetir" ):
                return visitor.visitSent_repetir(self)
            else:
                return visitor.visitChildren(self)




    def sent_repetir(self):

        localctx = PseudocodigoParser.Sent_repetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sent_repetir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(PseudocodigoParser.REPETIR)
            self.state = 214
            self.lista_sentencias(0)
            self.state = 215
            self.match(PseudocodigoParser.HASTA_QUE)
            self.state = 216
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_casoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EN_CASO(self):
            return self.getToken(PseudocodigoParser.EN_CASO, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def SEA(self):
            return self.getToken(PseudocodigoParser.SEA, 0)

        def lista_casos(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_casosContext,0)


        def FINCASO(self):
            return self.getToken(PseudocodigoParser.FINCASO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_caso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_caso" ):
                listener.enterSent_caso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_caso" ):
                listener.exitSent_caso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_caso" ):
                return visitor.visitSent_caso(self)
            else:
                return visitor.visitChildren(self)




    def sent_caso(self):

        localctx = PseudocodigoParser.Sent_casoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_sent_caso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(PseudocodigoParser.EN_CASO)
            self.state = 219
            self.expresion(0)
            self.state = 220
            self.match(PseudocodigoParser.SEA)
            self.state = 221
            self.lista_casos(0)
            self.state = 222
            self.match(PseudocodigoParser.FINCASO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_casosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uncaso(self):
            return self.getTypedRuleContext(PseudocodigoParser.UncasoContext,0)


        def lista_casos(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_casosContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_casos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_casos" ):
                listener.enterLista_casos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_casos" ):
                listener.exitLista_casos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_casos" ):
                return visitor.visitLista_casos(self)
            else:
                return visitor.visitChildren(self)



    def lista_casos(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_casosContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_lista_casos, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.uncaso()
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_casosContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_casos)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    self.uncaso() 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UncasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_num(self):
            return self.getTypedRuleContext(PseudocodigoParser.Const_numContext,0)


        def DP(self):
            return self.getToken(PseudocodigoParser.DP, 0)

        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def OTRO(self):
            return self.getToken(PseudocodigoParser.OTRO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_uncaso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUncaso" ):
                listener.enterUncaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUncaso" ):
                listener.exitUncaso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUncaso" ):
                return visitor.visitUncaso(self)
            else:
                return visitor.visitChildren(self)




    def uncaso(self):

        localctx = PseudocodigoParser.UncasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_uncaso)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.const_num()
                self.state = 235
                self.match(PseudocodigoParser.DP)
                self.state = 236
                self.lista_sentencias(0)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(PseudocodigoParser.OTRO)
                self.state = 239
                self.match(PseudocodigoParser.DP)
                self.state = 240
                self.lista_sentencias(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_iterarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITERAR(self):
            return self.getToken(PseudocodigoParser.ITERAR, 0)

        def lista_sentencias(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_sentenciasContext,0)


        def FINITERAR(self):
            return self.getToken(PseudocodigoParser.FINITERAR, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_iterar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_iterar" ):
                listener.enterSent_iterar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_iterar" ):
                listener.exitSent_iterar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_iterar" ):
                return visitor.visitSent_iterar(self)
            else:
                return visitor.visitChildren(self)




    def sent_iterar(self):

        localctx = PseudocodigoParser.Sent_iterarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sent_iterar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PseudocodigoParser.ITERAR)
            self.state = 244
            self.lista_sentencias(0)
            self.state = 245
            self.match(PseudocodigoParser.FINITERAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sent_salir_siContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALIR_SI(self):
            return self.getToken(PseudocodigoParser.SALIR_SI, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_sent_salir_si

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent_salir_si" ):
                listener.enterSent_salir_si(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent_salir_si" ):
                listener.exitSent_salir_si(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent_salir_si" ):
                return visitor.visitSent_salir_si(self)
            else:
                return visitor.visitChildren(self)




    def sent_salir_si(self):

        localctx = PseudocodigoParser.Sent_salir_siContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sent_salir_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(PseudocodigoParser.SALIR_SI)
            self.state = 248
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO_ENTERO(self):
            return self.getToken(PseudocodigoParser.NUMERO_ENTERO, 0)

        def NUMERO_REAL(self):
            return self.getToken(PseudocodigoParser.NUMERO_REAL, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_const_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_num" ):
                listener.enterConst_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_num" ):
                listener.exitConst_num(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_num" ):
                return visitor.visitConst_num(self)
            else:
                return visitor.visitChildren(self)




    def const_num(self):

        localctx = PseudocodigoParser.Const_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_const_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(PseudocodigoParser.FactorContext,0)


        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def OPSR(self):
            return self.getToken(PseudocodigoParser.OPSR, 0)

        def OP_MOD(self):
            return self.getToken(PseudocodigoParser.OP_MOD, 0)

        def OPREL(self):
            return self.getToken(PseudocodigoParser.OPREL, 0)

        def OPO(self):
            return self.getToken(PseudocodigoParser.OPO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 267
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 255
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 256
                        self.match(PseudocodigoParser.OPSR)
                        self.state = 257
                        self.factor(0)
                        pass

                    elif la_ == 2:
                        localctx = PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 258
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 259
                        self.match(PseudocodigoParser.OP_MOD)
                        self.state = 260
                        self.factor(0)
                        pass

                    elif la_ == 3:
                        localctx = PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 261
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 262
                        self.match(PseudocodigoParser.OPREL)
                        self.state = 263
                        self.factor(0)
                        pass

                    elif la_ == 4:
                        localctx = PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 264
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 265
                        self.match(PseudocodigoParser.OPO)
                        self.state = 266
                        self.factor(0)
                        pass

             
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primario(self):
            return self.getTypedRuleContext(PseudocodigoParser.PrimarioContext,0)


        def factor(self):
            return self.getTypedRuleContext(PseudocodigoParser.FactorContext,0)


        def OPMD(self):
            return self.getToken(PseudocodigoParser.OPMD, 0)

        def OPY(self):
            return self.getToken(PseudocodigoParser.OPY, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.primario()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 281
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PseudocodigoParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 275
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 276
                        self.match(PseudocodigoParser.OPMD)
                        self.state = 277
                        self.primario()
                        pass

                    elif la_ == 2:
                        localctx = PseudocodigoParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 278
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 279
                        self.match(PseudocodigoParser.OPY)
                        self.state = 280
                        self.primario()
                        pass

             
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_AB(self):
            return self.getToken(PseudocodigoParser.PAR_AB, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def PAR_CE(self):
            return self.getToken(PseudocodigoParser.PAR_CE, 0)

        def OPSR(self):
            return self.getToken(PseudocodigoParser.OPSR, 0)

        def primario(self):
            return self.getTypedRuleContext(PseudocodigoParser.PrimarioContext,0)


        def NO(self):
            return self.getToken(PseudocodigoParser.NO, 0)

        def constante(self):
            return self.getTypedRuleContext(PseudocodigoParser.ConstanteContext,0)


        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def arreglo(self):
            return self.getTypedRuleContext(PseudocodigoParser.ArregloContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = PseudocodigoParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primario)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(PseudocodigoParser.PAR_AB)
                self.state = 287
                self.expresion(0)
                self.state = 288
                self.match(PseudocodigoParser.PAR_CE)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(PseudocodigoParser.OPSR)
                self.state = 291
                self.primario()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(PseudocodigoParser.NO)
                self.state = 293
                self.primario()
                pass
            elif token in [39, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.constante()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 5)
                self.state = 295
                self.match(PseudocodigoParser.ID)
                self.state = 296
                self.arreglo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArregloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COR_AB(self):
            return self.getToken(PseudocodigoParser.COR_AB, 0)

        def lista_ind(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_indContext,0)


        def COR_CE(self):
            return self.getToken(PseudocodigoParser.COR_CE, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_arreglo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArreglo" ):
                listener.enterArreglo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArreglo" ):
                listener.exitArreglo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArreglo" ):
                return visitor.visitArreglo(self)
            else:
                return visitor.visitChildren(self)




    def arreglo(self):

        localctx = PseudocodigoParser.ArregloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arreglo)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(PseudocodigoParser.COR_AB)
                self.state = 300
                self.lista_ind(0)
                self.state = 301
                self.match(PseudocodigoParser.COR_CE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_indContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def lista_ind(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_indContext,0)


        def COMA(self):
            return self.getToken(PseudocodigoParser.COMA, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_ind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_ind" ):
                listener.enterLista_ind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_ind" ):
                listener.exitLista_ind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_ind" ):
                return visitor.visitLista_ind(self)
            else:
                return visitor.visitChildren(self)



    def lista_ind(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_indContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_lista_ind, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expresion(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_indContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_ind)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.match(PseudocodigoParser.COMA)
                    self.state = 311
                    self.expresion(0) 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lista_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def lista_expr(self):
            return self.getTypedRuleContext(PseudocodigoParser.Lista_exprContext,0)


        def COMA(self):
            return self.getToken(PseudocodigoParser.COMA, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_lista_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_expr" ):
                listener.enterLista_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_expr" ):
                listener.exitLista_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_expr" ):
                return visitor.visitLista_expr(self)
            else:
                return visitor.visitChildren(self)



    def lista_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.Lista_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_lista_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expresion(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PseudocodigoParser.Lista_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lista_expr)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    self.match(PseudocodigoParser.COMA)
                    self.state = 322
                    self.expresion(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO_ENTERO(self):
            return self.getToken(PseudocodigoParser.NUMERO_ENTERO, 0)

        def NUMERO_REAL(self):
            return self.getToken(PseudocodigoParser.NUMERO_REAL, 0)

        def CONSTANTE_CARACTER(self):
            return self.getToken(PseudocodigoParser.CONSTANTE_CARACTER, 0)

        def CONSTANTE_BOOLEANA(self):
            return self.getToken(PseudocodigoParser.CONSTANTE_BOOLEANA, 0)

        def CONSTANTE_STRING(self):
            return self.getToken(PseudocodigoParser.CONSTANTE_STRING, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_constante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstante" ):
                listener.enterConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstante" ):
                listener.exitConstante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstante" ):
                return visitor.visitConstante(self)
            else:
                return visitor.visitChildren(self)




    def constante(self):

        localctx = PseudocodigoParser.ConstanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_constante)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17042430230528) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.declaraciones_sempred
        self._predicates[6] = self.listadec_id_sempred
        self._predicates[8] = self.lista_indices_sempred
        self._predicates[10] = self.lista_sentencias_sempred
        self._predicates[15] = self.lista_id_sempred
        self._predicates[22] = self.lista_casos_sempred
        self._predicates[27] = self.expresion_sempred
        self._predicates[28] = self.factor_sempred
        self._predicates[31] = self.lista_ind_sempred
        self._predicates[32] = self.lista_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def declaraciones_sempred(self, localctx:DeclaracionesContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def listadec_id_sempred(self, localctx:Listadec_idContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def lista_indices_sempred(self, localctx:Lista_indicesContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def lista_sentencias_sempred(self, localctx:Lista_sentenciasContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def lista_id_sempred(self, localctx:Lista_idContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lista_casos_sempred(self, localctx:Lista_casosContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def lista_ind_sempred(self, localctx:Lista_indContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def lista_expr_sempred(self, localctx:Lista_exprContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         




