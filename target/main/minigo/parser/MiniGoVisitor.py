# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#single_method_call.
    def visitSingle_method_call(self, ctx:MiniGoParser.Single_method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_call.
    def visitList_method_call(self, ctx:MiniGoParser.List_method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_arr_access.
    def visitStruct_arr_access(self, ctx:MiniGoParser.Struct_arr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_access.
    def visitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_access.
    def visitArr_access(self, ctx:MiniGoParser.Arr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_arr_access_prime.
    def visitStruct_arr_access_prime(self, ctx:MiniGoParser.Struct_arr_access_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_ele.
    def visitArr_ele(self, ctx:MiniGoParser.Arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declr.
    def visitList_declr(self, ctx:MiniGoParser.List_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_values.
    def visitPrimitive_values(self, ctx:MiniGoParser.Primitive_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_types.
    def visitPrimitive_types(self, ctx:MiniGoParser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_type.
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_types.
    def visitAll_types(self, ctx:MiniGoParser.All_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_var.
    def visitAll_var(self, ctx:MiniGoParser.All_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declr_all.
    def visitDeclr_all(self, ctx:MiniGoParser.Declr_allContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_opp.
    def visitAssign_opp(self, ctx:MiniGoParser.Assign_oppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:MiniGoParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:MiniGoParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MiniGoParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postfixExpr.
    def visitPostfixExpr(self, ctx:MiniGoParser.PostfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_dec.
    def visitVar_dec(self, ctx:MiniGoParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_dec_init.
    def visitVar_dec_init(self, ctx:MiniGoParser.Var_dec_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_dec_no_init.
    def visitVar_dec_no_init(self, ctx:MiniGoParser.Var_dec_no_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_dec.
    def visitConst_dec(self, ctx:MiniGoParser.Const_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_dec.
    def visitFunc_dec(self, ctx:MiniGoParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_arguments.
    def visitList_arguments(self, ctx:MiniGoParser.List_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_arg_prime.
    def visitList_arg_prime(self, ctx:MiniGoParser.List_arg_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg.
    def visitArg(self, ctx:MiniGoParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg_prime.
    def visitArg_prime(self, ctx:MiniGoParser.Arg_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list_in_lit.
    def visitDimension_list_in_lit(self, ctx:MiniGoParser.Dimension_list_in_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list_in_var.
    def visitDimension_list_in_var(self, ctx:MiniGoParser.Dimension_list_in_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_in_lit.
    def visitDimension_in_lit(self, ctx:MiniGoParser.Dimension_in_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_in_var.
    def visitDimension_in_var(self, ctx:MiniGoParser.Dimension_in_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nested_list.
    def visitNested_list(self, ctx:MiniGoParser.Nested_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_list.
    def visitElement_list(self, ctx:MiniGoParser.Element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_val.
    def visitList_val(self, ctx:MiniGoParser.List_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_prime.
    def visitExpression_prime(self, ctx:MiniGoParser.Expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_def.
    def visitStruct_def(self, ctx:MiniGoParser.Struct_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field.
    def visitList_field(self, ctx:MiniGoParser.List_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_dec.
    def visitField_dec(self, ctx:MiniGoParser.Field_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field_init.
    def visitList_field_init(self, ctx:MiniGoParser.List_field_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field_prime.
    def visitList_field_prime(self, ctx:MiniGoParser.List_field_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_init.
    def visitField_init(self, ctx:MiniGoParser.Field_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_method_def.
    def visitStruct_method_def(self, ctx:MiniGoParser.Struct_method_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_dec.
    def visitInterface_dec(self, ctx:MiniGoParser.Interface_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method.
    def visitList_method(self, ctx:MiniGoParser.List_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_prime.
    def visitList_method_prime(self, ctx:MiniGoParser.List_method_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_dec.
    def visitMethod_dec(self, ctx:MiniGoParser.Method_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_prototypes.
    def visitList_prototypes(self, ctx:MiniGoParser.List_prototypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_prototypes_prime.
    def visitList_prototypes_prime(self, ctx:MiniGoParser.List_prototypes_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prototype.
    def visitPrototype(self, ctx:MiniGoParser.PrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prototype_prime.
    def visitPrototype_prime(self, ctx:MiniGoParser.Prototype_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_assign.
    def visitArr_assign(self, ctx:MiniGoParser.Arr_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_assign.
    def visitStruct_assign(self, ctx:MiniGoParser.Struct_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_else_if_stmt.
    def visitList_else_if_stmt(self, ctx:MiniGoParser.List_else_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_else_if_stmt_prime.
    def visitList_else_if_stmt_prime(self, ctx:MiniGoParser.List_else_if_stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#one_esle_if_stmt.
    def visitOne_esle_if_stmt(self, ctx:MiniGoParser.One_esle_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt.
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for_stmt.
    def visitBasic_for_stmt(self, ctx:MiniGoParser.Basic_for_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for_stmt.
    def visitInit_for_stmt(self, ctx:MiniGoParser.Init_for_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for_stmt.
    def visitRange_for_stmt(self, ctx:MiniGoParser.Range_for_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)



del MiniGoParser