
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__,func)
        return func
    return decorator

def addIndent(indent):
    result = ""
    i = 0
    while i < indent:
        result += "| "
        i += 1
    return result

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent):
        result = addIndent(indent)
        return result


    @addToClass(AST.Program)
    def printTree(self, indent):
        result = ""
        if self.declarations is not None:
            result += "DECL\n"
            result += addIndent(indent)
            result += self.declarations.printTree(indent)
        result += addIndent(indent)
        result += self.fundefs.printTree(indent)
        result += addIndent(indent)
        result += self.instructions.printTree(indent)
        return result

    @addToClass(AST.Declarations)
    def printTree(self, indent):
        result = ""
        if self.declarations is not None:
            result += self.declarations.printTree(indent)
        if self.declaration is not None:
            result += self.declaration.printTree(indent)
        return result

    @addToClass(AST.Declaration)
    def printTree(self, indent):
        result = ""
        if self.inits is None:
            result =+ self.type
        result += self.inits.printTree(indent)
        return result

    @addToClass(AST.Inits)
    def printTree(self, indent):
        result = ""
        if self.inits is not None:
            result += self.inits.printTree(indent)
        result += self.init.printTree(indent+1)
        return result

    @addToClass(AST.Init)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent) + "=\n"
        result += addIndent(indent+1)
        result += self.id
        result += "\n"
        result += self.expression.printTree(indent+1)
        return result

    @addToClass(AST.Instructions)
    def printTree(self, indent):
        result = ""
        if self.instructions is not None:
            result += self.instructions.printTree(indent)
        #result += addIndent(indent)
        result += self.instruction.printTree(indent)
        return result

    @addToClass(AST.Instruction)
    def printTree(self, indent):
        result = ""
        result += self.instruction.printTree(indent)
        return result

    @addToClass(AST.Print_instr)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent)
        result += "PRINT\n" + self.expression.printTree(indent+1)
        return result

    @addToClass(AST.Labeled_instr)
    def printTree(self, indent):
        result = ""
        return result

    @addToClass(AST.Assignment)
    def printTree(self, indent):
        result = ""
        result = addIndent(indent)
        result += "=\n"
        result += addIndent(indent+1)
        result += self.id +"\n"
        result += self.expression.printTree(indent+1)
        return result

    @addToClass(AST.Choice_instr)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent) + "IF\n"
        result += self.condition.printTree(indent+1)
        result += self.instruction.printTree(indent+1)
        if self.elseinstruction is not None:
            result += addIndent(indent)+ "ELSE\n"
            result += self.elseinstruction.printTree(indent+1)
        return result

    @addToClass(AST.While_instr)
    def printTree(self, indent):
        result = addIndent(indent) + "WHILE\n"
        result += self.condition.printTree(indent+1)
        result += self.instruction.printTree(indent+1)
        return result

    @addToClass(AST.Repeat_instr)
    def printTree(self, indent):
        result = addIndent(indent) + "REPEAT\n"
        result += self.instructions.printTree(indent+1)
        result += addIndent(indent)
        result += "UNTIL\n"
        result += self.condition.printTree(indent+1)
        return result

    @addToClass(AST.Return_instr)
    def printTree(self, indent):
        result = addIndent(indent) + "RETURN\n" + self.expression.printTree(indent+1)
        return result

    @addToClass(AST.Continue_instr)
    def printTree(self, indent):
        result = addIndent(indent) + "CONTINUE\n"
        return result

    @addToClass(AST.Break_instr)
    def printTree(self, indent):
        result = addIndent(indent) + "BREAK\n"
        return result

    @addToClass(AST.Compound_instr)
    def printTree(self, indent):
        result = ""
        if self.declarations is not None:
            if self.declarations.printTree(indent) != "":
                result += addIndent(indent)+"DECL\n"
                result += self.declarations.printTree(indent)
        result += self.instructions.printTree(indent)
        return result

    @addToClass(AST.Condition)
    def printTree(self, indent):
        result = ""
        result += self.expression.printTree(indent)
        return result

    @addToClass(AST.Const)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent)
        result += self.const_value[0] +"\n"
        return result

    @addToClass(AST.Expression)
    def printTree(self, indent):
        result = ""
        if self.id_or_const is not None:
            if isinstance(self.id_or_const,str):
                result +=addIndent(indent) + self.id_or_const+"\n"
            else:
                result += self.id_or_const.printTree(indent)
        else:
            result += addIndent(indent)
            result += self.typeexpr +"\n"
            result += self.expression1.printTree(indent+1)
            result += self.expression2.printTree(indent+1)
        return result

    @addToClass(AST.Funcalls)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent) + "FUNCALL\n"
        result += addIndent(indent+1) + self.id +"\n"
        result += self.expr_list_or_empty.printTree(indent+2)
        return result


    @addToClass(AST.ExprInBrackets)
    def printTree(self, indent):
        result = ""
        result += self.expression.printTree(indent)
        return result


    @addToClass(AST.Expr_list_or_empty)
    def printTree(self, indent):
        result = ""
        if self.expr_list is not None:
            result += self.expr_list.printTree(indent)
        return result

    @addToClass(AST.Expr_list)
    def printTree(self, indent):
        result = ""
        if self.expr_list is not None:
            result += self.expr_list.printTree(indent)
        result += self.expression.printTree(indent)
        return result



    @addToClass(AST.Fundefs)
    def printTree(self, indent):
        result = ""
        if self.fundef is not None:
            result += self.fundef.printTree(indent)
        if self.fundefs is not None:
            result += self.fundefs.printTree(indent)

        return result

    @addToClass(AST.Fundef)
    def printTree(self, indent):
        result = "FUNDEF\n"
        result += addIndent(indent+1)
        result += self.id +"\n"
        result += addIndent(indent+1)
        result += "RET " + self.type + "\n"
        result += self.arg_list.printTree(indent+1)
        result += self.compound_instr.printTree(indent+1)
        return result

    @addToClass(AST.Args_list_or_empty)
    def printTree(self, indent):
        result = ""
        if self.args_list is not None:
            result += self.args_list.printTree(indent)
        return result

    @addToClass(AST.Args_list)
    def printTree(self, indent):
        result = ""
        if self.args_list is not None:
            result += self.args_list.printTree(indent)
        result += self.arg.printTree(indent)
        return result

    @addToClass(AST.Arg)
    def printTree(self, indent):
        result = ""
        result += addIndent(indent) + "ARG " + self.id + "\n"
        return result