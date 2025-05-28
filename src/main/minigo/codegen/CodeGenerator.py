'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Symbol():
    def __init__(self, name, mtype, value=None):
        #name: String
        #mtype: MType
        #value: Index or CName

        self.name = name
        self.mtype = mtype
        self.value = value if value is not None else CName("")

    def __str__(self):
        return f"Symbol(name={self.name}, mtype={self.mtype}, value={self.value})"

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.env = self.init()
        self.astTree = None
        self.path = None
        self.emit = None

    def init(self):
        mem = [[Symbol("getInt",MType([],IntType()),CName("io")),
                Symbol("putInt",MType([IntType()],VoidType()),CName("io")),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io")),
                Symbol("getFloat",MType([],FloatType()),CName("io")),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io")),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io")),
                Symbol("getBool",MType([],BoolType()),CName("io")),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io")),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io")),
                Symbol("getString",MType([],StringType()),CName("io")),
                Symbol("putString",MType([StringType()],VoidType()),CName("io")),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io")),
                Symbol("putLn",MType([],VoidType()),CName("io")),]]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def genDefaultValue(self, t, frame):
        if type(t) is IntType:
            return self.emit.emitPUSHICONST(0, frame)
        elif type(t) is FloatType:
            return self.emit.emitPUSHFCONST(0.0, frame)
        elif type(t) is BoolType:
            return self.emit.emitPUSHICONST(0, frame)
        elif type(t) is StringType:
            return self.emit.emitPUSHCONST("\"\"", StringType(), frame)
        else:
            return self.emit.emitPUSHNULL(frame)

    def emitObjectInit(self, list_field):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        for i in list_field:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
            self.emit.printout(self.genDefaultValue(i[1], frame))
            self.emit.printout(self.emit.emitPUTFIELD(self.className + "/" + i[0], i[1], frame)) 
     
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def emitObjectInitFull(self, list_field):
        frame = Frame("<init>", VoidType())
        local_env = SubBody(frame, [[]])
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([field[1] for field in list_field], VoidType()), False, frame))  
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        local_env.sym[0].append(Symbol("this", ClassType(self.className), CName(self.className)))
        for field in list_field:
            local_env.sym[0] += [self.visit(ParamDecl(field[0], field[1]), local_env)]

        for i, field in enumerate(list_field):
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitREADVAR(field[0], field[1], i+1, frame))
            self.emit.printout(self.emit.emitPUTFIELD(self.className + "/" + field[0], field[1], frame))
            

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def emitClassInit(self, list_decl, o):
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), False, frame))
        frame.enterScope(True)  
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for i in list_decl:
            if i.varInit:
                init_code, init_type = self.visit(i.varInit, Access(frame, o.sym, False, True))
                self.emit.printout(init_code)
                self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + i.varName, init_type, frame))
            else:
                init_code = self.genDefaultValue(i.varType, frame)
                self.emit.printout(init_code)
                self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + i.varName, i.varType, frame))
            
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast, c):
        env = SubBody(None, self.env)
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object", None))
        
        list_method = []
        list_struct = []
        list_var_const_decl = []
        list_func = []
        list_interface = []

        for i in ast.decl:
            if type(i) is FuncDecl:
                env.sym[0].append(Symbol(i.name, MType(list(map(lambda x: x.parType, i.params)), i.retType), CName(self.className)))
                list_func.append(i)
            elif type(i) is MethodDecl:
                list_method.append(i)
            elif type(i) is StructType:
                env.sym[0].append(Symbol(i.name, i, CName(i.name)))
                list_struct.append(i)
            elif type(i) is VarDecl or type(i) is ConstDecl:
                list_var_const_decl.append(i)
            elif type(i) is InterfaceType:
                env.sym[0].append(Symbol(i.name, i, CName(i.name)))
                list_interface.append(i)
                
        for s in list_struct:
            if s.methods == []:
                for meth in list_method:
                    if s.name == meth.recType.name:
                        s.methods.append(meth) 

        for i in list_var_const_decl:
            x = self.visit(i, env)
            env.sym[0].append(x)
        for i in list_func:
            self.visit(i, env)
        for i in list_interface:
            self.visit(i, env)
        for i in list_struct:
            self.visit(i, env)
                
        self.emitClassInit(list_var_const_decl, env)
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitStructType(self, ast, o):
        tmp_emit = self.emit
        tmp_className = self.className
        self.emit = Emitter(self.path + "/" + ast.name + ".j")
        self.className = ast.name
        if len(ast.implements) > 0:
            self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object", [x.name for x in ast.implements]))
        else:
            self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object", None))
        for field in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(field[0], field[1], False, False, None))
        self.emitObjectInit(ast.elements)
        self.emitObjectInitFull(ast.elements)
        for method in ast.methods:
            self.visitMethodDecl(method, o)
        self.emit.printout(self.emit.emitEPILOG())

        self.className = tmp_className
        self.emit = tmp_emit
        return Symbol(ast.name, ast, CName(ast.name))

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        o.frame = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, o.frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(o.frame.getNewIndex(), ast.receiver, ClassType(self.className), o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        o.sym[0].append(Symbol(ast.receiver, ClassType(self.className), Index(0)))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), o.frame))
        o.sym = [[]] + o.sym
        for i in ast.fun.params:
            o.sym[0].append(self.visit(i, o))
        self.visit(ast.fun.body,o)
        o.sym = [o.sym[-1]]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), o.frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(o.frame))
        o.frame.exitScope()

    def visitMethCall(self, ast, o):
        rec_code, rec_type = self.visit(ast.receiver, Access(o.frame, o.sym, False, True))
        if type(rec_type) is ClassType or type(rec_type) is Id:
            sym = next(filter(lambda x: x.name == rec_type.name, o.sym[-1]), None)
            sym_type = sym.mtype
        else:
            sym_type = rec_type.mtype

        
        if type(sym_type) is StructType:
            method_full = next(filter(lambda x: x.fun.name == ast.metName, sym_type.methods), None)
            mtype = MType(list(map(lambda x: x.parType, method_full.fun.params)), method_full.fun.retType)
            method_full = method_full.fun
        else:
            method_full = next(filter(lambda x: x.name == ast.metName, sym_type.methods), None)
            mtype = MType(method_full.params, method_full.retType)
        o.isLeft = False
        #Method call
        if type(method_full.retType) is VoidType:
            self.emit.printout(rec_code)
            [self.emit.printout(self.visit(x, Access(o.frame, o.sym, False, True))[0]) for x in ast.args]
            if type(sym_type) is StructType:
                self.emit.printout(self.emit.emitINVOKEVIRTUAL(f"{sym_type.name}/{ast.metName}", mtype, o.frame))
            else:
                self.emit.printout(self.emit.emitINVOKEINTERFACE(f"{sym_type.name}/{ast.metName}", mtype, len(mtype.partype) + 1, o.frame))
        #Method call in expression
        else:
            code = rec_code
            for x in ast.args:
                code += self.visit(x, o)[0]
            if type(sym_type) is StructType:
                code += self.emit.emitINVOKEVIRTUAL(f"{sym_type.name}/{ast.metName}",mtype, o.frame)
            else:
                code += self.emit.emitINVOKEINTERFACE(f"{sym_type.name}/{ast.metName}",mtype, len(mtype.partype) + 1, o.frame)
            
            return code, mtype.rettype

    def visitFieldAccess(self, ast, o):
        code = ""
        scode, styp = self.visit(ast.receiver, Access(o.frame, o.sym, False, True))
        struct = next(filter(lambda x: x.name == styp.name, o.sym[-1]), None)
        field = next(filter(lambda x: x[0] == ast.field, struct.mtype.elements), None)
        code = scode
        if not o.isLeft:
            code += self.emit.emitGETFIELD(struct.name + '/' + ast.field, field[1], o.frame)

        return code, field[1]

    def visitStructLiteral(self, ast, o):
        code = ""
        sym = next(filter(lambda x: x.name == ast.name, o.sym[-1]), None)
        code += self.emit.emitNEW(ast.name, o.frame)
        code += self.emit.emitDUP(o.frame)
        
        if len(ast.elements) == 0:
            code += self.emit.emitINVOKESPECIAL(o.frame, ast.name + "/<init>", MType([], VoidType()))
        else:
            list_value = []
            for original in sym.mtype.elements:
                for init in ast.elements:
                    if original[0] == init[0]:
                        list_value.append(init[1])
                        break
            for val in list_value:
                code += self.visit(val, Access(o.frame, o.sym, False, True))[0]
            code += self.emit.emitINVOKESPECIAL(o.frame, ast.name + "/<init>", MType([field[1] for field in sym.mtype.elements], VoidType()))

        return code, ClassType(ast.name)




    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        o.frame = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, o.frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), o.frame))
        o.sym = [[]] + o.sym
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), o.frame))
        else:
            for i in ast.params:
                o.sym[0].append(self.visit(i, o))
        self.visit(ast.body,o)
        o.sym = [o.sym[-1]]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), o.frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(o.frame))
        o.frame.exitScope()
        
    def visitReturn(self, ast, o):
        if ast.expr:
            code, type_ = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            
            self.emit.printout(code + self.emit.emitRETURN(type_, o.frame))

    
    def visitVarDecl(self, ast, o):
        if ast.varInit:                
            init_code, init_type = self.visit(ast.varInit, Access(Frame(ast.varName, ast.varType) if not o.frame else o.frame, o.sym, False, True))
        else:
            init_code = self.genDefaultValue(ast.varType, Frame(ast.varName, ast.varType) if not o.frame else o.frame)
            if type(ast.varType) is Id:
                ast.varType = ClassType(ast.varType.name)
            init_type = ast.varType

        if ast.varType is None:
            ast.varType = init_type

        if type(ast.varType) is Id:
            ast.varType = ClassType(ast.varType.name)

        if ((type(ast.varType) is ClassType or type(ast.varType) is InterfaceType or type(ast.varType) is Id) 
        and (type(init_type) is ClassType or type(init_type) is StructType or type(init_type) is Id)):
            left_sym = next(filter(lambda x: x.name == ast.varType.name, o.sym[-1]), None)
            right_sym = next(filter(lambda x: x.name == init_type.name, o.sym[-1]), None)
            left = left_sym.mtype
            right = right_sym.mtype
            if type(left) is InterfaceType and type(right) is StructType:
                list_implements_name = [x.name for x in right.implements]
                if left.name not in list_implements_name:
                    right.implements.append(left)
            
        if o.frame:
            new_idx = o.frame.getNewIndex()
            code = self.emit.emitVAR(new_idx, ast.varName, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
            idx = Index(new_idx)

            self.emit.printout(code)

            if type(ast.varType) is FloatType and type(init_type) is IntType:
                init_code += self.emit.emitI2F(o.frame)
            self.emit.printout(init_code)

            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, new_idx, o.frame)) 
        else:
            code = self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None)
            cname = CName(self.className)

            self.emit.printout(code)
        
        return Symbol(name = ast.varName, mtype = ast.varType, value = idx if o.frame else cname)
    
    def visitConstDecl(self, ast, o):
        init_code, init_type = self.visit(ast.iniExpr, Access(Frame(ast.conName, ast.conType) if not o.frame else o.frame, o.sym, False, True))

        if ast.conType is None:
            ast.conType = init_type

        if type(ast.conType) is Id:
            ast.conType = ClassType(ast.conType.name)

        if ((type(ast.conType) is ClassType or type(ast.conType) is InterfaceType or type(ast.conType) is Id) 
        and (type(init_type) is ClassType or type(init_type) is StructType or type(init_type) is Id)):
            left_sym = next(filter(lambda x: x.name == ast.conType.name, o.sym[-1]), None)
            right_sym = next(filter(lambda x: x.name == init_type.name, o.sym[-1]), None)
            left = left_sym.mtype
            right = right_sym.mtype
            if type(left) is InterfaceType and type(right) is StructType:
                list_implements_name = [x.name for x in right.implements]
                if left.name not in list_implements_name:
                    right.implements.append(left)

        if o.frame:
            new_idx = o.frame.getNewIndex()
            code = self.emit.emitVAR(new_idx, ast.conName, ast.conType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
            idx = Index(new_idx)

            self.emit.printout(code)

            if type(ast.conType) is FloatType and type(init_type) is IntType:
                init_code += self.emit.emitI2F(o.frame)
            self.emit.printout(init_code)

            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, new_idx, o.frame)) 
        else:
            code = self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, None)
            cname = CName(self.className)

            self.emit.printout(code)
        
        return Symbol(name = ast.conName, mtype = ast.conType, value = idx if o.frame else cname)
    
    def visitParamDecl(self, ast, o):
        new_idx = o.frame.getNewIndex()
        code = self.emit.emitVAR(new_idx, ast.parName, ast.parType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        idx = Index(new_idx)
        self.emit.printout(code)
        return Symbol(name = ast.parName, mtype = ast.parType, value = idx)
    
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, o.sym[-1]),None)
        o.isLeft = False
        #Function call
        if type(sym.mtype.rettype) is VoidType:
            [self.emit.printout(self.visit(x, Access(o.frame, o.sym, False, True))[0]) for x in ast.args]
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o.frame))
        #Function call in expression
        else:
            code = ""
            for x in ast.args:
                code += self.visit(x, o)[0]
                
            code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o.frame)
            return code, sym.mtype.rettype
   
    def visitBlock(self, ast, o):
        flag = False
        o.sym = [[]] + o.sym
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        for i in ast.member:
            if type(i) is Return: flag = True
            x = self.visit(i, o)
            if type(x) is Symbol: o.sym[0].append(x)
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.sym = o.sym[1:]
        o.frame.exitScope()
        return flag
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [sym for env in o.sym for sym in env]), None)
        if not o.isLeft:
            if type(sym.value) is Index:
                #emitREADVAR
                code = self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame)
            else:
                #emitGETSTATIC
                code = self.emit.emitGETSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
        else:
            if type(sym.value) is Index:
                #emitWRITEVAR
                code = self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame)
            else:
                #emitPUTSTATIC
                code = self.emit.emitPUTSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
        return code, sym.mtype

    def visitAssign(self, ast, o):
        if type(ast.lhs) is Id:
            sym = next(filter(lambda x: x.name == ast.lhs.name, [sym for env in o.sym for sym in env]), None)
            if not sym:
                implicit_decl = VarDecl(ast.lhs.name, None, ast.rhs)
                o.sym[0].append(self.visit(implicit_decl, o))
            else:
                right_code, right_type = self.visit(ast.rhs, Access(o.frame, o.sym, False, True))
                left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))

                if ((type(left_type) is ClassType or type(left_type) is InterfaceType or type(left_type) is Id) 
                and (type(right_type) is ClassType or type(right_type) is StructType or type(right_type) is Id)):
                    left_sym = next(filter(lambda x: x.name == left_type.name, o.sym[-1]), None)
                    right_sym = next(filter(lambda x: x.name == right_type.name, o.sym[-1]), None)
                    left = left_sym.mtype
                    right = right_sym.mtype
                    if type(left) is InterfaceType and type(right) is StructType:
                        list_implements_name = [x.name for x in right.implements]
                        if left.name not in list_implements_name:
                            right.implements.append(left)

                if type(left_type) is FloatType and type(right_type) is IntType:
                    right_code += self.emit.emitI2F(o.frame)
                self.emit.printout(right_code + left_code)

        elif type(ast.lhs) is ArrayCell:
            left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
            right_code, right_type = self.visit(ast.rhs, Access(o.frame, o.sym, False, True))

            if type(left_type) is FloatType and type(right_type) is IntType:
                right_code += self.emit.emitI2F(o.frame)
                
            self.emit.printout(left_code + right_code + self.emit.emitASTORE(left_type, o.frame))

        elif type(ast.lhs) is FieldAccess:
            left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
            right_code, right_type = self.visit(ast.rhs, Access(o.frame, o.sym, False, True))
            if type(left_type) is FloatType and type(right_type) is IntType:
                right_code += self.emit.emitI2F(o.frame)

            fake_frame = Frame("fake", VoidType())

            _, rec_type = self.visit(ast.lhs.receiver, Access(fake_frame, o.sym, False, True))
            
            self.emit.printout(left_code + right_code + self.emit.emitPUTFIELD(rec_type.name + "/" + ast.lhs.field, left_type, o.frame))
        else:
            right_code, right_type = self.visit(ast.rhs, Access(o.frame, o.sym, False, True))
            left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
            if type(left_type) is FloatType and type(right_type) is IntType:
                right_code += self.emit.emitI2F(o.frame)
            self.emit.printout(right_code + left_code)
        
    def visitIntLiteral(self, ast, o):
        code, typ = self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
        return code, typ
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(1 if ast.value == "true" else 0, o.frame), BoolType()
    
    def visitNilLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(o.frame), VoidType()
    
    def genOneDimArrayLiteral(self, ast, o):
        code = ""
        code += self.emit.emitPUSHICONST(len(ast.value), o.frame)
        code += self.emit.emitNEWARRAY(ast.eleType, o.frame)
        for i in range(len(ast.value)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            code += self.visit(ast.value[i], o)[0]
            code += self.emit.emitASTORE(ast.eleType, o.frame)
        return code, ArrayType(ast.dimens, ast.eleType)
        
    def genArrayLiteral(self, ast, o):
        code = ""
        if len(ast.value) != 0 and type(ast.value[0]) is list:
            code += self.emit.emitPUSHICONST(len(ast.value), o.frame)
            code += self.emit.emitNEWARRAY(ArrayType(ast.dimens[1:], ast.eleType), o.frame)
            for i in range(len(ast.value)):
                code += self.emit.emitDUP(o.frame)
                code += self.emit.emitPUSHICONST(i, o.frame)
                code += self.genArrayLiteral(ArrayLiteral(ast.dimens[1:], ast.eleType, ast.value[i]), o)[0]
                code += self.emit.emitASTORE(ArrayType(ast.dimens, ast.eleType), o.frame)
        else:
            code += self.genOneDimArrayLiteral(ast, o)[0]

        return code, ArrayType(ast.dimens, ast.eleType)
    
    def visitArrayLiteral(self, ast, o):
        return self.genArrayLiteral(ast, o)

    def visitArrayCell(self, ast, o):
        code, typ = self.visit(ast.arr, Access(o.frame, o.sym, False, True))

        *eles, last_ele = ast.idx
        for e in eles:
            ele_code, ele_typ = self.visit(e, Access(o.frame, o.sym, False, True))
            code += ele_code
            code += self.emit.emitALOAD(typ, o.frame)
        code += self.visit(last_ele, Access(o.frame, o.sym, False, True))[0]

        rtype = typ.eleType if len(ast.idx) == len(typ.dimens) else ArrayType(typ.dimens[len(ast.idx):], typ.eleType)
        if not o.isLeft:
            code += self.emit.emitALOAD(rtype, o.frame)

        return code, rtype
            
    def visitInterfaceType(self, ast, o):
        tmp_emit = self.emit
        tmp_className = self.className
        self.emit = Emitter(self.path + "/" + ast.name + ".j")
        self.className = ast.name
        self.emit.printout(self.emit.emitIPROLOG(self.className, "java.lang.Object"))

        for method in ast.methods:
            self.visit(method, o)
        self.emit.printout(self.emit.emitEPILOG())

        self.className = tmp_className
        self.emit = tmp_emit
        return Symbol(ast.name, ast, CName(ast.name))
    
    def visitPrototype(self, ast, o):
        self.emit.printout(self.emit.emitMETHOD(ast.name, MType(ast.params, ast.retType), False, o.frame, True))
        self.emit.printout(self.emit.emitIENDMETHOD(o.frame))

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        if type(e1t) is type(e2t):
            if type(e1t) is StringType:
                if type(ast.left) is StringLiteral and type(ast.right) is StringLiteral:
                    if ast.op == '+':
                        return self.visit(StringLiteral("\"" + ast.left.value[1:-1] + ast.right.value[1:-1] + "\""), o)
                    else:
                        return e1c + e2c + self.emit.emitREOP(ast.op, e1t, o.frame), BoolType()
                else:
                    if ast.op == '+':
                        code = e1c + e2c + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame)
                        return code, StringType()
                    else:
                        code = e1c + e2c + self.emit.emitREOP(ast.op, StringType(), o.frame)
                        return code, BoolType()
            else:
                rt = e1t
                
        elif type(e1t) is FloatType and type(e2t) is IntType:
            e2c += self.emit.emitI2F(o.frame)
            rt = e1t
        elif type(e1t) is IntType and type(e2t) is FloatType:
            e1c += self.emit.emitI2F(o.frame)
            rt = e2t
            
        if ast.op in ["+", "-"]:
            op = self.emit.emitADDOP(ast.op, rt, o.frame)
        elif ast.op == '*':
            op = self.emit.emitMULOP(ast.op, rt, o.frame)
        elif ast.op == '/':
            if type(rt) is IntType:
                e1c += self.emit.emitI2F(o.frame)
                e2c += self.emit.emitI2F(o.frame)
                rt = FloatType()
            op = self.emit.emitMULOP(ast.op, rt, o.frame)
        elif ast.op == '%':
            op = self.emit.emitMOD(o.frame)
        elif ast.op in ['>','<','>=','<=','!=','==']:
            op = self.emit.emitREOP(ast.op, e1t, o.frame)
            rt = BoolType()
        elif ast.op == '&&':
            op = self.emit.emitANDOP(o.frame)
        elif ast.op == '||':
            op = self.emit.emitOROP(o.frame)
            
        return e1c + e2c + op, rt
    
    def visitUnaryOp(self, ast, o):
        ec, et = self.visit(ast.body, o)
        if ast.op == '-':
            return ec + self.emit.emitNEGOP(et, o.frame), et
        else:
            return ec + self.emit.emitNOT(et, o.frame), BoolType()
        
    def visitIf(self, ast, o):
        if ast.elseStmt is None:
            fL = o.frame.getNewLabel()
            self.emit.printout(self.visit(ast.expr, Access(o.frame, o.sym, False, True))[0])
            self.emit.printout(self.emit.emitIFFALSE(fL, o.frame))
            self.visit(ast.thenStmt, o)
            self.emit.printout(self.emit.emitLABEL(fL, o.frame))
        else:
            fL = o.frame.getNewLabel()
            eL = o.frame.getNewLabel()
            self.emit.printout(self.visit(ast.expr, Access(o.frame, o.sym, False, True))[0])
            self.emit.printout(self.emit.emitIFFALSE(fL, o.frame))
            flag = self.visit(ast.thenStmt, o)
            if not flag:
                self.emit.printout(self.emit.emitGOTO(eL, o.frame))
            self.emit.printout(self.emit.emitLABEL(fL, o.frame))
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(eL, o.frame))

    def visitForBasic(self, ast, o):
        o.frame.enterLoop()
        cL = o.frame.getContinueLabel()
        bL = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(cL, o.frame))
        self.emit.printout(self.visit(ast.cond, Access(o.frame, o.sym, False, True))[0])
        self.emit.printout(self.emit.emitIFFALSE(bL, o.frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitGOTO(cL, o.frame))
        self.emit.printout(self.emit.emitLABEL(bL, o.frame))
        o.frame.exitLoop()

    def visitForStep(self, ast, o):
        o.frame.enterLoop()
        cL = o.frame.getContinueLabel()
        bL = o.frame.getBreakLabel()
        sL = o.frame.getNewLabel()
        if type(ast.init) is Assign:
            self.visit(ast.init, o)
        else:
            o.sym[0].append(self.visit(ast.init, o))
        self.emit.printout(self.emit.emitLABEL(sL, o.frame))
        self.emit.printout(self.visit(ast.cond, Access(o.frame, o.sym, False, True))[0])
        self.emit.printout(self.emit.emitIFFALSE(bL, o.frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(cL, o.frame))
        self.visit(ast.upda, o)
        self.emit.printout(self.emit.emitGOTO(sL, o.frame))
        self.emit.printout(self.emit.emitLABEL(bL, o.frame))
        o.frame.exitLoop()

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

        


    
