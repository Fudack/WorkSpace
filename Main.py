from Database import Database
import os
db=Database()

try:

    def agregarUsuario():#listo
        rut=input("Ingrese el rut sin punto ni guion(*): ")
        validacion = db.validarRut(rut)
        while validacion == False:
            rut=input("Ingrese un rut valido(*): ")
            validacion=db.validarRut(rut)
        if db.buscarEmplado(rut):
            print("El rut del empleado ya existe en el sistema")
        else:
            correo=input("Ingrese Correo: ")
            bandera = db.es_correo_valido(correo)
            while bandera == False:
                correo = input("Ingrese Correo: ")
                bandera = db.es_correo_valido(correo)
            while len(correo) <8:
                correo = input("Ingrese Correo: ")
            nombre = str(input("Ingrese su primer nombre(*): "))
            while len(nombre) <0:
                nombre = input("Ingrese su primer nombre: ")
            apPat = str(input("Ingrese primer apellido: "))
            while len(apPat) <0:
                apPat = input("Ingrese ingrese el primer apellido: ")
            apMat = str(input("Ingrese segundo apellido: "))
            while len(apMat) <0:
                apMat = input("Ingrese segudo apellido: ")
            cargo = str(input("Ingrese cargo: "))
            while len(cargo) <0:
                cargo = input("Ingrese cargo: ")
            area = str(input("Ingrese area: "))
            while len(area) <0:
                area = input("Ingrese el area a la cual corresponde: ")
            direccion = input("Ingrese direccion: ")
            while len(direccion) <0:
                direccion = input("Ingrese Direccion: ")
            telefono = input("Ingrese telefono: ")
            while len(telefono) <0:
                telefono = input("Ingrese numero de telefono incluyendo el 9: ")
            cargas_familiares = input("Ingrese cargas familiares: ")
            while len(cargas_familiares) <0:
                cargas_familiares = input("Ingres cantidad de cargas familiares: ")
            ingreso_compania = input("Ingrese ingreso a la compañia (AA-MM-DD): ")
            while len(ingreso_compania) <0:
                ingreso_compania = input("Ingrese fecha de ingreso a la compañia (AA-MM-DD): ")
            sexo = str(input("Ingrese sexo: "))
            while len(sexo) <0:
                sexo = input("Ingrese sexo: ")
            liquidaciones = input("Ingrese liquidaciones: ")
            while len(liquidaciones) <0:
                liquidaciones = input("Ingrese liquidaciones: ")
            conEmengencia = input("Ingrese contacto de enmergencia: ")
            while len(conEmengencia) <0:
                conEmengencia = input("Ingrese un contacto de emergencia: ")
            contrasena = input("Ingese contraseña(*, +8): ")
            while len(contrasena) <0:
                contrasena = input("Ingrese debe poseer mas de 8 caracteres: ")
            db.agregarUsuario(rut, nombre, apPat, apMat, cargo, area, direccion,telefono,cargas_familiares,ingreso_compania,sexo, liquidaciones, conEmengencia,correo,contrasena)
            print("usuario agregado con exito")
    #agregarUsuario()#25443678
    def editarEmpleado(self):
        pass

    def login():#listo
        rut = input("Ingrese su Rut: ")
        bandera = db.validarRut(rut)
        while bandera == False:
            rut = input("Ingrese su Rut: ")
            bandera = db.validarRut(rut)
        correo=input("Ingrese Correo: ")
        bandera = db.es_correo_valido(correo)
        print(bandera)
        while bandera == False:
            correo = input("Ingrese Correo: ")
            bandera = db.es_correo_valido(correo)
        while len(correo) <8:
            correo = input("Ingrese Correo: ")
        if db.buscarEmplado(rut):
            contrasena=input("Ingese su contraseña: ")
            if db.login(correo,contrasena):
                print("acceso aprobado")
            else:
                print("acceso denegado")
        else:
            print("Correo inexistente")
                
    #login()

    def listarEmpleados(): 

        empleados=db.listarEmpleados()
        for m in empleados:

            print("rut-> {}".format(m[0]))
            print("-----------------------------")
            print("nombre-> {}".format(m[1]))
            print("-----------------------------")
            print("apellido paterno-> {}".format(m[2]))
            print("-----------------------------")
            print("apellido materno-> {}".format(m[3]))
            print("-----------------------------")
            print("cago-> {}".format(m[4]))
            print("-----------------------------")
            print("area-> {}".format(m[5]))
            print("-----------------------------")
            print("direccion-> {}".format(m[6]))
            print("-----------------------------")
            print("telefono-> {}".format(m[7]))
            print("-----------------------------")
            print("carga familiar-> {}".format(m[8]))
            print("-----------------------------")
            print("ingreso compañia-> {}".format(m[9]))
            print("-----------------------------")
            print("sexo-> {}".format(m[10]))
            print("-----------------------------")
            print("liquidaciones-> {}".format(m[11]))
            print("-----------------------------")
            print("contacto emergencia-> {}".format(m[12]))
            print("-----------------------------")
            print("correo-> {}".format(m[13]))
            print("-----------------------------")

    def listaFiltrada():
        print("hola")

    def Salir():
        os.system("clear")
        
    def menuRoot():
        respuesta="si"
        switch={1:listarEmpleados, 2:listaFiltrada, 3:agregarUsuario, 4:editarEmpleado, 5:Salir}

        while respuesta=="si":
            print("*****************************************")
            print("*    opcion 1: Lista de Empleados       *")
            print("*    opcion 2: Listado Filtrado         *")
            print("*    opcion 3: Agregar Empleados        *")
            print("*    opcion 4: Editar datos de Empleado *")
            print("*    opcion 5: Salir del sistema        *")
            print("*****************************************")
            x=int(input("Selecione su opcion \t"))
            switch.get(x,menuRoot)()
            respuesta=input("\n Desea continuar si/no \t")
            os.system("clear")
    menuRoot()
        
finally:

    pass