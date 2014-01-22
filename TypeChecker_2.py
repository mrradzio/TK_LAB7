#!/usr/bin/python



class TypeChecker(object):

    def dispatch(self, node, *args):
        self.node = node
        className = node.__class__.__name__
        meth = getattr(self, 'visit_' + className)
        return meth(node, *args)


    def visit_BinExpr(self, node):
        type1 = self.dispatch(node.left)
        type2 = self.dispatch(node.right)
        op    = node.op;
        # ... 
        #
 
    def visit_RelExpr(self, node):
        type1 = self.dispatch(node.left)
        type2 = self.dispatch(node.right)
        # ... 
        #

    def visit_Integer(self, node):
        return 'int'

    #def visit_Float(self, node):
    # ... 
    # 

    # ... 
    # 


