"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class NilType:pass

class DeclKind:
    VARIABLE = 1
    CONSTANT = 2
    FUNCTION = 3
    PARAMETER = 4
    METHOD = 6
    STRUCT = 7
    INTERFACE = 8

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in (self.partype or [])) + "]," + str(self.rettype) + ")"
    
class StructMType:
    def __init__(self, name, elements, methods = None):
        self.name = name
        self.elements = elements
        self.methods = methods

    def __str__(self):
        return "StructMType(" + str(self.name) + "," + str(self.elements) + "," + str(self.methods) + ")"
    

class Symbol:
    def __init__(self,name,mtype, kind = None, val = None):
        self.name = name
        self.mtype = mtype
        self.kind = kind
        self.val = val

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + "," + str(self.kind) + "," + str(self.val) + ")"
    
    
class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType()), DeclKind.FUNCTION),
                            Symbol("putInt",MType([IntType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("putIntLn",MType([IntType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("getFloat",MType([],FloatType()), DeclKind.FUNCTION),
                            Symbol("putFloat",MType([FloatType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("putFloatLn",MType([FloatType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("getBool",MType([],BoolType()), DeclKind.FUNCTION),
                            Symbol("putBool",MType([BoolType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("putBoolLn",MType([BoolType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("getString",MType([],StringType()), DeclKind.FUNCTION),
                            Symbol("putString",MType([StringType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("putStringLn",MType([StringType()],VoidType()), DeclKind.FUNCTION),
                            Symbol("putLn",MType([],VoidType()), DeclKind.FUNCTION)
                            ]
 
    
    def check(self):
        return self.visit(self.ast,self.global_envi)
    
    def get_symbol(self, name, c):
        return next(filter(lambda x: x.name == name, c), False)

    #class Program(AST): decl : List[Decl]
    def visitProgram(self,ast, c):
        env = []
        list_decl = ast.decl.copy()
        for decl in ast.decl:
            if type(decl) is MethodDecl:
                for sub_decl in ast.decl:
                    if type(sub_decl) is StructType and sub_decl.name == decl.recType.name:
                        sub_decl.methods = [] if sub_decl.methods is None else sub_decl.methods
                        sub_decl.methods.append(decl)
                        list_decl.remove(decl)

        for decl in list_decl:
            if type(decl) is FuncDecl:
                env.append(Symbol(decl.name, MType([x.parType for x in decl.params],decl.retType), DeclKind.FUNCTION))
            elif type(decl) is StructType:
                list_method_mtype = list(map(lambda x: [x.fun.name, MType([y.parType for y in x.fun.params], x.fun.retType)], decl.methods))
                env.append(Symbol(decl.name, StructMType(decl.name, decl.elements, list_method_mtype), DeclKind.STRUCT))
            elif type(decl) is InterfaceType:
                env.append(Symbol(decl.name, decl, DeclKind.INTERFACE))
        env += self.global_envi
        reduce(lambda acc,ele: self.visit(ele,acc), list_decl,[self.global_envi, env])

    # class VarDecl(Decl,BlockMember): varName : str
    #                                  varType : Type # None if there is no type
    #                                  varInit : Expr # None if there is no initialization
    def visitVarDecl(self, ast, c):
        res = self.get_symbol(ast.varName, c[0])
        if res: raise Redeclared(Variable(), ast.varName)
        
        if ast.varInit:
            ###
            if type(ast.varInit) is FuncCall:
                initType, _ = self.visitFuncCall(ast.varInit, c, True)
            elif type(ast.varInit) is MethCall:
                initType, _ = self.visitMethCall(ast.varInit, c, True)
            elif type(ast.varInit) is Id:
                initType, _ = self.visitId(ast.varInit, c, True)
            elif type(ast.varInit) is NilLiteral:
                initType = NilType()
            else: initType, _ = self.visit(ast.varInit, c)
            ###
            if ast.varType is None:
                var_type = initType
            elif type(ast.varType) is Id:
                var_type, _ = self.visit(ast.varType, c)
            elif type(ast.varType) is StructMType:
                var_type = ast.varType
            else: var_type = self.visit(ast.varType, c)

            if type(var_type) is VoidType: raise TypeMismatch(ast)
            elif type(var_type) is FloatType:
                if type(initType) is not IntType and type(initType) is not FloatType:
                    raise TypeMismatch(ast)
            
            elif type(var_type) is ArrayType:
                if type(initType) is not ArrayType or var_type.dimens != initType.dimens:
                    
                    raise TypeMismatch(ast)
                elif (type(var_type.eleType) is not type(initType.eleType) and type(var_type.eleType) is not FloatType) or ((type(initType.eleType) is StructMType or type(initType.eleType) is InterfaceType) and var_type.eleType.name != initType.eleType.name):
                    raise TypeMismatch(ast)

                if type(var_type.eleType) is FloatType:
                    if type(initType.eleType) is not IntType and type(initType.eleType) is not FloatType:
                        raise TypeMismatch(ast)
                
                    
            elif type(var_type) is InterfaceType:
                
                if type(initType) is not StructMType and type(initType) is not InterfaceType and type(initType) is not NilType:
                    raise TypeMismatch(ast)
                if type(initType) is StructMType:
                    list_meth_left = var_type.methods
                    list_meth_right = list(map(lambda x: AST.Prototype(x[0], x[1].partype, x[1].rettype), initType.methods))
                    left_wing = self.normalize_prototype_list(list_meth_left, c)
                    right_wing = self.normalize_prototype_list(list_meth_right, c)
                    if len(left_wing) > len(right_wing):
                        raise TypeMismatch(ast)
                    for i in range(len(left_wing)):
                        r_cur = next(filter(lambda x: x[0] == left_wing[i][0], right_wing), False)
                        if not r_cur:
                            raise TypeMismatch(ast)
                        if left_wing[i] != r_cur:
                            raise TypeMismatch(ast)
                        
                elif type(initType) is InterfaceType and initType.name != var_type.name:
                    raise TypeMismatch(ast)
                
            elif type(var_type) is StructMType:
                if type(initType) is not StructMType or var_type.name != initType.name:
                    if type(initType) is not NilType:
                        raise TypeMismatch(ast)

            elif type(var_type) is not InterfaceType and type(var_type) is not FloatType and type(var_type) is not type(initType):
                if not (type(var_type) is StructMType and type(initType) is NilType):
                    raise TypeMismatch(ast)
        
        else:
            if type(ast.varType) is Id:
                var_type, _ = self.visit(ast.varType, c)
            else: var_type = self.visit(ast.varType, c)
        
        return [[Symbol(ast.varName, var_type, DeclKind.VARIABLE)] + c[0]] + c[1:]
        
    # class FuncDecl(Decl): name: str
    #                       params: List[ParamDecl]
    #                       retType: Type # VoidType if there is no return type
    #                       body: Block
    def visitFuncDecl(self,ast, c):
        res = self.get_symbol(ast.name, c[0])
        if res: raise Redeclared(Function(), ast.name)

        list_type_param = list(map(lambda x: x.parType, ast.params))

        if type(ast.retType) is Id:
            rettype, _ = self.visit(ast.retType, c) 
        else: rettype = self.visit(ast.retType, c)

        new_c = reduce(lambda acc, cur: self.visit(cur, acc), ast.params, [[]] + [[Symbol(ast.name, MType(list_type_param,rettype), DeclKind.FUNCTION)] + c[0]] + c[1:])

        new_c2 = self.visit(ast.body, [[]] + new_c)
        flatten_new_c2 = [symbol for scope in new_c2 for symbol in scope]
        cur_func = next(filter(lambda x: x.name == ast.name, flatten_new_c2), False)
        
       
        if cur_func.val:
            for ret in cur_func.val:
                if type(ret[1]) is not type(rettype):
                    if type(ret[1]) is NilType and (type(rettype) is VoidType or type(rettype) is StructMType or type(rettype) is InterfaceType):pass
                    else: raise TypeMismatch(ret[0])
                elif type(ret[1]) is ArrayType:
                    if type(ret[1].eleType) is not type(rettype.eleType) or ((type(ret[1].eleType) is StructMType or type(ret[1].eleType) is InterfaceType) and ret[1].eleType.name != rettype.eleType.name):
                        raise TypeMismatch(ret[0])
                    if (type(ret[1]) is StructMType or type(ret[1]) is InterfaceType) and ret[1].name != rettype.name:
                        raise TypeMismatch(ret[0])
                    
                elif (type(ret[1]) is StructMType or type(ret[1]) is InterfaceType) and ret[1].name != rettype.name:
                    raise TypeMismatch(ret[0])
              
        return [[Symbol(ast.name, MType(list_type_param,rettype), DeclKind.FUNCTION, cur_func.val)] + c[0]] + c[1:]
    
    # class ParamDecl(Decl): parName: str
    #                        parType: Type
    def visitParamDecl(self,ast, c):
        res = self.get_symbol(ast.parName, c[0])
        if res: raise Redeclared(Parameter(), ast.parName)

        if type(ast.parType) is Id:
            rettype, _ = self.visit(ast.parType, c)
        else: rettype = self.visit(ast.parType, c)

        return [[Symbol(ast.parName, rettype, DeclKind.PARAMETER)] + c[0]] + c[1:]

    # class ConstDecl(Decl,BlockMember): conName : str
    #                                    conType : Type # None if there is no type 
    #                                    iniExpr : Expr
    def visitConstDecl(self,ast,c):
        res = self.get_symbol(ast.conName, c[0])
        if res: raise Redeclared(Constant(), ast.conName)

        ###
        if type(ast.iniExpr) is FuncCall:
            initType, initVal = self.visitFuncCall(ast.iniExpr, c, True)
        elif type(ast.iniExpr) is MethCall:
            initType, initVal = self.visitMethCall(ast.iniExpr, c, True)
        elif type(ast.iniExpr) is Id:
            initType, initVal = self.visitId(ast.iniExpr, c, True)
        else: initType, initVal = self.visit(ast.iniExpr, c)
        ###

        if ast.conType is None:
            ast.conType = initType
        if not type(ast.conType) is type(initType):
            raise TypeMismatch(ast)
        
        return [[Symbol(ast.conName, ast.conType, DeclKind.CONSTANT, initVal)] + c[0]] + c[1:]




    # class MethodDecl(Decl): receiver: str
    #                         recType: Type
    #                         fun: FuncDecl
    def visitMethodDecl(self,ast,c):
        res = self.get_symbol(ast.fun.name, c[0])
        if res: raise Redeclared(Method(), ast.fun.name)

        list_type_param = list(map(lambda x: x.parType, ast.fun.params))

        if type(ast.fun.retType) is Id:
            rettype, _ = self.visit(ast.fun.retType, c)
        else: rettype = self.visit(ast.fun.retType, c)
        
        receiver_param_decl = ParamDecl(ast.receiver,ast.recType)
        new_c1 = self.visit(receiver_param_decl, [[]] + [c[0] + [Symbol(ast.fun.name, MType(list_type_param,rettype), DeclKind.METHOD)]] + c[1:])
        new_c2 = reduce(lambda acc, cur: self.visit(cur, acc), ast.fun.params, [[]] + new_c1)
        new_c3 = self.visit(ast.fun.body, [[]] + new_c2)

        flatten_new_c3 = [symbol for scope in new_c3 for symbol in scope]
        cur_method = next(filter(lambda x: x.name == ast.fun.name, flatten_new_c3), False)
        

        if cur_method.val:
            for ret in cur_method.val:
                if type(ret[1]) is not type(rettype):
                    if type(ret[1]) is NilType and (type(rettype) is VoidType or type(rettype) is StructMType or type(rettype) is InterfaceType):pass
                    else: raise TypeMismatch(ret[0])
                elif type(ret[1]) is ArrayType and (ret[1].dimens != rettype.dimens or ret[1].eleType != rettype.eleType):
                    raise TypeMismatch(ret[0])
                elif (type(ret[1]) is StructMType or type(ret[1]) is InterfaceType) and ret[1].name != rettype.name:
                    raise TypeMismatch(ret[0])

        return [[Symbol(ast.fun.name, MType(list_type_param,rettype), DeclKind.METHOD, cur_method.val)] + c[0]] + c[1:]
    

    # class Prototype(AST): name: str
    #                       params:List[Type]
    #                       retType: Type # VoidType if there is no return type
    def visitPrototype(self,ast,c):
        res = self.get_symbol(ast.name, c[0])
        if res: raise Redeclared(Prototype(), ast.name)
        res = []
        for param in ast.params:
            if type(param) is Id:
                partype, _ = self.visit(param, c)
            else: partype = self.visit(param, c)
            res.append(partype)
        if type(ast.retType) is Id:
            rettype, _ = self.visit(ast.retType, c)
        else: rettype = self.visit(ast.retType, c)

        return [[Symbol(ast.name, MType(res,rettype))] + c[0]] + c[1:]
    
    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitVoidType(self,ast,c):
        return VoidType()


    # class ArrayType(Type): dimens:List[Expr]
    #                        eleType:Type
    def visitArrayType(self,ast,c):
        dimens_literal = []
        for dim in ast.dimens:
            if type(dim) is Id:
                dim_type, dim_val = self.visitId(dim, c, True)
            else: dim_type, dim_val = self.visit(dim, c)
            if type(dim_type) is not IntType:
                raise TypeMismatch(ast)
            dimens_literal.append(IntLiteral(dim_val))

        if type(ast.eleType) is Id:
            ele_type, _ = self.visit(ast.eleType, c)
        else: ele_type = self.visit(ast.eleType, c)
        return ArrayType(dimens_literal, ele_type)

    # Subfunction for StructType
    def visitFieldStruct(self, tuple, c):
        res = self.get_symbol(tuple[0], c[0])
        if res: raise Redeclared(Field(), tuple[0])
        if type(tuple[1]) is Id:
            field_type, _ = self.visit(tuple[1], c)
        else: field_type = self.visit(tuple[1], c)
        
        return [[Symbol(tuple[0], field_type)] + c[0]] + c[1:]
    
    # class StructType(Type): name: str
    #                         elements:List[Tuple[str,Type]]
    #                         methods:List[MethodDecl]
    def visitStructType(self,ast,c):
        res = self.get_symbol(ast.name, c[0])
        if res: raise Redeclared(Type(), ast.name)

        list_method_mtype = list(map(lambda x: [x.fun.name, MType([y.parType for y in x.fun.params], x.fun.retType)], ast.methods))

        new_c = reduce(lambda acc, cur: self.visitFieldStruct(cur, acc), ast.elements, [[]] + [[Symbol(ast.name, StructMType(ast.name, ast.elements, list_method_mtype), DeclKind.STRUCT)] + c[0]] + c[1:])
        
        reduce(lambda acc, cur: self.visit(cur, acc), ast.methods, new_c)

        return [[Symbol(ast.name, StructMType(ast.name, ast.elements, list_method_mtype), DeclKind.STRUCT)] + c[0]] + c[1:]

    # class InterfaceType(Type): name: str
    #                            methods:List[Prototype]
    def visitInterfaceType(self,ast,c):
        res = self.get_symbol(ast.name, c[0])
        if res: raise Redeclared(Type(), ast.name)
        
        reduce(lambda acc, cur: self.visit(cur, acc), ast.methods, [[]] + [c[0] + [Symbol(ast.name,ast ,DeclKind.INTERFACE)]] + c[1:])

        return [[Symbol(ast.name, ast, DeclKind.INTERFACE)] + c[0]] + c[1:]

    # class Block(Stmt): member:List[BlockMember]
    def visitBlock(self,ast,c):
        reduce(lambda acc, cur: self.visit(cur, acc), ast.member, c)
        return c

    def normalize_prototype_list(self, prototypes, c):
        result = []
        for proto in prototypes:
            if type(proto.retType) is Id: 
                ret = proto.retType.name
            elif type(proto.retType) is ArrayType:
                list_dimens = []
                for dim in proto.retType.dimens:
                    if type(dim) is Id:
                        dim_type, dim_val = self.visitId(dim, c, True)
                    else: dim_type, dim_val = self.visit(dim, c)
                    if type(dim_type) is not IntType:
                        raise TypeMismatch(proto)
                    list_dimens.append(IntLiteral(dim_val))
                eletype = proto.retType.name if type(proto.retType) is Id else type(proto.retType.eleType)
                ret = (list_dimens, eletype)
            else: 
                ret = type(proto.retType)
            list_param = []
            for param in proto.params:
                if type(param) is Id: 
                    list_param.append(param.name)
                elif type(param) is ArrayType:
                    list_dimens = []
                    for dim in param.dimens:
                        if type(dim) is Id:
                            dim_type, dim_val = self.visitId(dim, c, True)
                        else: dim_type, dim_val = self.visit(dim, c)
                        if type(dim_type) is not IntType:
                            raise TypeMismatch(param)
                        list_dimens.append(IntLiteral(dim_val))
                    eletype = param.name if type(param) is Id else type(param.eleType)
                    list_param.append((list_dimens, eletype))
                else: 
                    list_param.append(type(param))
            result.append((proto.name, list_param, ret))
        return result
    

    # class Assign(Stmt): lhs:LHS
    #                     rhs:Expr
    def visitAssign(self,ast,c):
        if type(ast.rhs) is FuncCall:
            right_type, _ = self.visitFuncCall(ast.rhs, c, True)
        elif type(ast.rhs) is MethCall:
            right_type, _ = self.visitMethCall(ast.rhs, c, True)
        elif type(ast.rhs) is Id:
            right_type, _ = self.visitId(ast.rhs, c, True)
        elif type(ast.rhs) is NilLiteral:
            right_type = NilType()
        else: right_type, _ = self.visit(ast.rhs, c)

        if type(ast.lhs) is Id:
            flatten_res = [symbol for scope in c for symbol in scope]
            res = next(filter(lambda sym: (sym.kind == DeclKind.VARIABLE or sym.kind == DeclKind.CONSTANT or sym.kind == DeclKind.PARAMETER) and (sym.name == ast.lhs.name), flatten_res), False)
            if not res:
                c[0].append(Symbol(ast.lhs.name, right_type, DeclKind.VARIABLE))
                left_type = right_type
            else:
                left_type, _ = self.visitId(ast.lhs, c, True)
                
        else: left_type, _ = self.visit(ast.lhs, c)

        if type(left_type) is VoidType: raise TypeMismatch(ast)
        elif type(left_type) is FloatType:
            if type(right_type) is not IntType and type(right_type) is not FloatType:
                raise TypeMismatch(ast)
        
        elif type(left_type) is ArrayType:
            if type(right_type) is not ArrayType or left_type.dimens != right_type.dimens:
                raise TypeMismatch(ast)
            elif (type(left_type.eleType) is not type(right_type.eleType) and type(left_type.eleType) is not FloatType) or ((type(right_type.eleType) is StructMType or type(right_type.eleType) is InterfaceType) and left_type.eleType.name != left_type.eleType.name):
                    raise TypeMismatch(ast)
            
            if type(left_type.eleType) is FloatType:
                if type(right_type.eleType) is not IntType and type(right_type.eleType) is not FloatType:
                    raise TypeMismatch(ast)
                
        elif type(left_type) is InterfaceType:
            if type(right_type) is not StructMType and type(right_type) is not InterfaceType and type(right_type) is not NilType:
                raise TypeMismatch(ast)
            elif type(right_type) is StructMType:
                list_meth_left = left_type.methods
                list_meth_right = list(map(lambda x: AST.Prototype(x[0], x[1].partype, x[1].rettype), right_type.methods))
                left_wing = self.normalize_prototype_list(list_meth_left, c)
                right_wing = self.normalize_prototype_list(list_meth_right, c)
                if len(left_wing) > len(right_wing):
                    raise TypeMismatch(ast)
                for i in range(len(left_wing)):
                    r_cur = next(filter(lambda x: x[0] == left_wing[i][0], right_wing), False)
                    if not r_cur:
                        raise TypeMismatch(ast)
                    if left_wing[i] != r_cur:
                        raise TypeMismatch(ast)
            elif type(right_type) is InterfaceType and right_type.name != left_type.name:
                raise TypeMismatch(ast)
            
        elif type(left_type) is StructMType:
            if type(right_type) is not StructMType or left_type.name != right_type.name:
                if type(right_type) is not NilType:
                    raise TypeMismatch(ast)
               
        elif type(left_type) is not InterfaceType and type(left_type) is not FloatType and type(left_type) is not type(right_type):
            if not (type(left_type) is StructMType and type(right_type) is NilType):
                raise TypeMismatch(ast)
        
        return c

    # class If(Stmt): expr:Expr
    #                 thenStmt:Stmt
    #                 elseStmt:Stmt # None if there is no else
    def visitIf(self,ast,c):
        if type(ast.expr) is FuncCall:
            expr_type, _ = self.visitFuncCall(ast.expr, c, True)
        elif type(ast.expr) is MethCall:
            expr_type, _ = self.visitMethCall(ast.expr, c, True)
        elif type(ast.expr) is Id:
            expr_type, _ = self.visitId(ast.expr, c, True)
        else: expr_type, _ = self.visit(ast.expr, c)
        
        if type(expr_type) is not BoolType:
            raise TypeMismatch(ast)
        
        self.visit(ast.thenStmt, [[]] + c)
        
        self.visit(ast.elseStmt, [[]] + c) if ast.elseStmt else None

        return c

    # class ForBasic(Stmt): cond:Expr
    #                       loop:Block
    def visitForBasic(self,ast,c):
        if type(ast.cond) is FuncCall:
            cond_type, _ = self.visitFuncCall(ast.cond, c, True)
        elif type(ast.cond) is MethCall:
            cond_type, _ = self.visitMethCall(ast.cond, c, True)
        elif type(ast.cond) is Id:
            cond_type, _ = self.visitId(ast.cond, c, True)
        else: cond_type, _ = self.visit(ast.cond, c)

        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.loop, [[]] + c)
        
        return c

    # class ForStep(Stmt): init:Stmt
    #                      cond:Expr
    #                      upda:Assign
    #                      loop:Block
    def visitForStep(self,ast,c):
        if type(ast.init) is Assign:
            c = [[]] + c
            self.visit(ast.init, c)
        else:
            new_c = self.visit(ast.init, [[]] + c)

        true_c = c if type(ast.init) is Assign else new_c

        if type(ast.cond) is FuncCall:
            cond_type, _ = self.visitFuncCall(ast.cond, true_c, True)
        elif type(ast.cond) is MethCall:
            cond_type, _ = self.visitMethCall(ast.cond, true_c, True)
        elif type(ast.cond) is Id:
            cond_type, _ = self.visitId(ast.cond, true_c, True)
        else: cond_type, _ = self.visit(ast.cond, true_c)

        if type(cond_type) is not BoolType:
            raise TypeMismatch(ast)

        self.visit(ast.upda, true_c)        
            
        self.visit(ast.loop, true_c)

        return c

    # class ForEach(Stmt): idx:Id
    #                      value:Id
    #                      arr:Expr
    #                      loop:Block
    def visitForEach(self,ast,c):

        if type(ast.arr) is FuncCall:
            arr_type, _ = self.visitFuncCall(ast.arr, c, True)
        elif type(ast.arr) is MethCall:
            arr_type, _ = self.visitMethCall(ast.arr, c, True)
        elif type(ast.arr) is Id:
            arr_type, _ = self.visitId(ast.arr, c, True)
        else: arr_type, _ = self.visit(ast.arr, c)

        if ast.idx.name != "_":
            idx_type, _ = self.visitId(ast.idx, c, True)
            if type(idx_type) is not IntType:
                raise TypeMismatch(ast)
        
        if type(arr_type) is not ArrayType:
            raise TypeMismatch(ast)
        dimens_of_arrtype = arr_type.dimens[1:] if len(arr_type.dimens) > 1 else arr_type.eleType

        val_type, _ = self.visitId(ast.value, c, True)

        if type(val_type) is ArrayType:
            if type(val_type.eleType) is not type(arr_type.eleType) or ((type(val_type.eleType) is StructMType or type(val_type.eleType) is InterfaceType) and val_type.eleType.name != arr_type.eleType.name):
                raise TypeMismatch(ast)
            if type(val_type.dimens) is not type(dimens_of_arrtype) or val_type.dimens != dimens_of_arrtype:
                raise TypeMismatch(ast)
        elif type(val_type) is not type(arr_type.eleType):
            raise TypeMismatch(ast)
        elif (type(val_type) is StructMType or type(val_type) is InterfaceType) and val_type.name != arr_type.eleType.name:
            raise TypeMismatch(ast)
        
        self.visit(ast.loop, [[]] + c)
        
        return c

    def visitBreak(self,ast,c):pass

    def visitContinue(self,ast,c):pass

    # class Return(Stmt): expr:Expr # None if there is no expr
    def visitReturn(self,ast,c):
        if ast.expr:
            if type(ast.expr) is FuncCall:
                expr_type, _ = self.visitFuncCall(ast.expr, c, True)
            elif type(ast.expr) is MethCall:
                expr_type, _ = self.visitMethCall(ast.expr, c, True)
            elif type(ast.expr) is Id:
                expr_type, _ = self.visitId(ast.expr, c, True)
            else: expr_type, _ = self.visit(ast.expr, c)
        else: expr_type = VoidType()

        flatten_c = [symbol for scope in c for symbol in scope]
        func = next(filter(lambda x: x.kind == DeclKind.FUNCTION or x.kind == DeclKind.METHOD, flatten_c), False)

        func.val = [(ast, expr_type)] if func.val is None else func.val + [(ast, expr_type)]

        return c


    # class Id(Type,LHS): name : str
    def visitId(self,ast,c, get_var = False):

        flatten_res = [symbol for scope in c for symbol in scope]  # flatten
        if get_var:
            res = next(filter(lambda sym: (sym.kind == DeclKind.VARIABLE or sym.kind == DeclKind.CONSTANT or sym.kind == DeclKind.PARAMETER) and (sym.name == ast.name), flatten_res), False)
        else: 
            res = next(filter(lambda sym: (sym.kind == DeclKind.STRUCT or sym.kind == DeclKind.INTERFACE) and (sym.name == ast.name), flatten_res), False)
        
        if not res: raise Undeclared(Identifier(), ast.name)

        return res.mtype, res.val

    # class ArrayCell(LHS): arr:Expr
    #                       idx:List[Expr]
    def visitArrayCell(self,ast,c):
        if type(ast.arr) is FuncCall:
            arr_type, _ = self.visitFuncCall(ast.arr, c, True)
        elif type(ast.arr) is MethCall:
            arr_type, _ = self.visitMethCall(ast.arr, c, True)
        elif type(ast.arr) is Id:
            arr_type, _ = self.visitId(ast.arr, c, True)
        else: arr_type, _ = self.visit(ast.arr, c)

        if type(arr_type) is not ArrayType:
            raise TypeMismatch(ast)
        
        for idx in ast.idx:
            if type(idx) is FuncCall:
                idx_type, _ = self.visitFuncCall(idx, c, True)
            elif type(idx) is MethCall:
                idx_type, _ = self.visitMethCall(idx, c, True)
            elif type(idx) is Id:
                idx_type, _ = self.visitId(idx, c, True)
            else: idx_type, _ = self.visit(idx, c)
            if type(idx_type) is not IntType:
                raise TypeMismatch(ast)

        rettype = ArrayType(arr_type.dimens[len(ast.idx):], arr_type.eleType) if len(arr_type.dimens) > len(ast.idx) else arr_type.eleType

        return rettype, None

    # class FieldAccess(LHS): receiver:Expr
    #                         field:str
    def visitFieldAccess(self,ast,c):
        if type(ast.receiver) is FuncCall:
            rec_type, _ = self.visitFuncCall(ast.receiver, c, True)
        elif type(ast.receiver) is MethCall:
            rec_type, _ = self.visitMethCall(ast.receiver, c, True)
        elif type(ast.receiver) is Id:
            rec_type, _ = self.visitId(ast.receiver, c, True)
        else: rec_type, _ = self.visit(ast.receiver, c)

        if type(rec_type) is not StructMType:
            raise TypeMismatch(ast)

        if type(rec_type) is InterfaceType:
            raise Undeclared(Field(), ast.field)
        else:
            list_fieldName = list(map(lambda x: x[0], rec_type.elements))
            if ast.field not in list_fieldName:
                raise Undeclared(Field(), ast.field)
        res = next(filter(lambda x: x[0] == ast.field, rec_type.elements), False)
        if type(res[1]) is not Id:
            res_type = self.visit(res[1], c)
        else: res_type, _ = self.visit(res[1], c)

        return res_type, None

    def eval_binop(self, op, left_val, right_val):
        if left_val is None or right_val is None:
            return None
        if op == "+":
            return left_val + right_val
        elif op == "-":
            return left_val - right_val
        elif op == "*":
            return left_val * right_val
        elif op == "/":
            if isinstance(left_val, int) and isinstance(right_val, int):
                return left_val // right_val
            return left_val / right_val
        elif op == "%":
            return left_val % right_val
        elif op == "==":
            return left_val == right_val
        elif op == "!=":
            return left_val != right_val
        elif op == "<":
            return left_val < right_val
        elif op == "<=":
            return left_val <= right_val
        elif op == ">":
            return left_val > right_val
        elif op == ">=":
            return left_val >= right_val
        elif op == "&&":
            return left_val and right_val
        elif op == "||":
            return left_val or right_val

    # class BinaryOp(Expr): op:str
    #                       left:Expr
    #                       right:Expr
    def visitBinaryOp(self,ast,c):
        if type(ast.left) is FuncCall:
            left_type, left_val = self.visitFuncCall(ast.left, c, True)
        elif type(ast.left) is MethCall:
            left_type, left_val = self.visitMethCall(ast.left, c, True)
        elif type(ast.left) is Id:
            left_type, left_val = self.visitId(ast.left, c, True)
        else: left_type, left_val = self.visit(ast.left, c)

        if type(ast.right) is FuncCall:
            right_type, right_val = self.visitFuncCall(ast.right, c, True)
        elif type(ast.right) is MethCall:
            right_type, right_val = self.visitMethCall(ast.right, c, True)
        elif type(ast.right) is Id:
            right_type, right_val = self.visitId(ast.right, c, True)
        else: right_type, right_val = self.visit(ast.right, c)

        if ast.op == '+':
            if type(left_type) is StringType and type(right_type) is StringType:
                return StringType(), self.eval_binop(ast.op, left_val, right_val)
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType(), self.eval_binop(ast.op, left_val, right_val)
            if type(left_type) is FloatType and type(right_type) is FloatType:
                return FloatType(), self.eval_binop(ast.op, left_val, right_val)
            if (type(left_type) is IntType and type(right_type) is FloatType) or (type(left_type) is FloatType and type(right_type) is IntType):
                return FloatType(), self.eval_binop(ast.op, left_val, right_val)
        if ast.op in ["-", "*", "/"]:
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType(), self.eval_binop(ast.op, left_val, right_val)
            if type(left_type) is FloatType and type(right_type) is FloatType:
                return FloatType(), self.eval_binop(ast.op, left_val, right_val)
            if (type(left_type) is IntType and type(right_type) is FloatType) or (type(left_type) is FloatType and type(right_type) is IntType):
                return FloatType(), self.eval_binop(ast.op, left_val, right_val)
        if ast.op == '%':
            if type(left_type) is IntType and type(right_type) is IntType:
                return IntType(), self.eval_binop(ast.op, left_val, right_val)
        if ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if type(left_type) is StringType and type(right_type) is StringType:
                return BoolType(), self.eval_binop(ast.op, left_val, right_val)
            if type(left_type) is IntType and type(right_type) is IntType:
                return BoolType(), self.eval_binop(ast.op, left_val, right_val)
            if type(left_type) is FloatType and type(right_type) is FloatType:
                return BoolType(), self.eval_binop(ast.op, left_val, right_val)
        if ast.op in ["&&", "||"]:
            if type(left_type) is BoolType and type(right_type) is BoolType:
                return BoolType(), self.eval_binop(ast.op, left_val, right_val)
            
        raise TypeMismatch(ast)    

    # class UnaryOp(Expr): op:str
    #                      body:Expr
    def visitUnaryOp(self,ast,c):
        if type(ast.body) is FuncCall:
            typ, val = self.visitFuncCall(ast.body, c, True)
        elif type(ast.body) is MethCall:
            typ, val = self.visitMethCall(ast.body, c, True)
        elif type(ast.body) is Id:
            typ, val = self.visitId(ast.body, c, True)
        else: typ, val = self.visit(ast.body, c)

        if ast.op == '-':
            if type(typ) is IntType or type(typ) is FloatType:
                return typ, -val
        if ast.op == '!':
            if type(typ) is BoolType:
                return typ, not val
        raise TypeMismatch(ast)

    # class FuncCall(Expr,Stmt): funName:str
    #                            args:List[Expr] # [] if there is no arg
    def visitFuncCall(self,ast,c, in_expr = False):
        flatten_c = [symbol for scope in c for symbol in scope]
        res = next(filter(lambda sym: sym.name == ast.funName, flatten_c), False)
        if not res or res.kind != DeclKind.FUNCTION: raise Undeclared(Function(), ast.funName)

        list_param_type = []
        for param in res.mtype.partype:
            if type(param) is Id:
                param_type, _ = self.visit(param, c)
            else: param_type = self.visit(param, c)
            list_param_type.append(param_type)

        list_arg_type = []
        for arg in ast.args:
            if type(arg) is FuncCall:
                arg_type, _ = self.visitFuncCall(arg, c, True)
            elif type(arg) is MethCall:
                arg_type, _ = self.visitMethCall(arg, c, True)
            elif type(arg) is Id:
                arg_type, _ = self.visitId(arg, c, True)
            else: arg_type, _ = self.visit(arg, c)
            list_arg_type.append(arg_type)

        if len(list_param_type) != len(list_arg_type):
            raise TypeMismatch(ast)
        for i in range(len(list_param_type)):
            if type(list_param_type[i]) is not type(list_arg_type[i]):
                if (type(list_param_type[i]) is StructMType or type(list_param_type[i]) is InterfaceType) and type(list_arg_type[i]) is NilType:pass
                else: raise TypeMismatch(ast)
            elif type(list_param_type[i]) is ArrayType:
                if type(list_param_type[i].eleType) is not type(list_arg_type[i].eleType) or ((type(list_param_type[i].eleType) is StructMType or type(list_param_type[i].eleType) is InterfaceType) and list_param_type[i].eleType.name != list_arg_type[i].eleType.name):
                    raise TypeMismatch(ast)
                if type(list_param_type[i].dimens) is not type(list_arg_type[i].dimens) or list_param_type[i].dimens != list_arg_type[i].dimens:
                    raise TypeMismatch(ast)
            elif (type(list_param_type[i]) is StructMType or type(list_param_type[i]) is InterfaceType) and list_param_type[i].name != list_arg_type[i].name:
                raise TypeMismatch(ast)  

        if in_expr:
            if type(res.mtype.rettype) is VoidType:
                raise TypeMismatch(ast)
            return res.mtype.rettype, None
        else:
            if type(res.mtype.rettype) is not VoidType:
                raise TypeMismatch(ast)
            return c
        
    # class MethCall(Expr,Stmt): receiver:Expr
    #                            metName:str
    #                            args:List[Expr]
    def visitMethCall(self,ast,c, in_expr = False):
        if type(ast.receiver) is Id:
            rec_type, _ = self.visitId(ast.receiver, c, True)
        else: rec_type, _ = self.visit(ast.receiver, c)

        if type(rec_type) is not StructMType and type(rec_type) is not InterfaceType:
            raise TypeMismatch(ast)

        if type(rec_type) is InterfaceType:
            list_protName = list(map(lambda x: x.name, rec_type.methods))
            if ast.metName not in list_protName:
                raise Undeclared(Method(), ast.metName)
            
            cur_method = next(filter(lambda x: x.name == ast.metName, rec_type.methods), False)

            list_param = cur_method.params
            list_param_type = []
            for param in list_param:
                if type(param) is Id:
                    param_type, _ = self.visit(param, c)
                else: param_type = self.visit(param, c)
                list_param_type.append(param_type) 
                
            if type(cur_method.retType) is Id:
                rettype, _ = self.visit(cur_method.retType, c)
            else: rettype = self.visit(cur_method.retType, c)

        else:
            list_metName = list(map(lambda x: x[0], rec_type.methods))
            if ast.metName not in list_metName:
                raise Undeclared(Method(), ast.metName)
            cur_method = next(filter(lambda x: x[0] == ast.metName, rec_type.methods), False)
            list_param_type = []
            for param in cur_method[1].partype:
                if type(param) is Id:
                    param_type, _ = self.visit(param, c)
                else: param_type = self.visit(param, c)
                list_param_type.append(param_type)
            
            if type(cur_method[1].rettype) is Id:
                rettype, _ = self.visit(cur_method[1].rettype, c)
            else: rettype = self.visit(cur_method[1].rettype, c)

        
        list_arg_type = []
        for arg in ast.args:
            if type(arg) is FuncCall:
                arg_type, _ = self.visitFuncCall(arg, c, True)
            elif type(arg) is MethCall:
                arg_type, _ = self.visitMethCall(arg, c, True)
            elif type(arg) is Id:
                arg_type, _ = self.visitId(arg, c, True)
            else: arg_type, _ = self.visit(arg, c)
            list_arg_type.append(arg_type)
            
        if len(list_param_type) != len(list_arg_type):
            raise TypeMismatch(ast)
        for i in range(len(list_param_type)):
            if type(list_param_type[i]) is not type(list_arg_type[i]):
                if (type(list_param_type[i]) is StructMType or type(list_param_type[i]) is InterfaceType) and type(list_arg_type[i]) is NilType:pass
                else: raise TypeMismatch(ast)
            elif type(list_param_type[i]) is ArrayType:
                if type(list_param_type[i].eleType) is not type(list_arg_type[i].eleType) or ((type(list_param_type[i].eleType) is StructMType or type(list_param_type[i].eleType) is InterfaceType) and list_param_type[i].eleType.name != list_arg_type[i].eleType.name):
                    raise TypeMismatch(ast)
                if type(list_param_type[i].dimens) is not type(list_arg_type[i].dimens) or list_param_type[i].dimens != list_arg_type[i].dimens:
                    raise TypeMismatch(ast)
            elif (type(list_param_type[i]) is StructMType or type(list_param_type[i]) is InterfaceType) and list_param_type[i].name != list_arg_type[i].name:
                raise TypeMismatch(ast)

        if in_expr:
            if type(rettype) is VoidType:
                raise TypeMismatch(ast)
            return rettype, None
        else:   
            if type(rettype) is not VoidType:
                raise TypeMismatch(ast)
            return c
        

    # class IntLiteral(PrimLit): value:int
    def visitIntLiteral(self,ast,c):
        if type(ast.value) is str:
            s = ast.value
            if s.startswith(("0b", "0B")):
                val = int(s[2:], 2)
            elif s.startswith(("0o", "0O")):
                val = int(s[2:], 8)
            elif s.startswith(("0x", "0X")):
                val = int(s[2:], 16)
            else: val = int(s)
        else: val = ast.value
        return IntType(), val

    # class FloatLiteral(PrimLit): value:float
    def visitFloatLiteral(self,ast,c):
        ast.value = float(ast.value)
        return FloatType(), ast.value

    # class StringLiteral(PrimLit): value:str
    def visitStringLiteral(self,ast,c):
        ast.value = str(ast.value)
        return StringType(), ast.value


    # class BooleanLiteral(PrimLit): value:bool
    def visitBooleanLiteral(self,ast,c):
        ast.value = bool(ast.value)
        return BoolType(), ast.value

    def flatten_nested_list(self, nested):
        if isinstance(nested, list):
            result = []
            for item in nested:
                result.extend(self.flatten_nested_list(item))
            return result
        else:
            return [nested]

    
    # class ArrayLiteral(Literal): dimens:List[Expr]
    #                              eleType:Type
    #                              value:NestedList
    def visitArrayLiteral(self,ast,c):
        dimens_literal = []
        for dim in ast.dimens:
            if type(dim) is Id:
                _, dim_val = self.visitId(dim, c, True)
            else: _, dim_val = self.visit(dim, c)
            dimens_literal.append(IntLiteral(dim_val))

        if type(ast.eleType) is Id:
            ele_type, _ = self.visit(ast.eleType, c)
        else: ele_type = self.visit(ast.eleType, c)

        flat_list = self.flatten_nested_list(ast.value)
        for ele in flat_list:
            if type(ele) is FuncCall:
                self.visitFuncCall(ele, c, True)
            elif type(ele) is MethCall:
                self.visitMethCall(ele, c, True)
            elif type(ele) is Id:
                self.visitId(ele, c, True)
            else: self.visit(ele, c)

        return ArrayType(dimens_literal,ele_type), None

    # class StructLiteral(Literal): name:str
    #                               elements:List[Tuple[str,Expr]] # [] if there is no elements
    def visitStructLiteral(self,ast,c):
        res = self.get_symbol(ast.name, c[-1])
        if not res: raise Undeclared(Type(), ast.name)

        list_field_name = list(map(lambda x: x[0], res.mtype.elements))
        for ele in ast.elements:
            if ele[0] not in list_field_name:
                raise Undeclared(Field(), ele[0])
            elif type(ele[1]) is FuncCall:
                self.visitFuncCall(ele[1], c, True)
            elif type(ele[1]) is MethCall:
                self.visitMethCall(ele[1], c, True)
            elif type(ele[1]) is Id:
                self.visitId(ele[1], c, True)
            else: self.visit(ele[1], c)

        return res.mtype, None

    def visitNilLiteral(self,ast,c):
        return NilType(), None







