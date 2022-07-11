import pymysql
import hashlib
import sys
from itertools import cycle
import re


class Database:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='Felipe@2003',
            db='empleados'
        )
        self.cursor=self.connection.cursor()

    def buscarEmplado(self,rut):#listo
        bandera = False
        query = "select count(rut) from empleados where rut='"+rut+"'"
        self.cursor.execute(query)
        empleados = self.cursor.fetchall()
        for x in empleados:
            cantidad = x[0]
            if cantidad > 0:
                bandera = True
        return bandera
    
    
    def es_correo_valido(self, correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, correo) is not None

    def validarRut(self,rut):
        rut = rut.upper()
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]

        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11

        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
        else:
            return False
#validacion de rut lista 
        
    
    
    
    def listarEmpleados(self):#listo
        try:
            query="Select*from empleados"
            self.cursor.execute(query)
            empleados=self.cursor.fetchall()
        except Exception as err:
            print(err)
        return empleados
    
    def listaSP(self):
        self.cursor.callproc("lmascotas")
        lista=self.cursor.fetchall()
        return lista

    def agregarUsuario(self,rut, nombre, apPat, apMat, cargo, area, direccion,telefono,cargas_familiares,ingreso_compania,sexo, liquidaciones, conEmengencia,correo,contrasena):#listo
        contrasena=hashlib.md5(contrasena.encode("utf-8")).hexdigest()
        query="insert into empleados(rut, nombre, apPat, apMat, cargo, area, direccion,telefono,cargas_familiares,ingreso_compania,sexo, liquidaciones, conEmengencia,correo,contrasena) values('"+rut+"','"+nombre+"','"+apPat+"','"+apMat+"','"+cargo+"','"+area+"','"+direccion+"','"+telefono+"','"+cargas_familiares+"','"+ingreso_compania+"','"+sexo+"','"+liquidaciones+"','"+conEmengencia+"','"+correo+"','"+contrasena+"')"
        self.cursor.execute(query)
        self.connection.commit()

    def login(self,correo,contrasena):#listo
        bandera=False
        password=hashlib.md5(contrasena.encode("utf-8")).hexdigest()
        query="select * from empleados where correo='"+correo+"'"
        self.cursor.execute(query)
        empleado=self.cursor.fetchall()
        for x in empleado:
            correoBD=x[13]
            claveBD=x[14]
            if claveBD==password:
                bandera=True
        return bandera