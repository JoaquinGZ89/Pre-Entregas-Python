"""
El sistema consta de 3 funciones ('registro', 'mostrar' y 'login') que se encargan de realizar las operaciones requeridas por el enunciado del trabajo
Por cuestiones de legibilidad y consigna, estas funciones estan contenidas en otra funcion principal llamada 'main'
Solamente hay que llamar a la funcion 'main' y esta se encarga de la simulacion completa ya que llama a las funciones dependiendo de lo que el usuario desee
Todas las funciones poseen como parametro una variable que tiene que ser del tipo diccionario para que funcione correctamente

"""
def registro(bdd):
  nuevo_archivo = open("BaseDeDatos.txt", "w")
  flag = True
  if type(bdd) != dict:
    flag = False
    print("Ingreso un parametro incorrecto. Ingrese un diccionario valido")
  while flag == True:
    try:
      usuario = input("Ingrese Usuario: ")
      password = input("Ingrese Contraseña: ")
      bdd[usuario] = password
      nuevo_archivo.write(str(usuario) + str(" ") + str(password) + "\n" )
      flag = bool(input("Si desea continuar ingrese un valor, de lo contrario deje la casilla en blanco: "))
    except Exception as e:
      print(f"Se produjo un error {type(e).__name__}")

def mostrar(bdd):
  if type(bdd) != dict:
    print("Ingreso un parametro incorrecto. Ingrese un diccionario valido")
  else:
    if not bdd:
      print("La base de datos está vacía.")
    else:
      print("La base de datos seleccionada contiene la siguiente informacion")
      print(bdd)

def login(bdd):
  user = input("Ingrese usuario a buscar: ")
  cont = input("Ingrese su contraseña: ")
  if user in bdd and bdd[user] == cont:
    print("La clave y el valor COINCIDEN con una entrada en el diccionario.")
  else:
    print("La clave y el valor NO COINCIDEN con ninguna entrada en el diccionario.")

def main(bdd):
  print("Bienvenido al sistema gestor de bases de datos")
  opcion = input(" Ingrese '1' para registrar nuevos datos \n Ingrese '2' para visualizar los datos \n Ingrese '3' para realizar un login \n Ingrese '4' para salir: \n Su opcion: " )
  flag = True
  while flag == True:
    if opcion == '1':
      registro(bdd)
      opcion = input(" Ingrese '1' para registrar nuevos datos \n Ingrese '2' para visualizar los datos \n Ingrese '3' para realizar un login \n Ingrese '4' para salir: \n Su opcion: " )
    elif opcion == '2':
      mostrar(bdd)
      opcion = input(" Ingrese '1' para registrar nuevos datos \n Ingrese '2' para visualizar los datos \n Ingrese '3' para realizar un login \n Ingrese '4' para salir: \n Su opcion: " )
    elif opcion =='3':
      login(bdd)
      opcion = input(" Ingrese '1' para registrar nuevos datos \n Ingrese '2' para visualizar los datos \n Ingrese '3' para realizar un login \n Ingrese '4' para salir: \n Su opcion: " )
    elif opcion =='4':
      flag = False
    else:
      print("Ocurrio un error, ingrese su opcion nuevamente")
      opcion = input(" Ingrese '1' para registrar nuevos datos \n Ingrese '2' para visualizar los datos \n Ingrese '3' para realizar un login \n Ingrese '4' para salir: \n Su opcion: " )

print("Segundo commit")
