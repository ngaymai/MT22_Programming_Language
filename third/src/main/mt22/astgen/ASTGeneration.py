from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(ctx.decls().accept(self))
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        declLst = ctx.decl().accept(self)
        if ctx.getChildCount() == 1:
            return declLst
        else:
            declLst += ctx.decls().accept(self)  
        return declLst
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.varDecl():
            return ctx.varDecl().accept(self)
        else:
            return ctx.funcDecl().accept(self)
        
    def visitVarDecl(self, ctx: MT22Parser.VarDeclContext):
        if ctx.formalDecl():
            return ctx.formalDecl().accept(self)      
        else:
            return ctx.initializationDecl().accept(self)
    
    def visitFormalDecl(self, ctx: MT22Parser.FormalDeclContext):
        lst = ctx.identifierList().accept(self)    
        varType = ctx.varType().accept(self)
        # size = len(lst)
        # res = []
        # for i in range(size):
        #     res += list(VarDecl(lst[i], varType, ""))            
        # return res
        return list(map(lambda x: VarDecl(x, varType), lst))
        
    def visitInitializationDecl(self, ctx: MT22Parser.InitializationDeclContext):        
            id = [ctx.Identifier().getText()]
            value = [ctx.expression().accept(self)]
            lst = id + ctx.term().accept(self) + value
            mid = int(len(lst)/2) 
            varType = lst[mid]

            lst1 = lst[:mid]
            lst2 = lst[mid + 1:]
            lst = list(zip(lst1, lst2))
            # size = len(lst)
            # res = []
            # for i in range(size):
            #     res += list(VarDecl(lst[i][0], varType, lst[i][1]))            
            # return res
            return list(map(lambda x: VarDecl(x[0], varType, x[1]), lst))
            
        
    
    def visitTerm(self, ctx: MT22Parser.TermContext):
        if ctx.getChildCount() == 3:
            return [ctx.varType().accept(self)]
        else:
            id = [ctx.Identifier().getText()]
            value = [ctx.expression().accept(self)]
            lst = id + ctx.term().accept(self) + value
            return lst
    def visitVarType(self, ctx: MT22Parser.VarTypeContext):
        if ctx.atomicType():
            return ctx.atomicType().accept(self)
        elif ctx.AUTO():
            return AutoType()
        else:
            return ctx.arrayType().accept(self)
    def visitArrayType(self, ctx: MT22Parser.ArrayTypeContext):              
        dimen = ctx.dimensions().accept(self)
        eleType = ctx.atomicType().accept(self)
        return ArrayType(dimen, eleType)
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return [int(x.getText()) for x in ctx.IntegerLiteral()]    
            
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.CONCATENATE().getText(), ctx.relationalExpression(0).accept(self), ctx.relationalExpression(1).accept(self))
        else: 
            return ctx.relationalExpression(0).accept(self)        
    def visitRelationalExpression(self, ctx: MT22Parser.RelationalExpressionContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.relationalOperator().accept(self), ctx.logicalExpression(0).accept(self), ctx.logicalExpression(1).accept(self))
        else: 
            return ctx.logicalExpression(0).accept(self) 
    def visitRelationalOperator(self, ctx: MT22Parser.RelationalOperatorContext):
        if ctx.Less():
            return ctx.Less().getText()
        elif ctx.Greater():
            return ctx.Greater().getText()
        elif ctx.LessEqual():
            return ctx.LessEqual().getText()
        elif ctx.GreaterEqual():
            return ctx.GreaterEqual().getText()
        elif ctx.Equal():
            return ctx.Equal().getText()
        else:
            return ctx.NotEqual().getText()

    def visitLogicalExpression(self, ctx: MT22Parser.LogicalExpressionContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.logicalOperator().accept(self), ctx.logicalExpression().accept(self), ctx.additiveExpression().accept(self))
        else: 
            return ctx.additiveExpression().accept(self)     
    def visitLogicalOperator(self, ctx: MT22Parser.LogicalOperatorContext):
        if ctx.And():
            return ctx.And().getText()
        else:
            return ctx.Or().getText()
    

    def visitAdditiveExpression(self, ctx: MT22Parser.AdditiveExpressionContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.additiveOperator().accept(self), ctx.additiveExpression().accept(self), ctx.multiplicativeExpression().accept(self))
        else: 
            return ctx.multiplicativeExpression().accept(self)
    def visitAdditiveOperator(self, ctx: MT22Parser.AdditiveOperatorContext):    
        if ctx.Plus():
            return ctx.Plus().getText()
        else:
            return ctx.Minus().getText()
        

    def visitMultiplicativeExpression(self, ctx: MT22Parser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.multiplicativeOperator().accept(self), ctx.multiplicativeExpression().accept(self), ctx.negationExpression().accept(self))
        else: 
            return ctx.negationExpression().accept(self)
    def visitMultiplicativeOperator(self, ctx: MT22Parser.MultiplicativeOperatorContext):    
        if ctx.Multiple():
            return ctx.Multiple().getText()
        elif ctx.Division():
            return ctx.Division().getText()
        else:
            return ctx.Remain().getText()
        
    def visitNegationExpression(self, ctx: MT22Parser.NegationExpressionContext):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.Negation().getText(), ctx.negationExpression().accept(self))
        else: 
            return ctx.negationSignExpression().accept(self)
    def visitNegationSignExpression(self, ctx: MT22Parser.NegationSignExpressionContext):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.Minus().getText(), ctx.negationSignExpression().accept(self))
        else: 
            return ctx.primaryExpression().accept(self)
    def visitPrimaryExpression(self, ctx: MT22Parser.PrimaryExpressionContext):
        if ctx.Identifier():
            return Id(ctx.Identifier().getText())
        elif ctx.constant():
            return ctx.constant().accept(self)
        elif ctx.arrayElement():
            return ctx.arrayElement().accept(self)
        elif ctx.functionCall():
            return ctx.functionCall().accept(self)
        else:
            return ctx.expression().accept(self)

    def visitConstant(self, ctx: MT22Parser.ConstantContext):
        if ctx.IntegerLiteral():
            return IntegerLit(int(ctx.IntegerLiteral().getText()))
        elif ctx.FloatLiteral():
            x = ctx.FloatLiteral().getText()
            if x[0] == '.':
                x = '0' + x
            return FloatLit(float(x))
        elif ctx.StringLiteral():
            return StringLit(ctx.StringLiteral().getText())
        elif ctx.BooleanLiteral():
            if ctx.BooleanLiteral().getText() == 'false':
                x = False
            else:
                x = True
            return BooleanLit(x)
        else:
            return ctx.arrayLiteral().accept(self)
    def visitArrayElement(self, ctx: MT22Parser.ArrayElementContext):
        if ctx.exprList():
            return ArrayCell(ctx.Identifier().getText(), ctx.exprList().accept(self))
        else:
            return ArrayCell(ctx.Identifier().getText(), [])
    def visitArrayLiteral(self, ctx: MT22Parser.ArrayLiteralContext):
        if ctx.getChildCount() == 3:
            return ArrayLit(ctx.exprList().accept(self))
        else:
            return ArrayLit([])
    # def visitlistIndex(self, ctx: MT22Parser.ListIndexContext):    
    #     if ctx.exprList():
    #         return [ctx.exprList().accept(self)]
    #     else:
    #         return []
    def visitExprList(self, ctx: MT22Parser.ExprListContext):
        return [x.accept(self) for x in ctx.expression()]
    
    
    
    def visitFunctionCall(self, ctx: MT22Parser.FunctionCallContext):
        lst = ctx.callStatement().accept(self)
        if len(lst) == 1:
            return FuncCall(lst[0],[])
        else:
            return FuncCall(lst[0],lst[1:])

    def visitIdentifierList(self, ctx: MT22Parser.IdentifierListContext):
        
        if ctx.getChildCount() ==  1:        
            return [ctx.Identifier(0).getText()]
            
        else:             
            return [x.getText() for x in ctx.Identifier()]
        
    def visitAtomicType(self, ctx: MT22Parser.AtomicTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.STRING():
            return StringType()

    def visitFuncDecl(self, ctx: MT22Parser.FuncDeclContext):
        
        lst1 = ctx.functionPrototype().accept(self)  
        lst2 = ctx.functionBody().accept(self)                         
        return [FuncDecl(lst1[0],lst1[1],lst1[2],lst1[3],lst2)]
        
    #   ---------------------------------------
    def visitFunctionPrototype(self, ctx: MT22Parser.FunctionPrototypeContext):
        id = ctx.Identifier().getText()
        funcType = ctx.dataType().accept(self)
        lst = ctx.listPara().accept(self)
        if ctx.inherSubpart():
            inher = ctx.inherSubpart().accept(self)
        else:
            inher = None
        return list((id, funcType, lst, inher))
    def visitListPara(self, ctx: MT22Parser.ListParaContext):
        if ctx.getChildCount() == 3:
            return ctx.paradeclList().accept(self)
        else:
            return []
    def visitParadeclList(self, ctx: MT22Parser.ParadeclListContext):
        return [x.accept(self) for x in ctx.argument()]
    def visitArgument(self, ctx: MT22Parser.ArgumentContext):
        if ctx.varDecl():
            return ctx.varDecl().accept(self)
        else: 
            return ctx.paramDecl().accept(self)
    def visitParamDecl(self, ctx: MT22Parser.ParamDeclContext):
        id = ctx.Identifier().getText()
        varType = ctx.varType().accept(self)
        if ctx.INHERIT():
            if ctx.OUT():
                return ParamDecl(id, varType, True, True)
            else:
                return ParamDecl(id, varType, False, True)
        elif ctx.OUT():
            return ParamDecl(id, varType, True, False)
        else: 
            return ParamDecl(id, varType, False, False)
    def visitInherSubpart(self, ctx: MT22Parser.InherSubpartContext):
        return ctx.Identifier().getText()
    def visitDataType(self, ctx: MT22Parser.DataTypeContext):
        if ctx.atomicType():
            return ctx.atomicType().accept(self)
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return ctx.arrayType().accept(self)
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.others():
            return ctx.others().accept(self)
        else: 
            return ctx.selectionStatement().accept(self)
    def visitSelectionStatement(self, ctx: MT22Parser.SelectionStatementContext):
        if ctx.matchStatement():
            return ctx.matchStatement().accept(self)
        else: 
            return ctx.unmatchStatement().accept(self)
    def visitMatchStatement(self, ctx: MT22Parser.MatchStatementContext):
        if ctx.others():
            return ctx.others().accept(self)
        else: 
            return IfStmt(ctx.expression().accept(self), ctx.matchStatement(0).accept(self), ctx.matchStatement(1).accept(self))
    def visitUnmatchStatement(self, ctx: MT22Parser.UnmatchStatementContext):
        if ctx.getChildCount() == 5:
            return IfStmt(ctx.expression().accept(self), ctx.statement().accept(self))
        else:
            return IfStmt(ctx.expression().accept(self), ctx.matchStatement().accept(self), ctx.unmatchStatement().accept(self))
    def visitOthers(self, ctx :MT22Parser.OthersContext):
        if ctx.iterationStatement():
            return ctx.iterationStatement().accept(self)
        elif ctx.assignmentStatement():
            return ctx.assignmentStatement().accept(self)
        elif ctx.blockStatement():
            return ctx.blockStatement().accept(self)
        elif ctx.callStatement():
             lst = ctx.callStatement().accept(self)
             if len(lst) == 1:
                 return CallStmt(lst[0], [])
             else:
                 return CallStmt(lst[0], lst[1:])
        else:
            return ctx.jumpStatement().accept(self)
    def visitAssignmentStatement(self, ctx: MT22Parser.AssignmentStatementContext):
        return AssignStmt(ctx.lhs().accept(self), ctx.expression().accept(self))
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.Identifier():
            return Id(ctx.Identifier().getText())
        else:
            return ctx.arrayElement().accept(self)
    def visitIterationStatement(self, ctx: MT22Parser.IterationStatementContext):        
        if ctx.DO():
            return DoWhileStmt(ctx.expression().accept(self), ctx.blockStatement().accept(self))
        elif ctx.FOR():
            lst = ctx.forCondition().accept(self)
            return ForStmt(lst[0], lst[1], lst[2], ctx.statement().accept(self))
        else: 
            return WhileStmt(ctx.expression().accept(self), ctx.statement().accept(self))
    def visitForCondition(self, ctx: MT22Parser.ForConditionContext):
        return list((ctx.assignmentStatement().accept(self), ctx.expression(0).accept(self), ctx.expression(1).accept(self)))
    def visitBlockStatement(self, ctx: MT22Parser.BlockStatementContext):
        if ctx.content():
            lst = []
            size = len(ctx.content())
            for i in range(size):
                item = ctx.content(i).accept(self)
                if isinstance(item, list):
                    lst += item
                else:
                    lst += [item]
            
            return BlockStmt(lst)
        else:
            return BlockStmt([])
    def visitContent(self, ctx: MT22Parser.ContentContext):
        if ctx.statement():
            return ctx.statement().accept(self)
        else:
            return ctx.varDecl().accept(self)
    def visitCallStatement(self, ctx: MT22Parser.CallStatementContext):
        if ctx.exprList():
            return [ctx.Identifier().getText()] + ctx.exprList().accept(self)
        else: 
            return [ctx.Identifier().getText()]
        
    def visitJumpStatement(self, ctx: MT22Parser.JumpStatementContext):
        if ctx.RETURN():
            if ctx.expression():
                return ReturnStmt(ctx.expression().accept(self))
            else:
                return ReturnStmt()
        elif ctx.BREAK():
            return BreakStmt()
        else:
            return ContinueStmt()
        

    
    
        
        
            
