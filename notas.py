import json
import os

class notas:
    def __init__(self, fecha, titulo, contenido):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido

    def to_dict(self):
        return {
            "fecha": self.fecha,
            "titulo": self.titulo,
            "contenido": self.contenido
        }

class NotasBook:
    def __init__(self):
        self.notas = []

    def load_notas(self, filename="mis_notas.json"):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []
        return []
    
    
def main():
    libro = NotasBook()
    
    while True:
        option = input("\nSelecciona la opcion que desea realizar: \n1.Agregar tarea \n2.Mirar tarea \n3.Buscar \n4.Salir: ").strip()
        
        if option == "1":
            titulo = input("Titulo: ").strip()
            fecha = input("fecha: ").strip()
            contenido  = input("contenido: ").strip()
            
            
            if fecha and titulo:
                new_nota = notas(fecha, titulo, contenido)
                libro.add_notas(new_nota)
            else:
                print("Error: Fecha y titulo requerido")
                
                
        elif option == "2":
            libro.list_notas()
            
            
        elif option == "3":
                    query = input("Ingresa la tarea que desea buscar: ").strip()
                    libro.search_book(query)
                    
                    
        elif option == "4":
            print("Adios")
            break
        
        else:
            print("Realice una operacion valida")
            
if __name__ == "__main__":
    main()