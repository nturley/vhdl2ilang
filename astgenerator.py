# Generated from vhdl.g4 by ANTLR 4.5.3
from vhdlListener import vhdlListener
from vhdlLexer import vhdlLexer
import logging
import attr

logging.basicConfig(filename="vhdl2ilang.log", level=logging.DEBUG)

def getTerminalType(node):
    if not hasattr(node, 'getSymbol'):
        return -1
    return node.getSymbol().type

class AstNode(object):
    def __init__(self, parent):
        self.parent = parent
        if parent:
            parent.children.append(self)
        self.children = []

    def __repr__(self):
        return self.__class__.__name__

class Design(AstNode):
    pass

class Identifier(AstNode):
    def __init__(self, parent, idstr):
        AstNode.__init__(self, parent)
        self.idstr = idstr

    def __repr__(self):
        return 'ID: ' + self.idstr

#place holder
class DesignUnit(AstNode):
    pass

class EntityDecl(AstNode):
    pass

class EntityArch(AstNode):
    pass

class Library(AstNode):
    pass

class UseClause(AstNode):
    pass

class NamePart(AstNode):
    pass

class Wire(AstNode):
    pass

class ConcAssign(AstNode):
    pass

class PortMode(AstNode):
    pass

class TypeIndication(AstNode):
    pass

class Process(AstNode):
    pass

class SensitivityList(AstNode):
    pass

class VariableDecl(AstNode):
    pass

class VariableAssign(AstNode):
    pass

class ConstantDecl(AstNode):
    pass

#place holder
class SimpleExpr(AstNode):
    pass

class Plus(AstNode):
    pass

class Minus(AstNode):
    pass

class Amp(AstNode):
    pass


class Direction(AstNode):
    def __init__(self, parent, dirstr):
        AstNode.__init__(self, parent)
        self.dirstr = dirstr

    def __repr__(self):
        return self.dirstr


class AstGenerator(vhdlListener):

    def __init__(self, design=None):
        if design is None:
            design = Design(None)
        self.design = design
        self.aststack = [design]

    def replaceParent(self, newnode):
        parent = self.aststack.pop()
        grandparent = self.aststack[-1]
        grandparent.children.remove(parent)
        newnode.children = parent.children
        self.aststack.append(newnode)

    def enterDesign_unit(self, ctx):
        parent = self.aststack[-1]
        newnode = DesignUnit(parent)
        self.aststack.append(newnode)

    def exitDesign_unit(self, ctx):
        self.aststack.pop()

    def enterIdentifier(self, ctx):
        parent = self.aststack[-1]
        Identifier(parent, ctx.getText())

    def enterLogical_name(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(Library(parent))
        
    def exitLogical_name(self, ctx):
        self.aststack.pop()

    def exitSuffix(self, ctx):
        # suffixes either have a terminal or an identifier
        if getTerminalType(ctx.getChild(0)) == vhdlLexer.ALL:
            parent = self.aststack[-1]
            Identifier(parent, 'ALL')

    def enterUse_clause(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(UseClause(parent))

    def exitUse_clause(self, ctx):
        self.aststack.pop()

    def enterEntity_declaration(self, ctx):
        grandparent = self.aststack[-2]
        newnode = EntityDecl(grandparent)
        self.replaceParent(newnode)

    def enterInterface_port_declaration(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(Wire(parent))

    def exitInterface_port_declaration(self, ctx):
        self.aststack.pop()

    def enterArchitecture_body(self, ctx):
        grandparent = self.aststack[-2]
        newnode = EntityArch(grandparent)
        self.replaceParent(newnode)

    def enterConcurrent_signal_assignment_statement(self, ctx):
        parent = self.aststack[-1]
        newnode = ConcAssign(parent)
        self.aststack.append(newnode)

    def exitConcurrent_signal_assignment_statement(self, ctx):
        self.aststack.pop()

    def enterSubtype_indication(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(TypeIndication(parent))

    def exitSubtype_indication(self, ctx):
        self.aststack.pop()

    def enterProcess_statement(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(Process(parent))

    def exitProcess_statement(self, ctx):
        process = self.aststack.pop()

    def enterSensitivity_list(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(SensitivityList(parent))

    def exitSensitivity_list(self, ctx):
        self.aststack.pop()

    def enterVariable_declaration(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(VariableDecl(parent))

    def exitVariable_declaration(self, ctx):
        self.aststack.pop()

    def enterVariable_assignment_statement(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(VariableAssign(parent))

    def exitVariable_assignment_statement(self, ctx):
        self.aststack.pop()

    def enterDirection(self, ctx):
        parent = self.aststack[-1]
        Direction(parent, ctx.getText())

    def enterConstant_declaration(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(ConstantDecl(parent))

    def exitConstant_declaration(self, ctx):
        self.aststack.pop()

    def enterSimple_expression(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(SimpleExpr(parent))

    def exitSimple_expression(self, ctx):
        self.aststack.pop()

    def enterSignal_declaration(self, ctx):
        parent = self.aststack[-1]
        self.aststack.append(Wire(parent))

    def exitSignal_declaration(self, ctx):
        self.aststack.pop()

    def enterAdding_operator(self, ctx):
        replace = self.aststack.pop()
        parent = self.aststack[-1]
        parent.children.pop()
        term = getTerminalType(ctx.getChild(0))
        if term == vhdlLexer.PLUS:
            newnode = Plus(parent)
        elif term == vhdlLexer.MINUS:
            newnode = Minus(parent)
        elif term == vhdlLexer.AMPERSAND:
            newnode = Amp(parent)
        else:
            raise Exception('Unknown Adding operator')
        newnode.children = replace.children
        self.aststack.append(newnode)


        


