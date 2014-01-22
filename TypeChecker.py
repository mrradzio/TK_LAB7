#!/usr/bin/python


from SymbolTable import FunctionsTable
from SymbolTable import SymbolTable

class TypeChecker(object):
    errors = []
    
    
    def __init__(self):
        self.ttype = {'+': {'string': {'string': 'string'}, 'int': {'float': 'float', 'int': 'int'}, 'float': {'int': 'float', 'float': 'float'}},
                      '-': {'int': {'int': 'int','float': 'float'}, 'float': {'int': 'float', 'float': 'float'}},
                      '*': {'string': {'int': 'string'}, 'int': {'int': 'int', 'float': 'float', 'string': 'string'}, 'float': {'int:':'float' , 'float':'float'}},
                      '/': {'int': {'int': 'float', 'float': 'float'}, 'float': {'float': 'float'} },
                      '!=': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '<': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '<=': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '>': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '>=': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '==': {'string': {'string': 'string'}, 'int': {'float': 'int', 'int': 'int'}, 'float': {'int': 'int', 'float': 'int'}},
                      '%': {'int': {'int': 'int'}},
                      '^': {'int': {'int': 'int', 'float' : 'float'}, 'float':{'int':'float' , 'float':'float'}},
                      '&': {'int': {'int': 'int'}},
                      'AND': {'int': {'int': 'int'}},
                      'OR': {'int': {'int': 'int'}},
                      'SHL': {'int': {'int': 'int'}},
                      'SHR': {'int': {'int': 'int'}},
                      'EQ': {'int': {'int': 'int'}},
                      'NEQ': {'int': {'int': 'int'}},
                      'LE': {'int': {'int': 'int'}},
                      'GE': {'int': {'int': 'int'}},
                      }

    #def visit_BinExpr(self, node):
        #type1 = node.left.accept(self)
        #type2 = node.right.accept(self)
        #op    = node.op;
        ## ... 
        ##
 
    #def visit_RelExpr(self, node):
        #type1 = node.left.accept(self);
        #type2 = node.right.accept(self);
        ## ... 
        ##


    #def visit_Integer(self, node):
        #return 'int'

    #def visit_Float(self, node):
    # ... 
    # 

    # ... 
    # 

#############################################################################################

    def visit_Program(self, node):
        node.Functions = FunctionsTable(None, "Functions")
        node.Variables = SymbolTable(None, "Variables")
        node.declarations.Functions = node.Functions
        node.declarations.Variables = node.Variables
        node.fundefs.Functions = node.Functions
        node.fundefs.Variables = node.Variables
        node.instructions.Functions = node.Functions
        node.instructions.Variables = node.Variables
        
        node.declarations.accept(self)
        node.fundefs.accept(self)
        node.instructions.accept(self)
        return self.errors

    def visit_Declarations(self, node):
        if node.declarations != None:
            node.declarations.Functions = node.Functions
            node.declarations.Variables = node.Variables
            node.declarations.accept(self)
        
        if node.declaration != None:
            node.declaration.Functions = node.Functions
            node.declaration.Variables = node.Variables
            node.declaration.accept(self)

            
    def visit_Declaration(self, node):
        node.inits.Functions = node.Functions
        node.inits.Variables = node.Variables
        self.visit_Inits(node.inits, node.type)


    def visit_Inits(self, node, type):
        node.init.Functions = node.Functions
        node.init.Variables = node.Variables
        self.visit_Init(node.init, type)
        if node.inits != None:
            node.inits.Functions = node.Functions
            node.inits.Variables = node.Variables
            self.visit_Inits(node.inits, type)
                       
    def visit_Init(self, node, type):
        # add declaration name = node.id, symbol = type
        if node.Variables.put(node.id, type)==-1:
            self.errors.append("In line "+ str(node.lineno) + ": Variable "+ node.id + " already initialized")
            
    def visit_Instructions(self, node):
        if node.instructions != None:
            node.instructions.Functions = node.Functions
            node.instructions.Variables = node.Variables
            node.instructions.accept(self)
        node.instruction.Functions = node.Functions
        node.instruction.Variables = node.Variables
        node.instruction.accept(self)
        
    def visit_Instruction(self, node):
        node.instruction.Functions = node.Functions
        node.instruction.Variables = node.Variables
        node.instruction.accept(self)
        
    def visit_Print_instr(self, node):
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        node.expression.accept(self)
        
    def visit_Labeled_instr(self, node):
        node.instruction.Functions = node.Functions
        node.instruction.Variables = node.Variables
        node.instruction.accept(self)
    
    def visit_Assignment(self, node):
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        type2 = node.expression.accept(self)
        type1 = node.Variables.get(node.id)
        if type1 == -1:
            self.errors.append("In line "+ str(node.lineno) + ": Variable " + node.id +" was not declared")
        elif type2 == -1:
            self.errors.append("In line "+ str(node.lineno) + ": Incorrect expression")
        elif type1 != type2:
            self.errors.append("In line "+ str(node.lineno) + ": Can't assign " + str(type2) + " to "+str(type1))
        
    def visit_Choice_instr(self, node):
        node.condition.Functions = node.Functions
        node.condition.Variables = node.Variables
        node.condition.accept(self)
        node.instruction.Functions = FunctionsTable(node.Functions, "Functions")
        node.instruction.Variables = SymbolTable(node.Variables, "Variables")
        node.instruction.accept(self)
        
        if node.elseinstruction != None:
            node.elseinstruction.Functions = FunctionsTable(node.Functions, "Functions")
            node.elseinstruction.Variables = SymbolTable(node.Variables, "Variables")
            node.elseinstruction.accept(self)
            
    def visit_While_instr(self, node):
        node.condition.Functions = node.Functions
        node.condition.Variables = node.Variables
        node.condition.accept(self)
        node.instruction.Functions = FunctionsTable(node.Functions, "Functions")
        node.instruction.Variables = SymbolTable(node.Variables, "Variables")
        node.instruction.accept(self)
        
    def visit_Repeat_instr(self, node):
        Functions = FunctionsTable(node.Functions, "Functions")
        Variables = SymbolTable(node.Variables, "Variables")
        node.instructions.Functions = Functions
        node.instructions.Variables = Variables
        node.instructions.accept(self)
        node.condition.Functions = Functions
        node.condition.Variables = Variables
        node.condition.accept(self)
        
    def visit_Return_instr(self, node):
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        node.expression.accept(self)
        
    def visit_Compound_instr(self, node):
        Functions = FunctionsTable(node.Functions, "Functions")
        Variables = SymbolTable(node.Variables, "Variables")
        node.declarations.Functions = Functions
        node.declarations.Variables = Variables
        node.declarations.accept(self)
        node.instructions.Functions = Functions
        node.instructions.Variables = Variables
        node.instructions.accept(self)
        
    def visit_Condition(self, node):
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        node.expression.accept(self)
        
    def visit_Expression(self, node):
        if node.id_or_const != None:
            if node.id_or_const.__class__.__name__ == "Const":
                node.id_or_const.Functions = node.Functions
                node.id_or_const.Variables = node.Variables
                return node.id_or_const.accept(self)
            if node.Variables.get(node.id_or_const)== -1:
                self.errors.append("In line "+ str(node.lineno) + ": Couldn't find the variable" +node.id_or_const+ " in a current scope")
                return 'int'
            return node.Variables.get(node.id_or_const)
        node.expression1.Functions = node.Functions
        node.expression1.Variables = node.Variables
        type1 = node.expression1.accept(self)
        node.expression2.Functions = node.Functions
        node.expression2.Variables = node.Variables
        type2 = node.expression2.accept(self)
        #print type1 + str(node.typeexpr) +type2
        if node.typeexpr in self.ttype.keys() and type1 in self.ttype[node.typeexpr].keys() and type2 in self.ttype[node.typeexpr][type1].keys():
            return  self.ttype[node.typeexpr][type1][type2]
        else:
            print str(type1) + node.typeexpr + str(type2)
            self.errors.append("In line "+ str(node.lineno) + ": Invalid expression")
            return 'int'

    def visit_ExprInBrackets(self,node):
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        return node.expression.accept(self)

    def visit_Const(self, node):
        return node.const_value[1]
    
    def visit_Funcalls(self, node):
        type1 = node.Functions.get(node.id)
        node.expr_list_or_empty.Functions = node.Functions
        node.expr_list_or_empty.Variables = node.Variables
        type2 = node.expr_list_or_empty.accept(self)      
        if type1[0] != type2:
            self.errors.append("In line "+ str(node.lineno) + ": Function call arguments don't match the definition")
        return type1[1]
            

    def visit_Expr_list_or_empty(self, node):
        node.expr_list.Functions = node.Functions
        node.expr_list.Variables = node.Variables
        if node.expr_list != None:
            return node.expr_list.accept(self)
        else:
            return None
        
    def visit_Expr_list(self, node):
        l1 = []
        if node.expr_list != None:
            node.expr_list.Functions = node.Functions
            node.expr_list.Variables = node.Variables
            l1.extend(node.expr_list.accept(self))
        node.expression.Functions = node.Functions
        node.expression.Variables = node.Variables
        l1.append(node.expression.accept(self))
        return l1

    def visit_Fundefs(self, node):
        if node.fundef != None:
            node.fundef.Functions = node.Functions
            node.fundef.Variables = node.Variables
            node.fundef.accept(self)
        
        if node.fundefs != None:
            node.fundefs.Functions = node.Functions
            node.fundefs.Variables = node.Variables
            node.fundefs.accept(self)

    def visit_Fundef(self, node):
        node.Functions.putNewFun(node.id, node.type) 
        Functions = FunctionsTable(node.Functions, "Functions")
        Variables = SymbolTable(node.Variables, "Variables")
        node.arg_list.Functions = Functions
        node.arg_list.Variables = Variables
        listOfArguments = node.arg_list.accept(self)
        for element in listOfArguments:
            if element!= None:
                node.Functions.put(node.id, element[1])
                #Functions.put(element[0], element[1]) # for recursion
                if Variables.put(element[0], element[1])==-1:
                    self.errors.append("In line "+ str(node.lineno) + ": Variable "+ element.name + " already initialized")
        node.compound_instr.Functions = Functions
        node.compound_instr.Variables = Variables
        node.compound_instr.accept(self)
                
    def visit_Args_list_or_empty(self, node):
        node.args_list.Functions = node.Functions
        node.args_list.Variables = node.Variables
        if node.args_list != None:
            return node.args_list.accept(self) 
        else:
            return None
        
    def visit_Args_list(self, node):
        l1 = []
        if node.args_list != None:
            node.args_list.Functions = node.Functions
            node.args_list.Variables = node.Variables
            l1.extend(node.args_list.accept(self))
        node.arg.Functions = node.Functions
        node.arg.Variables = node.Variables
        l1.append(node.arg.accept(self))
        return l1
    
    def visit_Arg(self,node):
        return node.id, node.type