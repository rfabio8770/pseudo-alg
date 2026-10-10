grammar Pseudocodigo;

// ==========================================
// REGLAS DEL PARSER (Gramática)
// ==========================================

programa        : ALGORITMO ID sec_decl cuerpo PUNTO ;

sec_decl        : dec_variables ;

dec_variables   : VAR declaraciones ;

declaraciones   : declaraciones declaracion
                | declaracion
                ;

declaracion     : tipo listadec_id ;

tipo            : ENTERO
                | CARACTER
                | BOOLEANO
                | REAL
                | STRING
                ;

listadec_id     : listadec_id COMA ID es_arreglo
                | ID es_arreglo
                ;

es_arreglo      : COR_AB lista_indices COR_CE
                | /* epsilon */
                ;

lista_indices   : lista_indices COMA NUMERO_ENTERO
                | NUMERO_ENTERO
                ;

cuerpo          : INICIO lista_sentencias FIN ;

lista_sentencias: lista_sentencias sentencia
                | sentencia
                ;

sentencia       : sent_asig
                | sent_lectura
                | sent_impresion
                | sent_condicional
                | sent_mientras
                | sent_desde
                | sent_repetir
                | sent_caso
                | sent_iterar
                | sent_salir_si
                ;

sent_asig       : ID arreglo ASIG expresion ;

sent_lectura    : LEER PAR_AB lista_id PAR_CE ;

sent_impresion  : IMPRIMIR PAR_AB lista_expr PAR_CE ;

lista_id        : lista_id COMA ID arreglo
                | ID arreglo
                ;

sent_condicional: SI expresion ENTONCES lista_sentencias FINSI
                | SI expresion ENTONCES lista_sentencias SINO lista_sentencias FINSI
                ;

sent_mientras   : MIENTRAS expresion lista_sentencias FINMIENTRAS ;

sent_desde      : DESDE sent_asig HASTA primario paso lista_sentencias FINDESDE ;

paso            : PASO NUMERO_ENTERO
                | /* epsilon */
                ;

sent_repetir    : REPETIR lista_sentencias HASTA_QUE expresion ;

sent_caso       : EN_CASO expresion SEA lista_casos FINCASO ;

lista_casos     : lista_casos uncaso
                | uncaso
                ;

uncaso          : const_num DP lista_sentencias
                | OTRO DP lista_sentencias
                ;

sent_iterar     : ITERAR lista_sentencias FINITERAR ;

sent_salir_si   : SALIR_SI expresion ;

const_num       : NUMERO_ENTERO
                | NUMERO_REAL
                ;

expresion       : expresion OPSR factor
                | expresion OP_MOD factor
                | expresion OPREL factor
                | expresion OPO factor
                | factor
                ;

factor          : factor OPMD primario
                | factor OPY primario
                | primario
                ;

primario        : PAR_AB expresion PAR_CE
                | OPSR primario
                | NO primario
                | constante
                | ID arreglo
                ;

arreglo         : COR_AB lista_ind COR_CE
                | /* epsilon */
                ;

lista_ind       : lista_ind COMA expresion
                | expresion
                ;

lista_expr      : lista_expr COMA expresion
                | expresion
                ;

constante       : NUMERO_ENTERO
                | NUMERO_REAL
                | CONSTANTE_CARACTER
                | CONSTANTE_BOOLEANA
                | CONSTANTE_STRING
                ;

// ==========================================
// REGLAS DEL LEXER (Tokens)
// ==========================================

ALGORITMO   : 'algoritmo' | 'ALGORITMO' ;
ENTERO      : 'entero' | 'ENTERO' ;
CARACTER    : 'caracter' | 'CARACTER' ;
REAL        : 'real' | 'REAL' ;
BOOLEANO    : 'booleano' | 'BOOLEANO' ;
STRING      : 'string' | 'STRING' ;
INICIO      : 'inicio' | 'INICIO' ;
FIN         : 'fin' | 'FIN' ;
SI          : 'si' | 'SI' ;
ENTONCES    : 'entonces' | 'ENTONCES' ;
SINO        : 'sino' | 'SINO' ;
FINSI       : 'finsi' | 'FINSI' ;
PASO        : 'paso' | 'PASO' ;
MIENTRAS    : 'mientras' | 'MIENTRAS' ;
FINMIENTRAS : 'finmientras' | 'FINMIENTRAS' ;
LEER        : 'leer' | 'LEER' ;
IMPRIMIR    : 'imprimir' | 'IMPRIMIR' ;
DESDE       : 'desde' | 'DESDE' ;
FINDESDE    : 'findesde' | 'FINDESDE' ;
HASTA       : 'hasta' | 'HASTA' ;
REPETIR     : 'repetir' | 'REPETIR' ;
HASTA_QUE   : 'hasta_que' | 'HASTA_QUE' ;
ITERAR      : 'iterar' | 'ITERAR' ;
SALIR_SI    : 'salir_si' | 'SALIR_SI' ;
FINITERAR   : 'finiterar' | 'FINITERAR' ;
EN_CASO     : 'en_caso' | 'EN_CASO' ;
DP          : ':' ;
FINCASO     : 'fincaso' | 'FINCASO' ;
OTRO        : 'otro' | 'OTRO' ;
SEA         : 'sea' | 'SEA' ;
VAR         : 'var' | 'VAR' ;

ASIG        : '<-' | '=' ;
COMA        : ',' ;
PAR_AB      : '(' ;
PAR_CE      : ')';
COR_AB      : '[' ;
COR_CE      : ']' ;
PUNTO       : '.' ;

CONSTANTE_BOOLEANA  : 'verdadero' | 'falso' | 'VERDADERO' | 'FALSO' ;
NUMERO_ENTERO       : [0-9]+ ;
NUMERO_REAL         : [0-9]+ '.' [0-9]+ ;
CONSTANTE_CARACTER  : '\'' . '\'' ;
CONSTANTE_STRING    : '"' ~["\r\n]* '"' ;

OPSR        : '+' | '-' ;
OP_MOD      : 'mod' | 'MOD' ;
OPREL       : '==' | '<>' | '<' | '<=' | '>' | '>=' ;
OPO         : 'o' | 'O' | 'or' | 'OR' ;
OPY         : 'y' | 'Y' | 'and' | 'AND' ;
OPMD        : '*' | '/' ;
NO          : 'no' | 'NO' | 'not' | 'NOT' ;

ID          : [a-zA-Z_] [a-zA-Z0-9_]* ;

WS          : [ \t\r\n]+ -> skip ;