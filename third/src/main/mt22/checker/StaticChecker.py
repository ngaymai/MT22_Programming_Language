
from Visitor import Visitor
from AST import *
from main.mt22.checker.StaticError import *
from main.mt22.utils.AST import *
# from StaticError import *
# from Utils import Utils
# from Visitor import *
# from AST import *

class Node:
    def __init__(self, name, kind, typ, scope,  value = None, inher = None, out = None):
        self.name = name
        self.scope = scope
        self.typ = typ        
        self.kind = kind   
        self.value = value     
        self.inher = inher
        self.out = out        
        self.next = None
    def __str__(self):
        return f"|| name: {self.name} | kind: {self.kind} | type: {self.typ} | scope: {self.scope} | inher: {self.inher} | out: {self.out} ||"
        
class Table:
    def __init__(self, name:str, typ = None, body = None, inher = None, args = []):
        self.name = name
        self.typ = typ                 
        self.body = body
        self.args = args
        self.inher = inher 
        self.head = None
        self.next = None
    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            term = self.head
            while term.next is not None:
                term = term.next
            term.next = newNode
    def deleteNode(self, delNode):
        term = self.head
        if self.head is not None:
            if self.head is delNode:
                self.head = term.next
                term = None
            else:
                while term is not None:
                    if term is delNode:
                        break
                    pre = term
                    term = term.next
                pre.next = term.next
                term = None
            
        term = self.head
        while term.next is not delNode:
            term = term.next
            term.next = delNode.next
            delNode.next = Node
 
    def searchVar(self, name, scope):
        res = None
        if self.head is not None:
            ptr = self.head
            max = 0
            
            while ptr is not None:            
                if ptr.name == name and ptr.scope <= scope:
                    if ptr.scope >= max:
                        max = ptr.scope
                        res = ptr
                ptr = ptr.next
        return res
    def checkArgs(self, args, ctx, len, s):
        ptr = self.head
        while ptr is not None and len != 0:
            if isinstance(ptr.kind, Parameter):
                if args:                    
                    if isinstance(ptr.typ, type(args[0])):
                        if isinstance(ptr.typ, ArrayType):
                            if ptr.typ.dimensions == args[0].dimensions and isinstance(ptr.typ.typ, type(args[0])):
                                args = args[1:]
                            else:
                                if s == 1:                         
                                    raise TypeMismatchInExpression(ctx)
                                else:
                                    raise TypeMismatchInStatement(ctx)
                        else: 
                            args = args[1:]
                    elif isinstance(ptr.typ, FloatType) and isinstance(args[0], IntegerType):
                        args = args[1:]
                    elif isinstance(ptr.typ, AutoType):
                        if isinstance(args[0], Table):
                            pass                 
                        elif isinstance(args[0], Node):
                            pass 
                        else:   
                            ptr.typ = args[0]
                            args = args[1:]
                    elif isinstance(args[0], Table):
                        
                        if isinstance(ptr.typ, AutoType):
                            pass 
                        else:
                            args[0].typ = ptr.typ
                            args = args[1:]
                    elif isinstance(args[0], Node):
                        if isinstance(ptr.typ, AutoType):
                            pass 
                        else:
                            args[0].typ = ptr.typ
                            args = args[1:]
                    else:                 
                        if s == 1:                         
                            raise TypeMismatchInExpression(ctx)
                        else:
                            raise TypeMismatchInStatement(ctx)
                else:
                    if s == 1:                         
                        raise TypeMismatchInExpression(ctx)
                    else:
                        raise TypeMismatchInStatement(ctx)

            ptr = ptr.next
            len = len - 1
                    

    def __str__(self):
        res = f"|| name: {self.name} | type: {self.typ} | inher: {self.inher} | args: {self.args} ||"
        term = self.head
        while term is not None:
           res += "\n" + str(term)
           term = term.next
        return res
       
    
class SymbolTable:
    def __init__(self):
        self.head = None
        
    def insertTable(self, newTable):
        if self.head is None:
            self.head = newTable
        else:
            term = self.head
            while term.next is not None:
                term = term.next
            term.next = newTable
    def deleteTable(self, delTable):
        term = self.head
        if self.head is not None:
            if self.head is delTable:
                self.head = term.next
                term = None
            else:
                while term is not None:
                    if term is delTable:
                        break
                    pre = term
                    term = term.next
                pre.next = term.next
                term = None
            
        term = self.head
        while term.next is not delTable:
            term = term.next
            term.next = delTable.next
            delTable.next = Node
    def searchTable(self, name):        
        if self.head is not None:
            ptr = self.head
            while ptr is not None:
                if ptr.name == name:                    
                    return ptr
                else:
                    ptr = ptr.next
        return None

    def isRedecl(self, Tname, name, scope):

        if Tname == 'global':
            ptr = self.head
            term = ptr.head
            while term is not None:
                if term.name == name:
                    return True
                term = term.next

            while ptr is not None:
                if ptr.name == name:
                    return True 
                ptr = ptr.next 
            
            return False   
        else: 
            ptr = self.searchTable(Tname)
            if ptr is not None:
                term = ptr.head
                while term is not None:
                    if term.name == name and term.scope == scope:
                        return True
                    term = term.next
            return False

        
    def searchElement(self, tabName, varName, scope):
        table = self.searchTable(tabName)        
        res = table.searchVar(varName, scope)
        if res is None:
            table = self.searchTable('global')            
            res = table.searchVar(varName, 0)
        return res
    def specialFunc(self): # name:str, typ = None, body = None, inher = None, args = []
        self.insertTable(Table('readInteger', IntegerType(), None, None, []))
        self.insertTable(Table('printInteger', VoidType(), None, None, [IntegerType()]))
        self.insertTable(Table('readFloat', FloatType(), None, None, []))
        self.insertTable(Table('writeFloat', VoidType(), None, None, [FloatType()]))
        self.insertTable(Table('readBoolean', BooleanType(), None, None, []))
        self.insertTable(Table('printBoolean', VoidType(), None, None, [BooleanType()]))
        self.insertTable(Table('readString', StringType(), None, None, []))
        self.insertTable(Table('printString', VoidType(), None, None, [StringType()]))
        self.insertTable(Table('super', VoidType(), None, None, []))
        self.insertTable(Table('preventDefault', VoidType(), None, None, []))
    def inher(self, parent, child):
        ptr = parent.head
        
        while ptr is not None:
            if ptr.inher:  
                if self.isRedecl(child.name, ptr.name, ptr.scope):
                    raise Invalid(Parameter, ptr.name)              
                child.insertNode(Node(ptr.name, ptr.kind, ptr.typ, ptr.scope, None, False, ptr.out))                
            ptr = ptr.next
    # =================================================
    def test(self):
        ptr = self.head
        while(ptr is not None):
            
            ptr = ptr.next
    # =====================================================
    def __str__(self):
        res = str(self.head)
        term = self.head.next
        while term is not None:
           res += "\n" + str(term)
           term = term.next
        return res
class StaticChecker(Visitor):
    st = SymbolTable()
    def __init__(self, ctx):
        self.ctx = ctx
    
    def check(self):
        self.st = SymbolTable()
        lst = {}
        lst['current'] = None
        lst['scope'] = None        
        return self.visit(self.ctx, lst)
    def visitProgram(self, ctx: Program, lst):        
        lst['current'] = 'global'
        lst['scope'] = 0
        lst['ins'] = []
        lst['inherit'] = None
        lst['decl'] = []
        lst['array'] = None
        t = Table('global')
        self.st.insertTable(t)        
        for decl in ctx.decls:  
            self.visit(decl, lst)          
        self.st.specialFunc()        
        ptr = self.st.head  
        for var in lst['decl']:        
            if self.st.isRedecl(lst['current'], var.name, lst['scope']):                       
                raise Redeclared(Variable(), var.name)
            else:
                t = self.st.searchTable(lst['current']) 
                typ = self.visit(var.typ, lst)
                if type(typ) is type(VoidType()):
                    raise Invalid(Variable(), var.name)
                if var.init is None:                
                    # name, kind, typ, dimen, scope, inher                                  
                    if type(typ) is type(AutoType()):
                        # Invalid(Variable(), <variable-name>)
                        raise Invalid(Variable(), var.name)              
                    else:
                        #t.insertNode(Node(ctx.name, Variable(), typ, dimen, scope))   
                        t.insertNode(Node(var.name, Variable(), typ, lst['scope'])) 
                else: 
                    v = Node(var.name, Variable(), typ, lst['scope'])
                    t.insertNode(v) 
                    init = self.visit(var.init, lst)  
                    if type(typ) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]:
                        if type(init) in [IntegerType, FloatType, BooleanType, StringType] and isinstance(typ, type(init)):                            
                           # v.typ = typ
                           pass
                        elif isinstance(typ, FloatType) and isinstance(init, IntegerType):
                            pass
                        elif isinstance(init, Node): # auto type
                            init.typ = typ  
                        elif isinstance(init, Table): # auto func
                            init.typ = typ
                        elif isinstance(typ, type(init)) and isinstance(typ, ArrayType):
                            if typ.dimensions == init.dimensions and isinstance(typ.typ, type(init.typ)):                     
                                pass                     
                            else:
                                raise TypeMismatchInVarDecl(var)     
                        else:
                            raise TypeMismatchInVarDecl(var) #cxt.init
                    elif isinstance(typ, AutoType): # type, arraylit 
                        if type(init) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]:
                            #t.insertNode(Node(var.name, Variable(), init, lst['scope']))  
                            v.typ = init   
                             
                        else:
                            raise TypeMismatchInVarDecl(var)
                    else:
                        raise TypeMismatchInVarDecl(var)
                

        while ptr is not None:            
            if ptr.name != 'global':
                lst['current'] = ptr.name 
                                
                if ptr.body is not None: 
                                            
                    self.visit(ptr.body, lst)
            ptr = ptr.next
        if self.st.searchTable('main') and isinstance(self.st.searchTable('main').typ, VoidType) :
            pass
        else:
            raise NoEntryPoint()
        return []
    def visitVarDecl(self, ctx: VarDecl, lst):  
        current = lst['current']             
        scope = lst['scope']

        if current == 'global':
            lst['decl'] += [ctx]
            return        
        if self.st.isRedecl(current, ctx.name, scope):                       
            raise Redeclared(Variable(), ctx.name)
        else:
            t = self.st.searchTable(current) 
            #typ, dimen = self.visit(ctx.typ, lst)
            typ = self.visit(ctx.typ, lst)
            if type(typ) is type(VoidType()):
                raise Invalid(Variable(), ctx.name)
            if ctx.init is None:                
                # name, kind, typ, dimen, scope, inher                
                if type(typ) is type(AutoType()):
                    # Invalid(Variable(), <variable-name>)
                    raise Invalid(Variable(), ctx.name)              
                else:
                    #t.insertNode(Node(ctx.name, Variable(), typ, dimen, scope))   
                    t.insertNode(Node(ctx.name, Variable(), typ, scope)) 
            else: 
                v = Node(ctx.name, Variable(), typ, scope)
                t.insertNode(v)
                init = self.visit(ctx.init, lst)  
                
                if type(typ) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]:
                    if type(init) in [IntegerType, FloatType, BooleanType, StringType] and isinstance(typ, type(init)):
                        # t.insertNode(Node(ctx.name, Variable(), typ, scope))
                        pass
                    elif isinstance(typ, FloatType) and isinstance(init, IntegerType):
                        # t.insertNode(Node(ctx.name, Variable(), typ, scope))     
                        pass
                    elif isinstance(init, Node): # auto func
                        init.typ = typ         
                        # t.insertNode(Node(ctx.name, Variable(), typ, scope)) 
                    elif isinstance(init, Table):
                        init.typ = typ
                            # t.insertNode(Node(ctx.name, Variable(), typ, scope)) 
                    elif isinstance(typ, type(init)) and isinstance(typ, ArrayType):
                        if typ.dimensions == init.dimensions and isinstance(typ.typ, type(init.typ)):
                                # t.insertNode(Node(ctx.name, Variable(), typ, scope))   
                                pass                          
                        else:
                            raise TypeMismatchInVarDecl(ctx)      
                    else:
                        raise TypeMismatchInExpression(ctx) #cxt.init
                elif isinstance(typ, AutoType): # type, arraylit 
                    if type(init) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]:
                        v.typ = init
                        # t.insertNode(Node(ctx.name, Variable(), init, scope))     
                    else:
                        raise TypeMismatchInVarDecl(ctx)                

                else:
                    raise TypeMismatchInVarDecl(ctx)
                
    def visitFuncDecl(self, ctx: FuncDecl, lst):
        current = lst['current']
        scope = lst['scope']
        if current == 'global':
            if self.st.isRedecl(current, ctx.name, scope):
                raise Redeclared(Function(), ctx.name)
            else:
                # name, kind, typ, dimen, scope, inher                  
                typ = self.visit(ctx.return_type, lst)
                newT = Table(ctx.name, typ, ctx.body, ctx.inherit)                                            
                self.st.insertTable(newT)
                lst['current'] = ctx.name
                args = []
                for param in ctx.params:
                    args += [self.visit(param, lst)]
                newT.args = args                
        lst['current'] = 'global'        
    
    def visitParamDecl(self, ctx: ParamDecl, lst):
        current = lst['current']
        scope = lst['scope'] + 1
        
        if self.st.isRedecl(current, ctx.name, scope):
            raise Redeclared(Parameter(), ctx.name)
        else:
            t = self.st.searchTable(current)
            # typ, dimen = self.visit(ctx.typ, lst)        
            typ = self.visit(ctx.typ, lst)          
            
            if isinstance(typ, VoidType):
                raise Invalid(Parameter(), ctx.Name)            
            else:                              
                t.insertNode(Node(ctx.name, Parameter(), typ, scope, None, ctx.inherit, ctx.out))
             
            return typ

    def visitBlockStmt(self, ctx: BlockStmt, lst):
        current = lst['current']        
        scope = lst['scope']        
        lst['inherit'] = None
        lst['scope'] = scope + 1 
        if lst['scope'] == 1:    
            table = self.st.searchTable(current)   
      
            if table.inher is not None:                   
                parent = self.st.searchTable(table.inher)
                #print(parent)
                lst['inherit'] = parent
                #self.st.inher(parent, table)
    
        for ins in ctx.body:
            
            self.visit(ins, lst)
            
            if lst['inherit'] is not None:                
                raise InvalidStatementInFunction(current) 
        lst['scope'] = scope
    
    def visitAssignStmt(self, ctx: AssignStmt, lst):
        lhs = self.visit(ctx.lhs, lst)   # atomic type
        rhs = self.visit(ctx.rhs, lst)   # funcCall, id, exprs, literal   

        res = None 
        if isinstance(lhs, Node):
            if type(rhs) in [IntegerType, FloatType, BooleanType, StringType]:
                lhs.typ = rhs
                res = rhs
            elif isinstance(rhs, ArrayType):
                lhs.typ.typ = rhs.typ
                res = rhs.typ
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            if isinstance(rhs, Table) and isinstance(rhs.typ, AutoType):
                rhs.typ = lhs
                res = lhs
            elif isinstance(rhs, Node):
                rhs.typ = lhs
                res = lhs
            elif type(lhs) in [IntegerType, FloatType, BooleanType, StringType] and isinstance(lhs, type(rhs)):
                
                res = lhs

            elif isinstance(lhs, FloatType) and isinstance(rhs, IntegerType):
                res = lhs
                
            else:
                raise TypeMismatchInStatement(ctx)
                
            return res
    def visitIfStmt(self, ctx: IfStmt, lst):          
        lst['ins'] += ['IfStmt']          
        cond = self.visit(ctx.cond, lst)    
           
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.tstmt, lst)
        if ctx.fstmt:   
            self.visit(ctx.fstmt, lst)
        lst['ins'] = lst['ins'][:-1]
        
    def visitForStmt(self, ctx: ForStmt, lst):           
        lst['ins'] += ['ForStmt']        
        init = self.visit(ctx.init, lst)
        if not isinstance(init, IntegerType):
            raise TypeMismatchInStatement(ctx)
        cond = self.visit(ctx.cond, lst)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ctx)
        upd = self.visit(ctx.upd, lst)
        if not isinstance(upd, IntegerType):
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.stmt, lst)
        lst['ins'] = lst['ins'][:-1]
        

    def visitWhileStmt(self, ctx: WhileStmt, lst):
        lst['ins'] += ['WhileStmt']
        cond = self.visit(ctx.cond, lst)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.stmt, lst)
        lst['ins'] = lst['ins'][:-1]
    def visitDoWhileStmt(self, ctx: DoWhileStmt, lst):
        lst['ins'] += ['DoWhileStmt']
        cond = self.visit(ctx.cond, lst)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.stmt, lst)
        lst['ins'] = lst['ins'][:-1]
    def visitBreakStmt(self, ctx: BreakStmt, lst):
        for each in lst['ins']:
            if each in ['ForStmt', 'WhileStmt', 'DoWhileStmt']:
                return 
        raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx: ContinueStmt, lst):
        for each in lst['ins']:
            if each in ['ForStmt', 'WhileStmt', 'DoWhileStmt']:
                return 
        raise MustInLoop(ctx)
    
    def visitReturnStmt(self, ctx: ReturnStmt, lst):
        current = lst['current']
        table = self.st.searchTable(current)
 #
        if ctx.expr:            # type, table, node 
            res = self.visit(ctx.expr, lst)
            if isinstance(table.typ, VoidType):
                raise TypeMismatchInStatement(ctx)
            elif isinstance(table.typ, AutoType):
                if type(res) in [IntegerType, float, BooleanType, StringType, ArrayType]:
                    table.typ = res 
                else:
                    raise TypeMismatchInStatement(ctx)
     
            elif isinstance(table.typ, ArrayType):
                if isinstance(res, ArrayType):
                    if res.typ.dimensions == table.typ.dimensions and isinstance(res.typ.dimensions, type(table.typ.dimensions)):
                        pass
                    elif res.typ.dimensions == table.typ.dimensions and isinstance(res.typ.dimensions, IntegerType) and isinstance(table.typ.typ, FloatType):
                        pass
                    else:
                        raise TypeMismatchInStatement(ctx)
                elif isinstance(res, Node):
                    res.typ = table.typ
                    
                elif isinstance(res, Table) and isinstance(res.typ, AutoType):
                    res.typ = table.typ
                    
                else:
                    raise TypeMismatchInStatement(ctx)                    
            else:
                if isinstance(table.typ, type(res)):
                    pass 
                elif isinstance(table.typ, FloatType) and isinstance(res, IntegerType):
                    pass 
            # node, list
                elif isinstance(res, Node): # auto
                    res.typ = table.typ
                elif isinstance(res, Table) and isinstance(res.typ, AutoType):
                    res.typ = table.typ
                else:
                    raise TypeMismatchInStatement(ctx)
        else: 
            if isinstance(table.typ, AutoType):
                table.typ = VoidType()     
            elif isinstance(table.typ, VoidType):
                pass       
            else:
                raise InvalidStatementInFunction(table.name)
                



            
        
    def visitCallStmt(self, ctx: CallStmt, lst):
        current = lst['current']        
        inher = lst['inherit']
        table = self.st.searchTable(ctx.name)
        args = []
      
        for arg in ctx.args:
            args += [self.visit(arg, lst)]        
        if inher is None:
            if table is None:  
                raise Undeclared(Function(), ctx.name)     
            else:
                if table.name == 'main':
                    raise TypeMismatchInStatement(ctx)   
                elif table.name == 'preventDefault':                
                    raise InvalidStatementInFunction(current)
                elif table.name == 'super':                
                    raise InvalidStatementInFunction(current)
                elif len(table.args) != len(ctx.args):                    
                    raise TypeMismatchInStatement(ctx)
                #elif isinstance(table.typ, AutoType):                    
                table.checkArgs(args, ctx, len(ctx.args), 2)
                
        else:
            if table.name == 'preventDefault':                
                lst['inherit'] = None
            elif table.name == 'super':                
                if len(inher.args) == len(ctx.args):
                    inher.checkArgs(args, ctx, len(ctx.args), 2)
                    child = self.st.searchTable(current)
                    self.st.inher(inher, child)
                    lst['inherit'] = None
                else:
                    raise TypeMismatchInStatement(ctx)
            else:
                raise InvalidStatementInFunction(current)
                        
            
            
            

# literal, id, arraycell, function
    def visitBinExpr(self, ctx: BinExpr, lst):
        left = self.visit(ctx.left, lst)
        right = self.visit(ctx.right, lst)
      
        op = ctx.op
        if op in ['+', '-', '*', '/']:
            #======================================================================
           
            if isinstance(left, Table) and isinstance(right, Table):
                raise TypeMismatchInExpression(ctx)
            elif isinstance(left, Table) and isinstance(left.typ, AutoType):
               
                if type(right) in [IntegerType, FloatType]:
                    left.typ = right
                    return right                   
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
             
                if  type(left) in [IntegerType, FloatType]:
                    right.typ = left
                    return left                
                else:
                    raise TypeMismatchInExpression(ctx)           
            elif isinstance(left, FloatType) and isinstance(right, FloatType):
                return FloatType()
            elif isinstance(left, IntegerType) and isinstance(right, IntegerType):
                return IntegerType()
            elif type(left) in [FloatType, IntegerType] and type(right) in [FloatType, IntegerType]:
                return FloatType()                    
            else:
                raise TypeMismatchInExpression(ctx)
        elif op == '%':
            if isinstance(left, Table) and isinstance(right, Table): # auto , array, void
                if isinstance(left.typ, AutoType) and isinstance(right.typ, AutoType):
                    left.typ = IntegerType()
                    right.typ = IntegerType()
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(left, Table) and isinstance(left.typ, AutoType):
                if isinstance(right, IntegerType):
                    left.typ = right
                    return right
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
                if isinstance(left, IntegerType):
                    right.typ = left
                    return left
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(left, IntegerType) and isinstance(right, IntegerType):
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif op == '::':
            if isinstance(left, Table) and isinstance(right, Table): # auto , array, void
                if isinstance(left.typ, AutoType) and isinstance(right.typ, AutoType):
                    left.typ = StringType()
                    right.typ = StringType()
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(left, Table) and isinstance(left.typ, AutoType):
                if isinstance(right, StringType):
                    left.typ = right
                    return right                  
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
                if isinstance(left, StringType):
                    right.typ = left
                    return left
                else:
                    raise TypeMismatchInExpression(ctx)
            
            elif isinstance(left, StringType) and isinstance(right, StringType):
                return StringType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['&&', '||']:
            if isinstance(left, Table) and isinstance(right, Table): # auto , array, void
                if isinstance(left.typ, AutoType) and isinstance(right.typ, AutoType):
                    left.typ = BooleanType()
                    right.typ = BooleanType()
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(left, Table) and isinstance(left.typ, AutoType):
                if isinstance(right, BooleanType):
                    left.typ = right
                    return right
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
                if isinstance(left, BooleanType):
                    right.typ = left
                    return left
                else:
                    raise TypeMismatchInExpression(ctx)
            
            elif isinstance(left, BooleanType) and isinstance(right, BooleanType):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['==', '!=']:
            
            if isinstance(left, Table) and isinstance(left.typ, AutoType):
                if type(right) in [IntegerType, BooleanType]:
                    left.typ = right
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
                if type(left) in [IntegerType, BooleanType]:
                    right.typ = left
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ctx)
            
            elif type(left) in [IntegerType, BooleanType] and type(right) in [IntegerType, BooleanType]:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        if op in ['<', '>', '<=', '>=']:
             
            if isinstance(left, Table) and isinstance(left.typ, AutoType):
                if type(right) in [IntegerType, FloatType]:
                    left.typ = right
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ctx)
            elif isinstance(right, Table) and isinstance(right.typ, AutoType):
                if type(left) in [IntegerType, FloatType]:
                    right.typ = left
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ctx)             
            elif type(left) in [FloatType, IntegerType] and type(right) in [FloatType, IntegerType]:
                return BooleanType()                   
            else:
                raise TypeMismatchInExpression(ctx)
                
    # literal, id, arraycell, function
    def visitUnExpr(self, ctx: UnExpr, lst):
        op = ctx.op
        val = self.visit(ctx.val, lst)
        if op == '-':
            if type(val) in [IntegerType, FloatType]:
                return val                
            else:
                raise TypeMismatchInExpression(ctx)
        if op == '!':
            if isinstance(val, Table) and isinstance(val.typ, AutoType):
                val.typ = BooleanType()
                return BooleanType()
            elif isinstance(val, BooleanType):
                return BooleanType()                        
            else:
                raise TypeMismatchInExpression(ctx)
            
    def visitFuncCall(self, ctx: FuncCall, lst):
        table = self.st.searchTable(ctx.name)
        args = []
        
        for arg in ctx.args:            
            args += [self.visit(arg, lst)]
        
        if table is None:                 
            raise Undeclared(Function(), ctx.name)   
        else:         
            if table.name == 'main':
                raise TypeMismatchInExpression(ctx)
            elif table.name == 'global':
                raise TypeMismatchInExpression(ctx)
            elif len(table.args) != len(ctx.args):                               
                raise TypeMismatchInExpression(ctx)
            elif type(table.typ) in [IntegerType, FloatType, BooleanType, StringType, ArrayType]:
                table.checkArgs(args, ctx, len(args), 1)                
                return table.typ        
            else:
                table.checkArgs(args, ctx, len(args), 1)
                return table # auto void
            
        
        
            



    def visitIntegerType(self,ctx:IntegerType,o):
        #return IntegerType(), 0
        return IntegerType()

    def visitFloatType(self,ctx:FloatType,o):
        #return FloatType(), 0
        return FloatType()

    def visitBooleanType(self,ctx:BooleanType,o):
        #return BooleanType(), 0
        return BooleanType()
    def visitStringType(self, ctx:StringType, lst):
        #return StringType(), 0
        return StringType()

    def visitAutoType(self, ctx: AutoType, lst):
        #return AutoType(), 0
        return AutoType()
    def visitVoidType(self, ctx: VoidType, lst):
        #return VoidType(), 0
        return VoidType()
    def visitArrayType(self, ctx: ArrayType, lst):
        dimen = ctx.dimensions
        typ = self.visit(ctx.typ, lst)   
        #dimen.append(typ)     
        return ArrayType(dimen, typ) 

    def visitIntegerLit(self,ctx:IntegerLit, lst): 
        return IntegerType()

    def visitFloatLit(self, ctx: FloatLit, lst): 
        return FloatType()

    def visitBooleanLit(self, ctx: BooleanLit, lst): 
        return BooleanType()
    
    def visitStringLit(self, ctx: StringLit, lst):
        return StringType()
    
    def visitArrayLit(self, ctx: ArrayLit, lst):
        typ = None
        size = 0     
        if lst['array'] is None:
            lst['array'] = ctx   
        for ele in ctx.explist:
            newtyp = self.visit(ele, lst)
            if typ is None:
                typ = newtyp    
            elif not isinstance(typ, type(newtyp)):
                if lst['array'] is None:
                    raise IllegalArrayLiteral(ctx)
                else:
                    raise IllegalArrayLiteral(lst['array'])
            elif isinstance(newtyp, ArrayType) and (not isinstance(typ.typ, type(newtyp.typ)) or typ.dimensions != newtyp.dimensions):
                if lst['array'] is None:
                    raise IllegalArrayLiteral(ctx)
                else:
                    raise IllegalArrayLiteral(lst['array'])
            size += 1
        if isinstance(typ, ArrayType):
            size = [size] + typ.dimensions 
            typ = typ.typ
        else:
            size = [size]
        lst['array'] = None
        return ArrayType(size, typ) 
    

    def visitArrayCell(self, ctx: ArrayCell, lst):
        current = lst['current']
        scope = lst['scope']
        node = self.st.searchElement(current, ctx.name, scope)
        #print(node)
        if node is not None:
            #print('heello')
            if isinstance(node.typ, ArrayType):     
                for index in ctx.cell:
                    if not isinstance(self.visit(index, lst), IntegerType):
                        raise TypeMismatchInExpression(ctx)
                if len(ctx.cell) == len(node.typ.dimensions):
                    return node.typ.typ
                elif len(ctx.cell) < len(node.typ.dimensions):                
                    return ArrayType(node.typ.dimensions[len(ctx.cell) : len(node.typ.dimensions)], node.typ.typ)
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise Undeclared(Identifier(), ctx.name)
        raise Undeclared(Identifier(), ctx.name)   

    def visitId(self, ctx: Id, lst):
        current = lst['current']
        scope = lst['scope'] 
      
        node = self.st.searchElement(current, ctx.name, scope)


        if node is None:
            raise Undeclared(Identifier(), ctx.name)      
        elif isinstance(node.typ, AutoType):            
            return node 
        else:            
            return node.typ



