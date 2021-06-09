import json

def registro(registrados):
    registrar = True
    numero = False
    ######### Registro #########
    listaAuxiliar = []
    nombres = input("Ingrese su nombre completo: ")
    while not numero:
        try:
            identificación = eval(input("Ingrese su número de identificación: "))
            numero = True
        except:
            print("Ingrese una identificación valida.")
    usu = True
    while usu:
        try:
            tipoUsusario = input("¿Es usted...?: \n(1) Estudiante \n(2) Profesor \n(3) Personal administrativo\n")
            if eval(tipoUsusario) == 1 or eval(tipoUsusario) == 2 or eval(tipoUsusario) == 3 or eval(tipoUsusario) == 4:
                usu = False
            else:
                print("Ingrese uno de los numeros que se piden.")
        except:
            print("Ingrese uno de los numeros que se piden.")

    placa = input("Ingrese la placa de su vehículo: ")

    tip = True
    while tip:
        try:
            tipoVehículo = input("¿Su vehículo es: \n(1) automóvil \n(2) automóvil eléctrico \n(3) motocicleta \n(4) discapacitado\n")
            if int(tipoVehículo) == 1 or int(tipoVehículo) == 2 or int(tipoVehículo) == 3 or int(tipoVehículo) == 4:
                tip = False
            else:
                print("Ingrese uno de los numeros que se piden.")
        except:
            print("Ingrese uno de los numeros que se piden.")
    plan = True
    while plan:
        try:
            planPago = input("Ingrese su plan de pago: \n(1) mensual \n(2) diario\n")
            if int(planPago) == 1 or int(planPago) == 2:
                plan = False
        except:
            print("Ingrese uno de los numeros que se piden.")

    ######## Cambios #########  
    auxiliarTipoUsuario = {"1": "Estudiante", "2":"Profesor", "3":"Personal Administrativo", "4": "Visitante"}
    auxiliarTipoVehículo = {"1": "Automóvil", "2": "Automóvil eléctrico", "3": "Motocicleta", "4": "Discapacitado"}
    auxiliarPlanPago = {"1": "Mensual", "2": "Diario"}
    tipoUsusario = auxiliarTipoUsuario[tipoUsusario]
    tipoVehículo = auxiliarTipoVehículo[tipoVehículo]
    planPago = auxiliarPlanPago[planPago]

    ######## Comprobar repetidos #########
    for i in range(len(registrados["usuarios"])):
        if (identificación == registrados["usuarios"][i][1]):
            registrar = False
            print("Ese número de identificación ya está registrado.")
            break

    ######## Registrar #########
    if (registrar):
        listaAuxiliar.append(nombres)
        listaAuxiliar.append(identificación)
        listaAuxiliar.append(tipoUsusario)
        listaAuxiliar.append(placa)
        listaAuxiliar.append(tipoVehículo)
        listaAuxiliar.append(planPago)
        registrados["usuarios"].append(listaAuxiliar)
        print("¡Registrado correctamente!")
    return registrados

def ingresoVehículos(espaciosOcupados, registrados, espacios):
    registrado = False
    placa = input("Ingrese la placa de su vehículo: ")

    ######### Comprobación de registro #########
    for i in range(len(registrados["usuarios"])):
        if (placa == registrados["usuarios"][i][3]):
            registrado = True
            tipoVehículo = registrados["usuarios"][i][4]
            print("Vehículo ya registrado.")
            break
    
     ######### Registro automatico #########
    if(not(registrado)):
        listaAux = []
        tipo = True
        while tipo:
            try:
                tipoVehículo = input("Ingrese el tipo del vehículo \n(1) automóvil \n(2) automóvil eléctrico \n(3) motocicleta \n(4) discapacitado\n")
                if tipoVehículo == "1" or tipoVehículo == "2" or tipoVehículo == "3" or tipoVehículo == "4":
                    tipo = False
                else:
                    print("Ingrese uno de los numeros que se piden.")
            except:
                print("Ingrese uno de los numeros que se piden.")
        auxiliarTipoVehículo = {"1": "Automóvil", "2": "Automóvil eléctrico", "3": "Motocicleta", "4": "Discapacitado"}
        tipoVehículo = auxiliarTipoVehículo[tipoVehículo]
        listaAux.append("Visitante")
        listaAux.append("N/A")
        listaAux.append("N/A")
        listaAux.append(placa)
        listaAux.append(tipoVehículo)
        listaAux.append("Diario")
        registrados["usuarios"].append(listaAux)

        with open('usuarios.json', 'w', encoding="utf8") as file:
            json.dump(registrados, file, indent=4, ensure_ascii=False)

        print("¡Registrado temporalmente!")

    ######### Condiciones de aparcamiento #########
    espaciosPermitidos = {"Automóvil": [1], "Automóvil eléctrico": [1, 2], "Motocicleta": [3], "Discapacitado": [1, 4]}

     ######### Espacios disponibles #########
    for n in range (1, 7):
        nombrePiso = "Piso" + str(n)
        contador = 0
  
        print("Piso " + str(n))
        for fila in range (len(espacios[nombrePiso])):
            for columna in range (len(espacios[nombrePiso][fila])):
                if (espacios[nombrePiso][fila][columna] in espaciosPermitidos[tipoVehículo]) and (espaciosOcupados[nombrePiso][fila][columna] == "0"):
                    contador += 1

        print("Espacios disponibles: " + str(contador))
        print()
    ayudaCoor = 1
    piso = True
    while piso:
        try:
            pisoAParquear = eval(input("Ingrese el número del piso donde quiere parquear: "))
            if pisoAParquear == 1 or pisoAParquear == 2 or pisoAParquear == 3 or pisoAParquear == 4 or pisoAParquear == 5 or pisoAParquear == 6:
                piso = False
            else:
                print("Escoja uno de los pisos que se muestran.")
        except:
            print("Escoja uno de los pisos que se muestran.")
    for fila in range (len(espacios["Piso" + str(pisoAParquear)])):
        auxiliar = []
        for columna in range (len(espacios["Piso" + str(pisoAParquear)][fila])):
            if fila == 0 and columna == 0:
                print("  A    B    C    D    E    F    G    H    I    J")

            if espacios["Piso" + str(pisoAParquear)][fila][columna] in espaciosPermitidos[tipoVehículo] and (espaciosOcupados["Piso" + str(pisoAParquear)][fila][columna] == "0"):
                auxiliar.append("0")
            else:
                auxiliar.append("X")
            if columna == (len(espacios["Piso" + str(pisoAParquear)][fila]) - 1):
                print(str(auxiliar) + " " + str(ayudaCoor))
                ayudaCoor += 1

    repetir = True
    while repetir:
        fila = (int(input("Ingrese la fila donde desea ingresar el carro: ")))-1
        columna = input("Ingrese la columna donde desea ingresar el carro (En mayúscula): ")
        cambiaLetras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        columna = cambiaLetras[columna]
        if espacios["Piso" + str(pisoAParquear)][fila][columna] in espaciosPermitidos[tipoVehículo] and (espaciosOcupados["Piso" + str(pisoAParquear)][fila][columna] == "0"):
            espaciosOcupados["Piso" + str(pisoAParquear)][fila][columna] = placa

            repetir = False
        else:
            print("El espacio escogido no puede ser seleccionado.")

    with open("espaciosOcupados.json", "w",encoding="utf8") as file:
        json.dump(espaciosOcupados, file, indent=4, ensure_ascii=False)





    return registrados

def retirarVehículo():
    placasalida = input("Ingrese la placa de su vehiculo: ")
    horas = eval(input("¿Cuantas horas ha permanecido en el parqueadero?: "))
    for z in range (1,7):
        for j in range (len(espaciosOcupados["Piso" + str(z)])):
            for i in range(len(espaciosOcupados["Piso" + str(z)][j])):
                if (espaciosOcupados["Piso" + str(z)][j][i]) == placasalida:
                    x = True
                    if x == True:
                        if ("Mensualidad" == registrados["usuarios"][i][5]):    
                            print("El usuario no debe relizar ningun pago")
                         
                        elif ("Diario" == registrados["usuarios"][i][5]):
                            pagoestudiante = 1000
                            pagoprofesor = 2000
                            pagopersonaladm = 1500
                            pagovisitante = 3000
                            if (("Estudiante" == registrados["usuarios"][i][2])):
                                pago = pagoestudiante*horas
                            elif (("Profesor" == registrados["usuarios"][i][2])):
                                pago = pagoprofesor*horas
                            elif (("Personal Administrativo" == registrados["usuarios"][i][2])):
                                pago = pagopersonaladm*horas
                            elif("Visitante" == registrados["usuarios"][i][0]):
                                pago = pagovisitante*horas
                            print("El valor a pagar por el parqueadero es de " + str(pago))
                            espaciosOcupados["Piso" + str(z)][j][i] = "0"            
    if not x:
        print("No se encuentra esta placa en el estacionamiento")
    
    with open("espaciosOcupados.json", "w", encoding="utf8") as file:
        json.dump(espaciosOcupados, file, indent=4, ensure_ascii=False)
    return registrados

registar = True
archivo1 = open("tiposParqueaderos.json", "r+")
espacios = json.load(archivo1)
archivo2 = open("usuarios.json","r")
registrados = json.load(archivo2)
archivo3 = open("espaciosOcupados.json", "r+")
espaciosOcupados = json.load(archivo3)

opcionesMenú = input("Qué desea hacer? \n(1) Registrarse \n(2) Ingresar un vehículo \n(3) Sacar un vehículo \n(4) Generar estadisticas\n")

if (opcionesMenú == "1"):
    registrados = registro(registrados)
    with open('usuarios.json', 'w',encoding="utf8") as file:
        json.dump(registrados, file, indent=4)

elif (opcionesMenú == "2"):
    ingresoVehículos(espaciosOcupados, registrados, espacios)

elif (opcionesMenú == "3"):
    retirarVehículo()

elif (opcionesMenú == "4"):
    auto = 0
    elec = 0
    disc = 0
    moto = 0
    padm = 0
    estu = 0
    profe = 0
    invi = 0
    espacios_ocupados = 0
    total_espacios = 550
    total_1 = 100
    total_2 = 100
    total_3 = 100
    total_4 = 100
    total_5 = 100
    total_6 = 50
    espacios_piso1 = 0
    espacios_piso2 = 0
    espacios_piso3 = 0
    espacios_piso4 = 0
    espacios_piso5 = 0
    espacios_piso6 = 0


    for i in range (1, 7):
        for n in range (len(espaciosOcupados["Piso" + str(i)])):

            for m in range (len(espaciosOcupados["Piso" + str(i)][n])):
                if espaciosOcupados["Piso" + str(i)][n][m] != "0":
                    if i == 1:
                        espacios_piso1 += 1
                    elif i == 2:
                        espacios_piso2 += 1
                    elif i == 3:
                        espacios_piso3 += 1
                    elif i == 4:
                        espacios_piso4 += 1
                    elif i ==5:
                        espacios_piso5 += 1
                    elif i == 6:
                        espacios_piso6 += 1
                    espacios_ocupados += 1
                    for k in range (len(registrados["usuarios"])):
                        if espaciosOcupados["Piso" + str(i)][n][m] == registrados["usuarios"][k][3]:
                            if registrados["usuarios"][k][4] == "Automovil":
                                auto += 1
                            elif registrados["usuarios"][k][4] == "Automovil electrico":
                                elec += 1
                            elif registrados["usuarios"][k][4] == "Motocicleta":
                                moto += 1
                            elif registrados["usuarios"][k][4] == "Discapacitado":
                                disc += 1
                    for p in range (len(registrados["usuarios"])):
                        if espaciosOcupados["Piso" + str(i)][n][m] == registrados["usuarios"][p][3]:
                            if registrados["usuarios"][k][2] == "Personal Administrativo":
                                padm += 1
                            elif registrados["usuarios"][k][2] == "Estudiante":
                                estu += 1
                            elif registrados["usuarios"][k][2] == "Profesor":
                                profe += 1
                            elif registrados["usuarios"][k][2] == "Visitante" or registrados["usuarios"][k][2] == "N/A":
                                invi += 1

                    
    porcentajetotal = (espacios_ocupados/total_espacios)*100
    pp1 = (espacios_piso1/total_1)*100
    pp2 = (espacios_piso2/total_2)*100
    pp3 = (espacios_piso3/total_3)*100
    pp4 = (espacios_piso4/total_4)*100
    pp5 = (espacios_piso5/total_5)*100
    pp6 = (espacios_piso6/total_6)*100

    archivotxt = open("Estadisticas.txt", "w")
    archivotxt.write("Según el tipo de usuarios, se registró que por parte del personal administratrivo, entraron al estacionamiento " + str(padm)+ " vehículos.\n"+ 
    "Por parte de los estudiantes entraron al estacionamiento " + str(estu) + " vehículos.\n" + "Por parte de los profesores entraron al estacionamiento " + str(profe) + " vehículos.\n" + 
    "Por parte de los visitantes entraron al estacionamiento " + str(invi) + " vehículos.\n")
    archivotxt.write("\n")
    archivotxt.write("La cantidad de vehículos estacionados segun el tipo de vehículos es:\n" + "Para vehículos es de " + str(auto) + " carros.\n" + 
    "Para Automoviles Eléctricos es de " + str(elec) + " carros eléctricos.\n" + "Para motocicletas es de " + str(elec)+ " motos.\n" + 
    "Para discapacitados es de " + str(disc)+ " carros.\n")
    archivotxt.write("\n")
    archivotxt.write("El Porcentaje de ocupación total del parqueadero es de  " + str(porcentajetotal) + "%\n" + "Para el piso 1, el porcentaje de ocupación es de: "  + str(pp1) + "%\n" +
    "Para el piso 2 el porcentaje de ocupación es de: "  + str(pp2) + "%\n" + "Para el piso 3 el porcentaje de ocupación es de: "  + str(pp3) + "%\n" + 
    "Para el piso 4 el porcentaje de ocupación es de: "  + str(pp4) + "%\n"+ "Para el piso 5 el porcentaje de ocupación es de: "  + str(pp5) + "%\n" + 
    "Para el piso 6 es de " + str(pp6) + "%")
    archivotxt.close()
    print("Estadísticas generadas correctamente.")