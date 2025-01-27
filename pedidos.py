def calcular_precio(tipo_de_ropa, tipo_de_tela, tecnica_de_sublimacion, diseno):
    # Definir precios base según tipo de ropa
    precios_base_ropa = {1: 10, 2: 20, 3: 25, 4: 10, 5: 10, 6: 5}
    precio_base_ropa = precios_base_ropa.get(tipo_de_ropa, 0)

    # Definir precios según tipo de tela
    precios_tela = {1: 2, 2: 3, 3: 5, 4: 5, 5: 4, 6: 5, 7: 3, 8: 3}
    precio_tela = precios_tela.get(tipo_de_tela, 0)

    # Definir precios según técnica de sublimación
    precios_sublimacion = {0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 2}
    precio_sublimacion = precios_sublimacion.get(tecnica_de_sublimacion, 0)

    # Calcular precio total
    precio_total = precio_base_ropa + precio_tela + precio_sublimacion + (3 if diseno == 2 else 0)  # Precio del diseño propio es estándar ($3)
    return precio_total

def procedimiento_pedidos():
    pedidos = []
    i = 0

    while True:
        print("Bienvenidos a nuestro sistema de pedidos personalizados")
        print("Por favor, ingrese la opción de su preferencia")
        print("1: Realizar pedido")
        print("2: Salir")
        menu = int(input("Ingrese su opción: "))
        while menu < 1 or menu > 2:
            print("Error, debe ingresar una de las opciones")
            menu = int(input("Ingrese su opción: "))

        if menu == 1:
            pedido = {}
            print("Seleccione el tipo de ropa")
            print("1: Chemise")
            print("2: Camisa de Botón")
            print("3: Suéter")
            print("4: Jersey")
            print("5: Franela")
            print("6: Camiseta")
            pedido['tipo_de_ropa'] = int(input("Ingrese su opción: "))

            while pedido['tipo_de_ropa'] < 1 or pedido['tipo_de_ropa'] > 6:
                print("Error de datos ingresados, ingrese nuevamente")
                pedido['tipo_de_ropa'] = int(input("Ingrese su opción: "))

            print("Seleccione la talla (3-4, 5-6, 7-8, 9-11, 12-14, 14-15, S, M, L, XL, XXL, XXXL)")
            pedido['talla'] = input("Ingrese su opción: ")

            tallas_validas = ["3-4", "5-6", "7-8", "9-11", "12-14", "14-15", "S", "M", "L", "XL", "XXL", "XXXL"]
            while pedido['talla'] not in tallas_validas:
                print("Error de datos ingresados, ingrese nuevamente")
                pedido['talla'] = input("Ingrese su opción: ")

            print("Seleccione el color")
            colores_validos = ["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco", "Gris", "Naranja", "Rosa", "Morado"]
            for idx, color in enumerate(colores_validos, 1):
                print(f"{idx}: {color}")
            color = int(input("Ingrese su opción: "))
            while color < 1 or color > len(colores_validos):
                print("Error de datos ingresados, ingrese nuevamente")
                color = int(input("Ingrese su opción: "))
            pedido['color'] = colores_validos[color - 1]

            print("Seleccione el tipo de tela")
            print("1: Atlética")
            print("2: Micro-durazno")
            print("3: Dry-Fit")
            print("4: Terry-Spun")
            print("5: Manchester")
            print("6: Algodón")
            print("7: Semi-Algodón")
            print("8: Tela de Mono")
            pedido['tipo_de_tela'] = int(input("Ingrese su opción: "))

            while pedido['tipo_de_tela'] < 1 or pedido['tipo_de_tela'] > 8:
                print("Error de datos ingresados, ingrese nuevamente")
                pedido['tipo_de_tela'] = int(input("Ingrese su opción: "))

            print("Seleccione la técnica de sublimación")
            print("0: Ninguna")
            print("1: Sublimación Minimalista")
            print("2: Sublimación Completa")
            print("3: Bordado")
            print("4: Vinil Textil")
            print("5: DTF")
        
            pedido['tecnica_de_sublimacion'] = int(input("Ingrese su opción: "))

            while pedido['tecnica_de_sublimacion'] < 0 or pedido['tecnica_de_sublimacion'] > 5:
                print("Error de datos ingresados, ingrese nuevamente")
                pedido['tecnica_de_sublimacion'] = int(input("Ingrese su opción: "))

            if pedido['tecnica_de_sublimacion'] == 0:
                pedido['diseno'] = 0
                pedido['diseno_existente'] = None
                pedido['diseno_propio'] = None
            else:
                print("¿Desea realizar un diseño?")
                print("1: Sí")
                print("2: No")
                realizar_diseno = int(input("Ingrese su opción: "))

                while realizar_diseno < 1 or realizar_diseno > 2:
                    print("Error de datos ingresados, ingrese nuevamente")
                    realizar_diseno = int(input("Ingrese su opción: "))

                if realizar_diseno == 2:
                    pedido['diseno'] = 2  # Opción para diseño propio
                    pedido['diseno_propio'] = "Sin diseño"
                else:
                    print("Seleccione el diseño")
                    print("1: Elegir un diseño existente")
                    print("2: Realizar un diseño propio")
                    pedido['diseno'] = int(input("Ingrese su opción: "))

                    while pedido['diseno'] < 1 or pedido['diseno'] > 2:
                        print("Error de datos ingresados, ingrese nuevamente")
                        pedido['diseno'] = int(input("Ingrese su opción: "))

                    if pedido['diseno'] == 1:
                        print("Seleccione el diseño existente")
                        print("1: Camisa de Goku UI")
                        print("2: Camisa de Naruto")
                        print("3: Camisa de Grand Theft Auto")
                        print("4: Camisa para el Gym blanca")
                        print("5: Camisa de The Weeknd")
                        print("6: Camisa de Breaking Bad")
                        print("7: Camisa de Messi")
                        print("8: Camisa de CR7")
                        print("9: Camisa de Spiderman")
                        print("10: Camisa de Nissan Skyline R34")
                        print("11: Camisa de Toyota Supra MK4")
                        print("12: Camisa de Lightning McQueen")
                        print("13: Camisa de Porsche GT3 RS")
                        print("14: Camisa de Gojo Saturo")
                        print("15: Camisa de Kakashi")
                        print("16: Camisa de Luffy")
                        print("17: Camisa de Blue Lock")
                        print("18: Camisa de Nicki Nicole")
                        print("19: Camisa de Billie Eilish")
                        dis_existente = int(input("Ingrese su opción: "))

                        while dis_existente < 1 or dis_existente > 19:
                            print("Error de datos ingresados, intente nuevamente")
                            dis_existente = int(input("Ingrese su opción: "))
                        pedido['diseno_existente'] = dis_existente
                    else:
                        pedido['diseno_propio'] = input("Ingrese el diseño propio: ")

            print("Ingrese su Ubicación:")
            print("Ingrese su país")
            paises = [
                "Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia",
                "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Belarús",
                "Bélgica", "Belice", "Benín", "Bután", "Bolivia", "Bosnia y Herzegovina", "Brasil", "Brunei", "Bulgaria",
                "Burkina Faso", "Burundi", "Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China",
                "Chipre", "Colombia", "Congo, Rep. Dem.", "Congo, Rep.", "Corea del Norte", "Corea del Sur", "Costa de Marfil",
                "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto", "El Salvador", "Emiratos Árabes Unidos",
                "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Esuatini", "Etiopía", "Filipinas", "Finlandia",
                "Fiyi", "Francia", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guinea", "Guinea-Bisáu",
                "Guinea Ecuatorial", "Guyana", "Haití", "Honduras", "Hungría", "India", "Indonesia", "Irán", "Irlanda", "Islandia",
                "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kosovo",
                "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano", "Liberia", "Libia", "Lituania", "Luxemburgo", "Madagascar",
                "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco",
                "Mongolia", "Namibia", "Nauru", "Nepal", "Nicaragua", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Países Bajos",
                "Pakistán", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", "Reino Unido", "República Centroafricana",
                "República Checa", "República Dominicana", "Ruanda", "Rumania", "Rusia", "San Cristóbal y Nieves", "San Marino", "San Vicente y las Granadinas",
                "Santa Lucía", "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia",
                "Sri Lanka", "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania", "Tayikistán",
                "Timor-Leste", "Togo", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda",
                "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia"
            ]

            for idx, pais in enumerate(paises, 1):
                print(f"{idx}. {pais}")

            pais = new_func()
            while pais < 1 or pais > len(paises):
                print("Error de datos ingresados, ingrese nuevamente")
                pais = int(input("Ingrese su opción: "))
            pedido['pais'] = paises[pais - 1]

            estado = input("Ingrese su estado: ")

            if pedido['pais'] == "Venezuela":
                estados_venezuela = [
                    "Amazonas", "Anzoátegui", "Apure", "Aragua", "Barinas", "Bolívar", "Carabobo", "Cojedes", "Delta Amacuro",
                    "Distrito Capital", "Falcón", "Guárico", "Lara", "Mérida", "Miranda", "Monagas", "Nueva Esparta", "Portuguesa",
                    "Sucre", "Táchira", "Trujillo", "Vargas", "Yaracuy", "Zulia"
                ]
                while estado not in estados_venezuela:
                    print("Estado no encontrado, ingrese nuevamente")
                    estado = input("Ingrese su estado: ")
            pedido['estado'] = estado

            pedido['municipio'] = input("Ingrese su localidad o municipio: ")
        
            pedido['numero_de_casa'] = input("Ingrese número de casa: ")

            print("Seleccione el método de pago")
            print("1: Pago Móvil")
            print("2: Zelle")
            print("3: Visa")
            print("4: MasterCard")
            print("5: Paypal")
            metodo_de_pago = int(input("Ingrese su opción: "))

            while metodo_de_pago < 1 or metodo_de_pago > 5:
                print("Error de datos ingresados, ingrese nuevamente")
                metodo_de_pago = int(input("Ingrese su opción: "))
            pedido['metodo_de_pago'] = metodo_de_pago

            if metodo_de_pago == 1:
                print("Su pago móvil es:")
                print("Banco: Banesco")
                print("C.I: 32139656")
                print("TLF: 04121461867")
                ref = input("Por favor, anote los últimos 6 dígitos de la referencia: ")
                pedido['referencia'] = ref
            elif metodo_de_pago == 2:
                zelle = input("Ingrese los datos del Zelle: ")
                pedido['zelle'] = zelle
            elif metodo_de_pago == 3:
                print("Ingrese sus datos de Visa")
                vector_visa = [input(f"Ingrese el dígito {i + 1} de la tarjeta: ") for i in range(16)]
                ven_visa = input("Ingrese fecha de vencimiento: ")
                cvv_visa = input("Ingrese CVV: ")
                pedido['visa'] = {'numero': vector_visa, 'vencimiento': ven_visa, 'cvv': cvv_visa}
            elif metodo_de_pago == 4:
                print("Ingrese sus datos de MasterCard")
                vector_master = [input(f"Ingrese el dígito {i + 1} de la tarjeta: ") for i in range(16)]
                ven_master = input("Ingrese fecha de vencimiento: ")
                cvv_master = input("Ingrese CVV: ")
                pedido['mastercard'] = {'numero': vector_master, 'vencimiento': ven_master, 'cvv': cvv_master}
            elif metodo_de_pago == 5:
                correo_paypal = input("Ingrese el correo de Paypal, ejemplo correo@gmail.com: ")
                pedido['paypal'] = correo_paypal

            pedidos.append(pedido)

            precio_total = calcular_precio(pedido['tipo_de_ropa'], pedido['tipo_de_tela'], pedido['tecnica_de_sublimacion'], pedido['diseno'])
            print(f"El precio total del pedido es: ${precio_total}")
            confirmacion = int(input("¿Desea confirmar el pedido? (1: Sí, 2: No): "))

            if confirmacion == 1:
                print(f"Pedido confirmado. El monto a pagar es: ${precio_total}")
                print("Factura")
                print(f"Su tipo de ropa es: {pedido['tipo_de_ropa']}")
                print(f"Su tipo de talla: {pedido['talla']}")
                print(f"Su tipo de tela: {pedido['tipo_de_tela']}")
                print(f"Su técnica de sublimación es: {pedido['tecnica_de_sublimacion']}")
                print(f"Su diseño es: {pedido['diseno']}")
                print(f"Su monto total es: ${precio_total}")
                print(f"Su ubicación es: {pedido['pais']}, {pedido['estado']}, {pedido['municipio']}, número de casa: {pedido['numero_de_casa']}")
                print(f"Su método de pago es: {pedido['metodo_de_pago']}")
                print("Gracias por utilizar el sistema de pedidos de JhCreativo")
                print("¡Gracias por su compra, vuelva pronto!")
            else:
                print("Pedido cancelado.")

            i += 1

        elif menu == 2:
            print("Gracias por utilizar el sistema de pedidos de JhCreativo. ¡Vuelva pronto!")
            break

def new_func():
    pais = int(input("Ingrese su opción: "))
    return pais

# Ejecutar el procedimiento de pedidos
procedimiento_pedidos()