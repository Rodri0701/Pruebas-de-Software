from typing import List

class ShoppingCart:

    def __init__(self) -> None:
        self.items: List[str] = []
    
    def add_item(self, item: str) -> int:
        if not item or any(char.isdigit() for char in item) or item in self.items or ' ' in item:
            if not item:
                #raise ValueError("Debe ingresar algun dato")
                print ("Debe ingresar algun dato")
            if any(char.isdigit() for char in item): 
                #raise ValueError("El producto ingresado no debe tener numeros")
                print ("El producto ingresado no debe tener numeros")
            if item in self.items: 
                #raise ValueError("El producto ya existe en el carrito")
                print ("El producto ya existe")
            if ' ' in item:
                #raise ValueError("El producto no puede contener espacios")
                print ("El producto no puede contener espacios")
        else:
            self.items.append(item)
            print ("El producto " + item + " se agrego correctamente")
            return self.size()

    def remove_item(self, item: str) -> None:
        if item not in self.items:
            #raise ValueError("El producto no existe")
            print ("EL producto no existe")
        else:
            self.items.remove(item)
            print (item+" a sido eliminado")

    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> list[str]:
        print (self.items)
        return self.items
    
cart = ShoppingCart()

#Test de ingreso de datos
cart.add_item("")
cart.add_item("orange")
cart.add_item("apple1")
cart.add_item("orange")
cart.get_items()
#test de eliminacion de datos
cart.remove_item("orange")
cart.get_items()
cart.remove_item("orange")