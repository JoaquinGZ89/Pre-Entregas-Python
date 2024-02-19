class Cliente: #Defino clase cliente especificando atributos y metodos, cabe destacar que el carrito es un atributo 
    def __init__(self,nombre,apellido,carrito,edad,vip) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.carrito = carrito
        self.edad = edad
        self.vip = vip #Este campo indica con un booleano si el cliente es VIP o no
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"    

    def addcarrito(self, articulo):
        return self.carrito.agregar_articulo(articulo)

    def elimcarrito(self, articulo):
        return self.carrito.eliminar_articulo(articulo)

    def calcular_total(self):
        return self.carrito.calculartotal()

class ClienteVIP(Cliente): #Clase que deriva de cliente. Los clientes VIP disfrutan de descuentos exclusivos 
    def __init__(self, nombre, apellido, carrito, edad, vip, descuento) -> None:
        super().__init__(nombre, apellido, carrito, edad, vip)
        self.descuento = descuento #los descuentos se expresan en decimales ej 0.5 = 50% off
    
    def calcular_total(self):
        total = super().calcular_total()
        if self.vip:
            print(f"Total con descuento: ${total*self.descuento}")
            return total*self.descuento
        else:
            print(f"Total del carrito: ${total}")
            return total

class Carrito:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)
        print(f"{articulo} agregado al carrito con exito.")

    def eliminar_articulo(self, articulo):
        if articulo in self.articulos:
            self.articulos.remove(articulo)
            print(f"{articulo} eliminado del carrito con exito.")
        else:
            print(f"{articulo} no encontrado en el carrito.")

    def calculartotal(self):
        total = [articulo.precio for articulo in self.articulos]
        print(f"Total del carrito: ${total}")
        return sum(total)
    
    def __str__(self):
        if not self.articulos:
            return "Carrito vacío"
        else:
            return "\n".join(str(articulo) for articulo in self.articulos)


class Articulo:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return (f"Articulo: {self.nombre} precio: {self.precio}")


item1 = Articulo("Manzana", 100)
item2 = Articulo("Banana", 150)
car = Carrito()
car.agregar_articulo(item1)
car.agregar_articulo(item2)
print(car)


""" 
car = Carrito()
carvip = Carrito()
item1 = Articulo("Manzana", 100)
item2 = Articulo("Banana", 150)
clienteNormal = Cliente("Juan", "Perez", car, 22, False)
clientevp = ClienteVIP("Bruno", "Zago", carvip, 70, True, 0.5)

clienteNormal.addcarrito(item1)
clientevp.addcarrito(item1)

clienteNormal.calcular_total()
clientevp.calcular_total()
"""

print("Toma puto")