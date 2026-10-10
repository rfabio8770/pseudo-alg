import sys
from antlr4 import *
from PseudocodigoLexer import PseudocodigoLexer
from PseudocodigoParser import PseudocodigoParser
from InterpreterVisitor import InterpreterVisitor

def main():
    # Supongamos que tu código fuente está en un archivo llamado 'programa.txt'
    archivo_fuente = sys.argv[1] if len(sys.argv) > 1 else "programa.txt"
    
    input_stream = FileStream(archivo_fuente, encoding='utf-8')
    lexer = PseudocodigoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudocodigoParser(stream)
    
    tree = parser.programa()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Se encontraron errores de sintaxis.")
        return

    # Instanciamos nuestro Visitor y recorremos el árbol
    visitor = InterpreterVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()