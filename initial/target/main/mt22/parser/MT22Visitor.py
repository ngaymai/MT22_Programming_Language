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


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function.
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDecl.
    def visitVarDecl(self, ctx:MT22Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#temp1.
    def visitTemp1(self, ctx:MT22Parser.Temp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#temp2.
    def visitTemp2(self, ctx:MT22Parser.Temp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#temp3.
    def visitTemp3(self, ctx:MT22Parser.Temp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#temp4.
    def visitTemp4(self, ctx:MT22Parser.Temp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#temp5.
    def visitTemp5(self, ctx:MT22Parser.Temp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionPrototype.
    def visitFunctionPrototype(self, ctx:MT22Parser.FunctionPrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listIndex.
    def visitListIndex(self, ctx:MT22Parser.ListIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierList.
    def visitIdentifierList(self, ctx:MT22Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initialization.
    def visitInitialization(self, ctx:MT22Parser.InitializationContext):
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


    # Visit a parse tree produced by MT22Parser#inherSubpart.
    def visitInherSubpart(self, ctx:MT22Parser.InherSubpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionBody.
    def visitFunctionBody(self, ctx:MT22Parser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#datatype.
    def visitDatatype(self, ctx:MT22Parser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numberExpression.
    def visitNumberExpression(self, ctx:MT22Parser.NumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatExpression.
    def visitFloatExpression(self, ctx:MT22Parser.FloatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatRelationalExpression.
    def visitFloatRelationalExpression(self, ctx:MT22Parser.FloatRelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatLogicalExpression.
    def visitFloatLogicalExpression(self, ctx:MT22Parser.FloatLogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatAdditiveExpression.
    def visitFloatAdditiveExpression(self, ctx:MT22Parser.FloatAdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatMultiplicativeExpression.
    def visitFloatMultiplicativeExpression(self, ctx:MT22Parser.FloatMultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intExpression.
    def visitIntExpression(self, ctx:MT22Parser.IntExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intRelationalExpression.
    def visitIntRelationalExpression(self, ctx:MT22Parser.IntRelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intLogicalExpression.
    def visitIntLogicalExpression(self, ctx:MT22Parser.IntLogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intAdditiveExpression.
    def visitIntAdditiveExpression(self, ctx:MT22Parser.IntAdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intMultiplicativeExpression.
    def visitIntMultiplicativeExpression(self, ctx:MT22Parser.IntMultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:MT22Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpression.
    def visitLogicalExpression(self, ctx:MT22Parser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MT22Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MT22Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#negationSingExpression.
    def visitNegationSingExpression(self, ctx:MT22Parser.NegationSingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MT22Parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intNegationSignExpression.
    def visitIntNegationSignExpression(self, ctx:MT22Parser.IntNegationSignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intPrimaryExpression.
    def visitIntPrimaryExpression(self, ctx:MT22Parser.IntPrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatNegationSignExpression.
    def visitFloatNegationSignExpression(self, ctx:MT22Parser.FloatNegationSignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatPrimaryExpression.
    def visitFloatPrimaryExpression(self, ctx:MT22Parser.FloatPrimaryExpressionContext):
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


    # Visit a parse tree produced by MT22Parser#stringExpression.
    def visitStringExpression(self, ctx:MT22Parser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringPrimaryExpression.
    def visitStringPrimaryExpression(self, ctx:MT22Parser.StringPrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolExpression.
    def visitBoolExpression(self, ctx:MT22Parser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#negationExpression.
    def visitNegationExpression(self, ctx:MT22Parser.NegationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolPrimaryExpression.
    def visitBoolPrimaryExpression(self, ctx:MT22Parser.BoolPrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
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


    # Visit a parse tree produced by MT22Parser#iterationStatement.
    def visitIterationStatement(self, ctx:MT22Parser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forCondition.
    def visitForCondition(self, ctx:MT22Parser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forDeclaration.
    def visitForDeclaration(self, ctx:MT22Parser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditionExpression.
    def visitConditionExpression(self, ctx:MT22Parser.ConditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#updateExpression.
    def visitUpdateExpression(self, ctx:MT22Parser.UpdateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argumentList.
    def visitArgumentList(self, ctx:MT22Parser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#jumpStatement.
    def visitJumpStatement(self, ctx:MT22Parser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MT22Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayIndex.
    def visitArrayIndex(self, ctx:MT22Parser.ArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elements.
    def visitElements(self, ctx:MT22Parser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element.
    def visitElement(self, ctx:MT22Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sepcialFunction.
    def visitSepcialFunction(self, ctx:MT22Parser.SepcialFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intArgument.
    def visitIntArgument(self, ctx:MT22Parser.IntArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatArgument.
    def visitFloatArgument(self, ctx:MT22Parser.FloatArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringArgument.
    def visitStringArgument(self, ctx:MT22Parser.StringArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolArgument.
    def visitBoolArgument(self, ctx:MT22Parser.BoolArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listexpr.
    def visitListexpr(self, ctx:MT22Parser.ListexprContext):
        return self.visitChildren(ctx)



del MT22Parser