print ("Lista de tareas")


tasks = []

while True:
    print ("\n--- MENU ---")
    print ("1. Ver tareas")
    print ("2. Agregar tarea")
    print ("3. Eliminar tarea")
    print ("4. Salir")
    
    option = input("Selecciona una opcion del 1-4: ")
    
    if option == "1":
        if not tasks:
            print("La lista de tareas esta vacia")
    
        else: 
            print("\n Tus tareas:")
        for index,  task in enumerate(tasks, start=1):
            print (f"{index}. {task}")
            
    elif option == "2":
        new_task = input("Ingrese la nueva tarea: ").strip()
        if new_task:
            tasks.append(new_task)
            print(f"La nueva tarea {new_task} fue agregada con exito")
        else:
            print("No se puede agregar una tarea vacia")

    elif option == "3":
        if not tasks:
            print("No hay tareas que eliminar")
        else:
            print("\nTus tareas actuales")
            for index,task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_num = input("ingrese la tarea que desea eliminar: ")
            if task_num.isdigit():
                task_index = int(task_num) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Tarea {removed_task} Eliminada con exito")
                else:
                    print("Numero de tarea invalido")
            else:
                print("Ingrese una tarea valida")
    elif option == "4":
        print("Hasta luego")
        break
    else:
        print("ingrese un numero valido")