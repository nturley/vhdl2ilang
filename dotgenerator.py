from antlr4 import *
from vhdlParser import *
# This class defines a complete listener for a parse tree produced by vhdlParser.

def getrulename(ctx):
    if ctx.getAltNumber() != ATN.INVALID_ALT_NUMBER:
        return vhdlParser.ruleNames[ctx.getRuleIndex()]+":"+str(ctx.getAltNumber())
    else:
        return vhdlParser.ruleNames[ctx.getRuleIndex()]

class DotGenerator(ParseTreeListener):

    def __init__(self, f):
        self.f = f
        self.auto_index = 0
        f.write('''
digraph {
  ordering=out;
  ranksep=.4;
  bgcolor="lightgrey";
  node [shape=box, fixedsize=false, fontsize=12, fontname="Helvetica-bold", fontcolor="blue"
    width=.25, height=.25, color="black", fillcolor="white", style="filled, solid, bold"];
  edge [arrowsize=.5, color="black", style="bold"]
''')

    def visitTerminal(self, node):
        dotname = 'n' + str(self.auto_index)
        self.auto_index += 1
        self.f.write('  ' + dotname + ' [label="' + node.getText().strip() + '"];\n')
        self.f.write('  ' + node.parentCtx.dotname + ' -> ' + dotname + '\n')

    def visitErrorNode(self, node):
        print 'error'

    def enterEveryRule(self, ctx):
        ctx.dotname = 'n' + str(self.auto_index)
        self.auto_index += 1
        self.f.write('  ' + ctx.dotname + ' [label="' + getrulename(ctx) + '"];\n')

    def exitEveryRule(self, ctx):
        if ctx.parentCtx:
            self.f.write('  ' + ctx.parentCtx.dotname + ' -> ' + ctx.dotname + '\n')
        else:
            self.f.write('}\n')

