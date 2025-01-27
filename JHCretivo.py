import sys
#declaracion de clase
class pedido:
   def __init__(self,ropa,talla,tela,sublimaje):
      self.ropa = ropa
      self.talla = talla
      self.tela = tela
      self.sublimaje = sublimaje

class usuario:
   def __init__(self, nombre, sesionType):
    self.nombre = nombre
    self.sesionType = sesionType
    
pedidoN = pedido("camisa",45,"algodon","micro")

#Lista de objetos 
pedidos = []

#catalogo
tipoR = ["Camisa Chemise", "Franela", "Camiseta", "Jersey", "Camisa de Boton", "Sueter"]
talla = ["3-4", "5-6", "7-8", "9-11", "12-14", "14-15", "S", "M", "L", "XL", "XXL" ,"XXXL"]
tipoT = ["Atlética", "Micro-durazno", "Dry-Fit", "Terry-Spum", "Algodon", "Semi-Algodón"]
tipoS = ["Sublimación Minimalista", "Sublimación Completa", "Bordado", "Vinil Textil", "DTF"]

def inicio_sesion():
  usuarioN = usuario("", 0)
  password = ""
  print("Bienvenido, diganos su nombre por favor")
  usuarioN.nombre = input()

  print("eliga el tipo de sesión que desea iniciar")
  print("1: Cliente") 
  print("2: Administrador")
  print("3: Salir") 
  usuarioN.sesionType = int (input())

  while usuarioN.sesionType < 1 or usuarioN.sesionType > 3:
    print ("dato invalido, por favor eliga una de las opciones")
    usuarioN.sesionType = input()

  if usuarioN.sesionType == 1:
    print("Bienvenido, ha iniciado como cliente")

  elif usuarioN.sesionType == 2:
   print ("Ingrese la clave de administrador")  
   password = input()
   
   while password != "Administrador":
     print ("Contraseña incorrecta, intente de nuevo")
     password = input()
   print ("contraseña correcta, sesion iniciada como administrador")
  
  else:
   print("vuelva pronto!")
   sys.exit

inicio_sesion()
