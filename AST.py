#!/usr/bin/python
# Gabriela Fidyk, Mateusz Radko

class Node:

    def __str__(self):
        return  self.printTree(0)


    def accept(self, visitor):
        className = self.__class__.__name__
        # return visitor.visit_<className>(self)
        meth = getattr(visitor, 'visit_' + className, None)
        if meth!=None:
            return meth(self)


class Program(Node):
    def __init__(self,lineno, declarations, fundefs, instructions):
        self.lineno = lineno
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions


class Declarations(Node):
    def __init__(self,lineno,  declarations = None , declaration = None ):
        self.lineno = lineno
        self.declarations = declarations
        self.declaration = declaration


class Declaration(Node):
    def __init__(self,lineno,  type, inits = None):
        self.lineno = lineno
        self.type = type
        self.inits = inits


class Inits(Node):
    def __init__(self,lineno,  init, inits = None):
        self.lineno = lineno
        self.init = init
        self.inits = inits


class Init(Node):
    def __init__(self,lineno, id, expression):
        self.lineno = lineno
        self.id = id
        self.expression = expression


class Instructions(Node):
    def __init__(self,lineno,  instruction ,instructions = None):
        self.lineno = lineno
        self.instructions = instructions
        self.instruction = instruction


class Instruction(Node):
    def __init__(self,lineno,  instruction):
        self.lineno = lineno
        self.instruction = instruction


class Print_instr(Node):
    def __init__(self,lineno, expression):
        self.lineno = lineno
        self.expression = expression


class Labeled_instr(Node):
    def __init__(self,lineno, id, instruction):
        self.lineno = lineno
        self.id = id
        self.instruction = instruction


class Assignment(Node):
    def __init__(self,lineno, id, expression):
        self.lineno = lineno
        self.id = id
        self.expression = expression


class Choice_instr(Node):
    def __init__(self,lineno, condition, instruction, elseinstruction = None):
        self.lineno = lineno
        self.condition = condition
        self.instruction = instruction
        self.elseinstruction = elseinstruction


class While_instr(Node):
    def __init__(self,lineno, condition, instruction):
        self.lineno = lineno
        self.condition = condition
        self.instruction = instruction


class Repeat_instr(Node):
    def __init__(self,lineno, instructions, condition):
        self.lineno = lineno
        self.instructions = instructions
        self.condition = condition


class Return_instr(Node):
    def __init__(self,lineno, expression):
        self.lineno = lineno
        self.expression = expression


class Continue_instr(Node):
    pass

class Break_instr(Node):
    pass


class Compound_instr(Node):
    def __init__(self,lineno, declarations, instructions):
        self.lineno = lineno
        self.declarations = declarations
        self.instructions = instructions


class Condition(Node):
    def __init__(self,lineno, expression):
        self.lineno = lineno
        self.expression = expression

class Const(Node):
    def __init__(self,lineno, const_value):
        self.lineno = lineno
        self.const_value = const_value


class Expression(Node):
    def __init__(self,lineno, expression1, typeexpr, expression2, id_or_const = None):
        self.lineno = lineno
        self.expression1 = expression1
        self.typeexpr = typeexpr
        self.expression2 = expression2
        self.id_or_const = id_or_const

class Funcalls(Node):
    def __init__(self,lineno, id, expr_list_or_empty):
        self.lineno = lineno
        self.id = id
        self.expr_list_or_empty = expr_list_or_empty


class ExprInBrackets(Node):
    def __init__(self,lineno, expression):
        self.lineno = lineno
        self.expression = expression

class Expr_list_or_empty(Node):
    def __init__(self,lineno, expr_list = None):
        self.lineno = lineno
        self.expr_list = expr_list


class Expr_list(Node):
    def __init__(self,lineno, expression, expr_list=None):
        self.lineno = lineno
        self.expr_list = expr_list
        self.expression = expression


class Fundefs(Node):
    def __init__(self,lineno, fundef = None, fundefs = None):
        self.lineno = lineno
        self.fundef = fundef
        self.fundefs = fundefs


class Fundef(Node):
    def __init__(self,lineno, type, id, args_list_or_empty, compound_instruction):
        self.lineno = lineno
        self.type = type
        self.id = id
        self.arg_list = args_list_or_empty
        self.compound_instr = compound_instruction


class Args_list_or_empty(Node):
    def __init__(self,lineno, args_list = None):
        self.lineno = lineno
        self.args_list = args_list

class Args_list(Node):
    def __init__(self,lineno, arg, args_list = None):
        self.lineno = lineno
        self.args_list = args_list
        self.arg = arg

class Arg(Node):
    def __init__(self,lineno, type, id):
        self.lineno = lineno
        self.type = type
        self.id = id

