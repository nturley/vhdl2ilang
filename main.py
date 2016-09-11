import logging

logging.basicConfig(filename="vhdl2ilang.log", level=logging.DEBUG)

import sys
from antlr4 import *
from vhdlLexer import vhdlLexer
from vhdlParser import vhdlParser
from dotgenerator import DotGenerator
from astgenerator import AstGenerator
from ast2dot import ast2dot

def main(argv):
    input = FileStream(argv[1])
    lexer = vhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = vhdlParser(stream)
    tree = parser.design_file()
    # write the parse tree
    with open('parsetree.dot', 'w') as f:
        printer = DotGenerator(f)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

    astgen = AstGenerator()
    walker.walk(astgen, tree)

    with open('ast.dot', 'w') as f:
        ast2dot(astgen.design, f)

if __name__ == '__main__':
    main(sys.argv)