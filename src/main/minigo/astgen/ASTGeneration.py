import sys
sys.path.append('./main/minigo/utils/')
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *


class ASTGeneration(MiniGoVisitor):
    
    def visitAll_types(self,ctx:MiniGoParser.All_typesContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.getChild(0))
    
    def visitArr_type(self,ctx:MiniGoParser.Arr_typeContext):
        if ctx.IDENTIFIER():
            return ArrayType(self.visit(ctx.dimension_list_in_lit()), Id(ctx.IDENTIFIER().getText()))
        return ArrayType(self.visit(ctx.dimension_list_in_lit()), self.visit(ctx.primitive_types()))


    def visitFunc_call(self, ctx: MiniGoParser.Func_callContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.list_val()))
    
    def visitSingle_method_call(self, ctx: MiniGoParser.Single_method_callContext):
        return (ctx.IDENTIFIER().getText(), self.visit(ctx.list_val()))
    
    def visitList_method_call(self, ctx: MiniGoParser.List_method_callContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.single_method_call())]
        return [self.visit(ctx.single_method_call())] + self.visit(ctx.list_method_call())
    
    def visitMethod_call(self, ctx: MiniGoParser.Method_callContext):
        list_method_call = self.visit(ctx.list_method_call())
        receiver = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.struct_arr_access())
        for method in list_method_call:
            receiver = MethCall(receiver, method[0], method[1])
        return receiver
    
    def visitList_val(self, ctx: MiniGoParser.List_valContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expression_prime())
    
    def visitExpression_prime(self, ctx: MiniGoParser.Expression_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expression_prime())

    def visitDimension_in_lit(self, ctx: MiniGoParser.Dimension_in_litContext):
        if ctx.INTEGER_LIT():
            return IntLiteral(ctx.INTEGER_LIT().getText())
        return Id(ctx.IDENTIFIER().getText())
    
    def visitDimension_in_var(self, ctx: MiniGoParser.Dimension_in_varContext):
        return self.visit(ctx.expression())
    
    def visitDimension_list_in_lit(self, ctx: MiniGoParser.Dimension_list_in_litContext):
        if ctx.dimension_list_in_lit():
            return [self.visit(ctx.dimension_in_lit())] + self.visit(ctx.dimension_list_in_lit())
        return [self.visit(ctx.dimension_in_lit())]
    
    def visitDimension_list_in_var(self, ctx: MiniGoParser.Dimension_list_in_varContext):
        if ctx.dimension_list_in_var():
            return [self.visit(ctx.dimension_in_var())] + self.visit(ctx.dimension_list_in_var())
        return [self.visit(ctx.dimension_in_var())]



    def visitArr_ele(self, ctx: MiniGoParser.Arr_eleContext):
        return [ctx.IDENTIFIER().getText(), self.visit(ctx.dimension_list_in_var())]
        
    def visitStruct_arr_access_prime(self, ctx: MiniGoParser.Struct_arr_access_primeContext):
        if ctx.getChildCount() == 3:
            if ctx.arr_ele():
                arr_ele = self.visit(ctx.arr_ele())
                return ArrayCell(FieldAccess(self.visit(ctx.struct_arr_access_prime()), arr_ele[0]), arr_ele[1])
            return FieldAccess(self.visit(ctx.struct_arr_access_prime()), ctx.IDENTIFIER().getText())
        if ctx.arr_ele():
            arr_ele = self.visit(ctx.arr_ele())
            return ArrayCell(Id(arr_ele[0]), arr_ele[1])
        return Id(ctx.IDENTIFIER().getText())
    
    def visitArr_access(self, ctx: MiniGoParser.Arr_accessContext):
        return self.visit(ctx.struct_arr_access_prime())
    
    def visitStruct_access(self, ctx: MiniGoParser.Struct_accessContext):
        return FieldAccess(self.visit(ctx.struct_arr_access_prime()), ctx.IDENTIFIER().getText())
    
    def visitStruct_arr_access(self, ctx: MiniGoParser.Struct_arr_accessContext):
        return self.visit(ctx.getChild(0))
    


    def visitArr_lit(self, ctx: MiniGoParser.Arr_litContext):
        return ArrayLiteral(self.visit(ctx.dimension_list_in_lit()), self.visit(ctx.all_types()), self.visit(ctx.nested_list()))

    def visitNested_list(self, ctx: MiniGoParser.Nested_listContext):
        if ctx.getChildCount() == 2:
            return []
        return self.visit(ctx.element_list())

    def visitElement_list(self, ctx: MiniGoParser.Element_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.element())]
        return [self.visit(ctx.element())] + self.visit(ctx.element_list())

    def visitElement(self, ctx: MiniGoParser.ElementContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.getChild(0))



    def visitPrimitive_values(self,ctx:MiniGoParser.Primitive_valuesContext):
        if ctx.INTEGER_LIT():
            return IntLiteral(ctx.INTEGER_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.KW_NIL():
            return NilLiteral()
        return BooleanLiteral(ctx.BOOLEAN_LIT().getText())
        
        
    def visitPrimitive_types(self,ctx:MiniGoParser.Primitive_typesContext):
        if ctx.KW_INT():
            return IntType()
        elif ctx.KW_FLOAT():
            return FloatType()
        elif ctx.KW_STRING():
            return StringType()
        else:
            return BoolType()
        
    def visitAssign_opp(self,ctx:MiniGoParser.Assign_oppContext):
        return ctx.getChild(0).getText()

    def visitPrimaryExpr(self,ctx:MiniGoParser.PrimaryExprContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.getChild(0))
    
    def visitPostfixExpr(self,ctx:MiniGoParser.PostfixExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.postfixExpr()), ctx.IDENTIFIER().getText())
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.postfixExpr()), self.visit(ctx.getChild(1)))
        return MethCall(self.visit(ctx.postfixExpr()), ctx.IDENTIFIER().getText(), self.visit(ctx.list_val()))

    def visitUnaryExpr(self,ctx:MiniGoParser.UnaryExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
    
    def visitMultiplicativeExpr(self,ctx:MiniGoParser.MultiplicativeExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitAdditiveExpr(self,ctx:MiniGoParser.AdditiveExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitEqualityExpr(self,ctx:MiniGoParser.EqualityExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitLogicalAndExpr(self,ctx:MiniGoParser.LogicalAndExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitLogicalOrExpr(self,ctx:MiniGoParser.LogicalOrExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitExpression(self,ctx:MiniGoParser.ExpressionContext):
        return self.visit(ctx.getChild(0))
    
    def visitVar_dec(self,ctx:MiniGoParser.Var_decContext):
        return self.visit(ctx.getChild(0))
    
    def visitVar_dec_init(self,ctx:MiniGoParser.Var_dec_initContext):
        if ctx.getChildCount() == 5:
            return VarDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.all_types()), self.visit(ctx.expression()))
        return VarDecl(ctx.IDENTIFIER().getText(), None, self.visit(ctx.expression()))
    
    def visitVar_dec_no_init(self,ctx:MiniGoParser.Var_dec_no_initContext):
        return VarDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.all_types()), None)
    
    def visitConst_dec(self,ctx:MiniGoParser.Const_decContext):
        return ConstDecl(ctx.IDENTIFIER().getText(), None, self.visit(ctx.expression()))
    


    def visitFunc_dec(self,ctx:MiniGoParser.Func_decContext):
        if ctx.getChildCount() == 8:
            return FuncDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.list_arguments()), VoidType(), self.visit(ctx.list_statement()))
        return FuncDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.list_arguments()), self.visit(ctx.all_types()), self.visit(ctx.list_statement()))
    
    def visitStruct_method_def(self,ctx:MiniGoParser.Struct_method_defContext):
        if ctx.getChildCount() == 12:
            return MethodDecl(ctx.IDENTIFIER(0).getText(), Id(ctx.IDENTIFIER(1).getText()), FuncDecl(ctx.IDENTIFIER(2).getText(), self.visit(ctx.list_arguments()), VoidType(), self.visit(ctx.list_statement())))
        return MethodDecl(ctx.IDENTIFIER(0).getText(), Id(ctx.IDENTIFIER(1).getText()), FuncDecl(ctx.IDENTIFIER(2).getText(), self.visit(ctx.list_arguments()), self.visit(ctx.all_types()), self.visit(ctx.list_statement())))



    def visitList_arguments(self,ctx:MiniGoParser.List_argumentsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_arg_prime())
    
    def visitList_arg_prime(self,ctx:MiniGoParser.List_arg_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(0)) + self.visit(ctx.list_arg_prime())
    
    def visitArg(self,ctx:MiniGoParser.ArgContext):
        return [ParamDecl(param_name, self.visit(ctx.all_types())) for param_name in self.visit(ctx.arg_prime())]   
    
    def visitArg_prime(self,ctx:MiniGoParser.Arg_primeContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.arg_prime())

    
    def visitAll_var(self,ctx:MiniGoParser.All_varContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.getChild(0))
    
    def visitAssignment(self,ctx:MiniGoParser.AssignmentContext):
        if ctx.getChildCount() == 3:
            if self.visit(ctx.assign_opp()) == ":=":
                return Assign(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            elif self.visit(ctx.assign_opp()) == "+=":
                return Assign(self.visit(ctx.getChild(0)), BinaryOp("+", self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))))
            elif self.visit(ctx.assign_opp()) == "-=":
                return Assign(self.visit(ctx.getChild(0)), BinaryOp("-", self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))))
            elif self.visit(ctx.assign_opp()) == "*=":
                return Assign(self.visit(ctx.getChild(0)), BinaryOp("*", self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))))
            elif self.visit(ctx.assign_opp()) == "/=":
                return Assign(self.visit(ctx.getChild(0)), BinaryOp("/", self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))))
            elif self.visit(ctx.assign_opp()) == "%=":
                return Assign(self.visit(ctx.getChild(0)), BinaryOp("%", self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2))))
        return self.visit(ctx.getChild(0))

    def visitArr_assign(self,ctx:MiniGoParser.Arr_assignContext):
        return Assign(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))  

    def visitStruct_assign(self,ctx:MiniGoParser.Struct_assignContext):
        return Assign(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitStruct_def(self,ctx:MiniGoParser.Struct_defContext):
        list_field = self.visit(ctx.list_field())
        return StructType(ctx.IDENTIFIER().getText(), list_field[0], list_field[1])
    
    def visitList_field(self, ctx: MiniGoParser.List_fieldContext):
        result = [[], []] 
        if ctx.getChildCount() == 2:
            child_result = self.visit(ctx.getChild(0))
            if ctx.field_dec():
                result[0].append(child_result)
            else:
                result[1].append(child_result)
            return result

        child_result = self.visit(ctx.list_field())

        if ctx.field_dec():
            child_result[0].insert(0, self.visit(ctx.field_dec()))
        else:
            child_result[1].insert(0, self.visit(ctx.struct_method_def()))
        return child_result
    
    def visitField_dec(self,ctx:MiniGoParser.Field_decContext):
        return [ctx.IDENTIFIER().getText(), self.visit(ctx.all_types())]

    def visitStruct_lit(self, ctx: MiniGoParser.Struct_litContext):
        return StructLiteral(ctx.IDENTIFIER().getText(), self.visit(ctx.list_field_init()))

    def visitList_field_init(self, ctx: MiniGoParser.List_field_initContext):
        if ctx.list_field_prime():
            return self.visit(ctx.list_field_prime())
        return []

    def visitList_field_prime(self, ctx: MiniGoParser.List_field_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.field_init())]
        return [self.visit(ctx.field_init())] + self.visit(ctx.list_field_prime())

    def visitField_init(self, ctx: MiniGoParser.Field_initContext):
        return [ctx.IDENTIFIER().getText(), self.visit(ctx.expression())]

    def visitInterface_dec(self, ctx: MiniGoParser.Interface_decContext):
        return InterfaceType(ctx.IDENTIFIER().getText(), self.visit(ctx.list_method()))
    
    def visitList_method(self, ctx: MiniGoParser.List_methodContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_method_prime())

    def visitList_method_prime(self, ctx: MiniGoParser.List_method_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        return [self.visit(ctx.getChild(0))] + self.visit(ctx.list_method_prime())
    
    def visitMethod_dec(self, ctx: MiniGoParser.Method_decContext):
        if ctx.getChildCount() == 5:
            return Prototype(ctx.IDENTIFIER().getText(), self.visit(ctx.list_prototypes()), VoidType())
        return Prototype(ctx.IDENTIFIER().getText(), self.visit(ctx.list_prototypes()), self.visit(ctx.all_types()))
   
    def visitList_prototypes(self,ctx:MiniGoParser.List_prototypesContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_prototypes_prime())
    
    def visitList_prototypes_prime(self,ctx:MiniGoParser.List_prototypes_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(0)) + self.visit(ctx.list_prototypes_prime())
    
    def visitPrototype(self,ctx:MiniGoParser.PrototypeContext):
        return [self.visit(ctx.all_types()) for i in range(self.visit(ctx.prototype_prime()))]   
    
    def visitPrototype_prime(self,ctx:MiniGoParser.Prototype_primeContext):
        if ctx.getChildCount() == 1:
            return 1
        return 1 + self.visit(ctx.prototype_prime())
    


    def visitIf_stmt(self, ctx: MiniGoParser.If_stmtContext):
        return If(self.visit(ctx.expression()), self.visit(ctx.list_statement()), self.visit(ctx.list_else_if_stmt()))
        
    def visitList_else_if_stmt(self, ctx: MiniGoParser.List_else_if_stmtContext):
        list_else_if = self.visit(ctx.list_else_if_stmt_prime())
        ans = self.visit(ctx.else_stmt()) if ctx.else_stmt() else None
        if list_else_if == []:
            return ans
        for i in range(len(list_else_if)-1, -1, -1):
            ans = If(list_else_if[i][0], list_else_if[i][1], ans)
        return ans
        
    def visitList_else_if_stmt_prime(self, ctx: MiniGoParser.List_else_if_stmt_primeContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.getChild(0))] + self.visit(ctx.list_else_if_stmt_prime())

    def visitOne_esle_if_stmt(self, ctx: MiniGoParser.One_esle_if_stmtContext):
        return [self.visit(ctx.expression()), self.visit(ctx.list_statement())]

    def visitElse_stmt(self, ctx: MiniGoParser.Else_stmtContext):
        return self.visit(ctx.list_statement())
    


    def visitFor_stmt(self, ctx: MiniGoParser.For_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitBasic_for_stmt(self, ctx: MiniGoParser.Basic_for_stmtContext):
        return ForBasic(self.visit(ctx.expression()), self.visit(ctx.list_statement()))

    def visitInit_for_stmt(self, ctx: MiniGoParser.Init_for_stmtContext):
        return ForStep(self.visit(ctx.getChild(1)), self.visit(ctx.expression()), self.visit(ctx.getChild(5)), self.visit(ctx.list_statement()))

    def visitRange_for_stmt(self, ctx: MiniGoParser.Range_for_stmtContext):
        if ctx.UNDERLINE():
            return ForEach(Id(ctx.UNDERLINE().getText()), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression()), self.visit(ctx.list_statement()))
        return ForEach(Id(ctx.IDENTIFIER(0).getText()), Id(ctx.IDENTIFIER(1).getText()), self.visit(ctx.expression()), self.visit(ctx.list_statement()))



    def visitBreak_stmt(self, ctx: MiniGoParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: MiniGoParser.Continue_stmtContext):
        return Continue()

    def visitCall_stmt(self, ctx: MiniGoParser.Call_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitReturn_stmt(self, ctx: MiniGoParser.Return_stmtContext):
        if ctx.getChildCount() == 1:
            return Return(None)
        return Return(self.visit(ctx.expression()))

    def visitList_statement(self, ctx: MiniGoParser.List_statementContext):
        if ctx.getChildCount() == 1:
            return Block([self.visit(ctx.stmt())])
        
        stmt_list = self.visit(ctx.list_statement())

        if isinstance(stmt_list, Block):
            return Block([self.visit(ctx.stmt())] + stmt_list.member)
        else:
            return Block([self.visit(ctx.stmt())] + [stmt_list])

    def visitStmt(self, ctx: MiniGoParser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitDeclr_all(self, ctx: MiniGoParser.Declr_allContext):
        return self.visit(ctx.getChild(0))
    
    def visitList_declr(self, ctx: MiniGoParser.List_declrContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declr_all())]
        return [self.visit(ctx.declr_all())] + self.visit(ctx.list_declr())
    
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.list_declr()))
    

    

    


    


    

