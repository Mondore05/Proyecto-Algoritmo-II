##################################################################
# Variables preestablecidas (pueden modificarse)
# Categorías de prendas precios
pchemise = 2
pboton = 2
psueter = 2
pjersie = 2
pcamiseta = 2
# Disponibilidad de prendas
dchemise = 15
dboton = 12
dsueter = 3
djersie = 7
dcamiseta = 10

# Categorias de telas precios
pmicrodurazno = 2
pdryfit = 1
pterryspum = 3
pmanchester = 2
palgodon = 2
psemi = 2
ptelamono = 3
# Disponibilidad de telas
dmicrodurazno = 15
ddryfit = 12
dterryspum = 3
dmanchester = 7
dalgodon = 10
dsemi = 5
dtelamono = 8

# Propiedades de las prendas, precios
pestampados = 1
pimagen = 2
ptexto = 1
# Disponibilidades de las propiedades
destampados = True
dimagen = True
dtexto = True



##################################################################
vmenup = 1
while vmenup == 1:
    print("Bienvenido al catálogo de productos")
    print("Inicie sesión como...")
    print("1. Administrador")
    print("2. Cliente")
    menu1 = int(input("Ingrese su opción: "))
    while menu1 != 1 and menu1 != 2:
        print("Opción inválida")
        menu1 = int(input("Ingrese su opción: "))

    if menu1 == 1:
        print("Ingrese la contraseña de administrador")
        password = input()
        while password != "admin":
            print("Contraseña incorrecta")
            password = input()
        vmenu1 = 1
        while vmenu1 == 1:
            print("Contraseña correcta")
            print("Bienvenido, administrador")
            print("¿Qué operación desea realizar?")
            print("1. Modificar el catálogo")
            print("2. Ver listado de productos")
            print("3. Salir")
            menu2 = int(input("Ingrese su opción: "))
            while menu2 != 1 and menu2 != 2 and menu2 != 3:
                print("Opción inválida")
                menu2 = int(input("Ingrese su opción: "))
            if menu2 == 1:
                vmenu2 = 1
                while vmenu2 == 1:
                    print("Seleccione la categoría a modificar")
                    print("1. Tipo de prenda")
                    print("2. Tipo de tela")
                    print("3. Propiedades de la prenda")
                    print("4. Volver")
                    menu3 = int(input("Ingrese su opción: "))
                    while menu3 != 1 and menu3 != 2 and menu3 != 3 and menu3 != 4:
                        print("Opción inválida")
                        menu3 = int(input("Ingrese su opción: "))
                    if menu3 == 1:
                        print("Seleccione el tipo de prenda a modificar")
                        print(f"1. Chemise - Precio: {pchemise} - Disponibilidad: {dchemise}")
                        print(f"2. Botón - Precio: {pboton} - Disponibilidad: {dboton}")
                        print(f"3. Suéter - Precio: {psueter} - Disponibilidad: {dsueter}")
                        print(f"4. Jersie - Precio: {pjersie} - Disponibilidad: {djersie}")
                        print(f"5. Camiseta - Precio: {pcamiseta} - Disponibilidad: {dcamiseta}")
                        menu4 = int(input("Ingrese su opción: "))
                        while menu4 != 1 and menu4 != 2 and menu4 != 3 and menu4 != 4 and menu4 != 5:
                            print("Opción inválida")
                            menu4 = int(input("Ingrese su opción: "))
                        if menu4 == 1:
                            print("Ingrese el nuevo precio de Chemise")
                            pchemise = int(input())
                            print("Ingrese la nueva disponibilidad de Chemise")
                            dchemise = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 2:
                            print("Ingrese el nuevo precio de Botón")
                            pboton = int(input())
                            print("Ingrese la nueva disponibilidad de Botón")
                            dboton = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 3:
                            print("Ingrese el nuevo precio de Suéter")
                            psueter = int(input())
                            print("Ingrese la nueva disponibilidad de Suéter")
                            dsueter = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 4:
                            print("Ingrese el nuevo precio de Jersie")
                            pjersie = int(input())
                            print("Ingrese la nueva disponibilidad de Jersie")
                            djersie = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 5:
                            print("Ingrese el nuevo precio de Camiseta")
                            pcamiseta = int(input())
                            print("Ingrese la nueva disponibilidad de Camiseta")
                            dcamiseta = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                    elif menu3 == 2:
                        print("Seleccione el tipo de tela a modificar")
                        print(f"1. Microdurazno - Precio: {pmicrodurazno} - Disponibilidad: {dmicrodurazno}")
                        print(f"2. Dryfit - Precio: {pdryfit} - Disponibilidad: {ddryfit}")
                        print(f"3. Terryspum - Precio: {pterryspum} - Disponibilidad: {dterryspum}")
                        print(f"4. Manchester - Precio: {pmanchester} - Disponibilidad: {dmanchester}")
                        print(f"5. Algodón - Precio: {palgodon} - Disponibilidad: {dalgodon}")
                        print(f"6. Semi - Precio: {psemi} - Disponibilidad: {dsemi}")
                        print(f"7. Tela mono - Precio: {ptelamono} - Disponibilidad: {dtelamono}")
                        menu4 = int(input("Ingrese su opción: "))
                        while menu4 != 1 and menu4 != 2 and menu4 != 3 and menu4 != 4 and menu4 != 5 and menu4 != 6 and menu4 != 7:
                            print("Opción inválida")
                            menu4 = int(input("Ingrese su opción: "))
                        if menu4 == 1:
                            print("Ingrese el nuevo precio de Microdurazno")
                            pmicrodurazno = int(input())
                            print("Ingrese la nueva disponibilidad de Microdurazno")
                            dmicrodurazno = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 2:
                            print("Ingrese el nuevo precio de Dryfit")
                            pdryfit = int(input())
                            print("Ingrese la nueva disponibilidad de Dryfit")
                            ddryfit = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 3:
                            print("Ingrese el nuevo precio de Terryspum")
                            pterryspum = int(input())
                            print("Ingrese la nueva disponibilidad de Terryspum")
                            dterryspum = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 4:
                            print("Ingrese el nuevo precio de Manchester")
                            pmanchester = int(input())
                            print("Ingrese la nueva disponibilidad de Manchester")
                            dmanchester = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 5:
                            print("Ingrese el nuevo precio de Algodón")
                            palgodon = int(input())
                            print("Ingrese la nueva disponibilidad de Algodón")
                            dalgodon = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 6:
                            print("Ingrese el nuevo precio de SemiAlgodon")
                            psemi = int(input())
                            print("Ingrese la nueva disponibilidad de SemiAlgodon")
                            dsemi = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 7:
                            print("Ingrese el nuevo precio de Tela mono")
                            ptelamono = int(input())
                            print("Ingrese la nueva disponibilidad de Tela mono")
                            dtelamono = int(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                    elif menu3 == 3:
                        print("Seleccione la propiedad a modificar")
                        print(f"1. Estampados - Precio: {pestampados} - Disponibilidad: {destampados}")
                        print(f"2. Imagen - Precio: {pimagen} - Disponibilidad: {dimagen}")
                        print(f"3. Texto - Precio: {ptexto} - Disponibilidad: {dtexto}")
                        menu4 = int(input("Ingrese su opción: "))
                        while menu4 != 1 and menu4 != 2 and menu4 != 3:
                            print("Opción inválida")
                            menu4 = int(input("Ingrese su opción: "))
                        if menu4 == 1:
                            print("Ingrese el nuevo precio de Estampados")
                            pestampados = int(input())
                            print("Ingrese la nueva disponibilidad de Estampados")
                            destampados = bool(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 2:
                            print("Ingrese el nuevo precio de Imagen")
                            pimagen = int(input())
                            print("Ingrese la nueva disponibilidad de Imagen")
                            dimagen = bool(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                        elif menu4 == 3:
                            print("Ingrese el nuevo precio de Texto")
                            ptexto = int(input())
                            print("Ingrese la nueva disponibilidad de Texto")
                            dtexto = bool(input())
                            print("Cambios realizados con éxito")
                            vmenu2 = 1
                    elif menu3 == 4:
                        vmenu2 = 0
                        vmenu1 = 1
            
            if menu2 == 2:
                    vmenu21 = 1
                    while vmenu21 == 1:
                        print("Seleccione categoría de productos")
                        print("1. Tipo de prenda")
                        print("2. Tipo de tela")
                        print("3. Propiedades de la prenda")
                        print("4. Volver")
                        menu21 = int(input("Ingrese su opción: "))
                        while menu21 != 1 and menu21 != 2 and menu21 != 3 and menu21 != 4:
                            print("Opción inválida")
                            menu21 = int(input("Ingrese su opción: "))
                        if menu21 == 1:
                            print(f"1. Chemise - Precio: {pchemise} - Disponibilidad: {dchemise}")
                            print(f"2. Botón - Precio: {pboton} - Disponibilidad: {dboton}")
                            print(f"3. Suéter - Precio: {psueter} - Disponibilidad: {dsueter}")
                            print(f"4. Jersie - Precio: {pjersie} - Disponibilidad: {djersie}")
                            print(f"5. Camiseta - Precio: {pcamiseta} - Disponibilidad: {dcamiseta}")
                            nada = input("Presione enter para continuar")
                            vmenu21 = 1
                        elif menu21 == 2:
                            print(f"1. Microdurazno - Precio: {pmicrodurazno} - Disponibilidad: {dmicrodurazno}")
                            print(f"2. Dryfit - Precio: {pdryfit} - Disponibilidad: {ddryfit}")
                            print(f"3. Terryspum - Precio: {pterryspum} - Disponibilidad: {dterryspum}")
                            print(f"4. Manchester - Precio: {pmanchester} - Disponibilidad: {dmanchester}")
                            print(f"5. Algodón - Precio: {palgodon} - Disponibilidad: {dalgodon}")
                            print(f"6. Semi - Precio: {psemi} - Disponibilidad: {dsemi}")
                            print(f"7. Tela mono - Precio: {ptelamono} - Disponibilidad: {dtelamono}")
                            nada = input("Presione enter para continuar")
                            vmenu21 = 1
                        elif menu21 == 3:
                            print(f"1. Estampados - Precio: {pestampados} - Disponibilidad: {destampados}")
                            print(f"2. Imagen - Precio: {pimagen} - Disponibilidad: {dimagen}")
                            print(f"3. Texto - Precio: {ptexto} - Disponibilidad: {dtexto}")
                            nada = input("Presione enter para continuar")
                            vmenu21 = 1
                        elif menu21 == 4:
                            vmenu21 = 0
                            vmenu1 = 1
            if menu2 == 3:
                vmenu1 = 0
                vmenup = 1
    if menu1 == 2:
        vmenuc = 1
        while vmenuc == 1:
            print("Bienvenido, cliente")
            print("Seleccione la categoría de productos que desea consultar")
            print("1. Tipo de prenda")
            print("2. Tipo de tela")
            print("3. Propiedades de la prenda")
            print("4. Volver")
            menu5 = int(input("Ingrese su opción: "))
            while menu5 != 1 and menu5 != 2 and menu5 != 3 and menu5 != 4:
                print("Opción inválida")
                menu5 = int(input("Ingrese su opción: "))
            if menu5 == 1:
                print(f"1. Chemise - Precio: {pchemise} - Disponibilidad: {dchemise}")
                print(f"2. Botón - Precio: {pboton} - Disponibilidad: {dboton}")
                print(f"3. Suéter - Precio: {psueter} - Disponibilidad: {dsueter}")
                print(f"4. Jersie - Precio: {pjersie} - Disponibilidad: {djersie}")
                print(f"5. Camiseta - Precio: {pcamiseta} - Disponibilidad: {dcamiseta}")
                nada = input("Presione enter para continuar")
            elif menu5 == 2:
                print(f"1. Microdurazno - Precio: {pmicrodurazno} - Disponibilidad: {dmicrodurazno}")
                print(f"2. Dryfit - Precio: {pdryfit} - Disponibilidad: {ddryfit}")
                print(f"3. Terryspum - Precio: {pterryspum} - Disponibilidad: {dterryspum}")
                print(f"4. Manchester - Precio: {pmanchester} - Disponibilidad: {dmanchester}")
                print(f"5. Algodón - Precio: {palgodon} - Disponibilidad: {dalgodon}")
                print(f"6. Semi - Precio: {psemi} - Disponibilidad: {dsemi}")
                print(f"7. Tela mono - Precio: {ptelamono} - Disponibilidad: {dtelamono}")
                nada = input("Presione enter para continuar")
            elif menu5 == 3:
                print(f"1. Estampados - Precio: {pestampados} - Disponibilidad: {destampados}")
                print(f"2. Imagen - Precio: {pimagen} - Disponibilidad: {dimagen}")
                print(f"3. Texto - Precio: {ptexto} - Disponibilidad: {dtexto}")
                nada = input("Presione enter para continuar")
            elif menu5 == 4:
                vmenuc = 0
                vmenup = 1

                    
