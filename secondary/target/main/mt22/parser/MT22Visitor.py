# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDecl.
    def visitFuncDecl(self, ctx:MT22Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDecl.
    def visitVarDecl(self, ctx:MT22Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#formalDecl.
    def visitFormalDecl(self, ctx:MT22Parser.FormalDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initializationDecl.
    def visitInitializationDecl(self, ctx:MT22Parser.InitializationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term.
    def visitTerm(self, ctx:MT22Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varType.
    def visitVarType(self, ctx:MT22Parser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierList.
    def visitIdentifierList(self, ctx:MT22Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionPrototype.
    def visitFunctionPrototype(self, ctx:MT22Parser.FunctionPrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramDecl.
    def visitParamDecl(self, ctx:MT22Parser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listPara.
    def visitListPara(self, ctx:MT22Parser.ListParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradeclList.
    def visitParadeclList(self, ctx:MT22Parser.ParadeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument.
    def visitArgument(self, ctx:MT22Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherSubpart.
    def visitInherSubpart(self, ctx:MT22Parser.InherSubpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionBody.
    def visitFunctionBody(self, ctx:MT22Parser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dataType.
    def visitDataType(self, ctx:MT22Parser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprList.
    def visitExprList(self, ctx:MT22Parser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:MT22Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalOperator.
    def visitRelationalOperator(self, ctx:MT22Parser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpression.
    def visitLogicalExpression(self, ctx:MT22Parser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalOperator.
    def visitLogicalOperator(self, ctx:MT22Parser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MT22Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#additiveOperator.
    def visitAdditiveOperator(self, ctx:MT22Parser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MT22Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:MT22Parser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#negationExpression.
    def visitNegationExpression(self, ctx:MT22Parser.NegationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#negationSignExpression.
    def visitNegationSignExpression(self, ctx:MT22Parser.NegationSignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MT22Parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayElement.
    def visitArrayElement(self, ctx:MT22Parser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionCall.
    def visitFunctionCall(self, ctx:MT22Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#constant.
    def visitConstant(self, ctx:MT22Parser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#others.
    def visitOthers(self, ctx:MT22Parser.OthersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MT22Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#selectionStatement.
    def visitSelectionStatement(self, ctx:MT22Parser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#matchStatement.
    def visitMatchStatement(self, ctx:MT22Parser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unmatchStatement.
    def visitUnmatchStatement(self, ctx:MT22Parser.UnmatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#iterationStatement.
    def visitIterationStatement(self, ctx:MT22Parser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forCondition.
    def visitForCondition(self, ctx:MT22Parser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#content.
    def visitContent(self, ctx:MT22Parser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#jumpStatement.
    def visitJumpStatement(self, ctx:MT22Parser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MT22Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)



del MT22Parser