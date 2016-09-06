# Generated from vhdl.g4 by ANTLR 4.5.3
from vhdlListener import vhdlListener
from vhdlLexer import vhdlLexer


def getTerminalType(node):
    if not hasattr(node, 'getSymbol'):
        return -1
    return node.getSymbol().type


class AstNode(object):

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    def name(self):
        if hasattr(self, 'myid'):
            return self.typestr + ' : ' + self.myid
        return self.typestr

class Design(AstNode):
    typestr = 'design'
    def __init__(self):
        AstNode.__init__(self, None)

class DesignUnit(AstNode):
    typestr = 'design unit'
    def __init__(self, design):
        AstNode.__init__(self, design)

class Library(AstNode):
    typestr = 'library'
    def __init__(self, design_unit, myid):
        AstNode.__init__(self, design_unit)
        self.myid = myid

class UseClause(AstNode):
    typestr = 'use clause'
    def __init__(self, design_unit):
        AstNode.__init__(self, design_unit)


class NamePart(AstNode):
    typestr = 'name part'
    def __init__(self, parent, myid):
        AstNode.__init__(self, parent)
        self.myid = myid

class Wire(AstNode):
    typestr = 'wire'
    def __init__(self, parent):
        AstNode.__init__(self, parent)

# This class defines a complete listener for a parse tree produced by vhdlParser.
class AstGenerator(vhdlListener):

    def __init__(self, design=None):
        if design is None:
            design = Design()
        self.design = design
        self.aststack = [design]


    # Enter a parse tree produced by vhdlParser#design_file.
    def enterDesign_unit(self, ctx):
        ctx.identifiers = []
        parent = self.aststack[-1]
        newnode = DesignUnit(parent)
        self.aststack.append(newnode)

    # Exit a parse tree produced by vhdlParser#design_file.
    def exitDesign_unit(self, ctx):
        self.aststack.pop()


    # Enter a parse tree produced by vhdlParser#identifier.
    def enterIdentifier(self, ctx):
        if hasattr(ctx.parentCtx, 'identifiers'):
            ctx.parentCtx.identifiers.append(ctx.getText())

    # Enter a parse tree produced by vhdlParser#logical_name.
    def enterLogical_name(self, ctx):
        ctx.identifiers = []

    def exitLogical_name(self, ctx):
        parent = self.aststack[-1]
        assert len(ctx.identifiers) is 1
        newnode = Library(parent, ctx.identifiers[0])

    def enterSelected_name(self, ctx):
        ctx.identifiers = []

    def exitSelected_name(self, ctx):
        if hasattr(ctx.parentCtx, 'clauses'):
            ctx.parentCtx.clauses.append(ctx.identifiers)

    # Enter a parse tree produced by vhdlParser#suffix.
    def enterSuffix(self, ctx):
        ctx.identifiers = []

    # Exit a parse tree produced by vhdlParser#suffix.
    def exitSuffix(self, ctx):
        if getTerminalType(ctx.getChild(0)) == vhdlLexer.ALL:
            ctx.identifiers = ['ALL']
        assert len(ctx.identifiers)==1
        ctx.parentCtx.identifiers.append(ctx.identifiers[0])

    # Enter a parse tree produced by vhdlParser#use_clause.
    def enterUse_clause(self, ctx):
        ctx.clauses = []

    # Exit a parse tree produced by vhdlParser#use_clause.
    def exitUse_clause(self, ctx):
        parent = self.aststack[-1]
        for clause in ctx.clauses:
            newnode = UseClause(parent)
            for name in clause:
                newchild = NamePart(newnode, name)

    def enterEntity_declaration(self, ctx):
        ctx.identifiers = []

    def exitEntity_declaration(self, ctx):
        pass

    def enterInterface_port_declaration(self, ctx):
        ctx.portnames = []

    def exitInterface_port_declaration(self, ctx):
        parent = self.aststack[-1]
        for port in ctx.portnames:
            newnode = Wire(parent)


    def enterIdentifier_list(self, ctx):
        ctx.identifiers = []

    def exitIdentifier_list(self, ctx):
        if hasattr(ctx.parentCtx, 'portnames'):
            ctx.parentCtx.portnames = ctx.identifiers




