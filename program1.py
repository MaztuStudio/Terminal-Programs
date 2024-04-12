tareas =["ejemplo"]
continuar = True

def agregar(desc):
    tareas.append(desc)
    print("\n")

def completar():
    count=1
    for i in tareas:
        print(f"  ({count}). {i}")
        count+=1
    print(f"{count}. Salir")
    ans = int(input("Que tarea?: "))
    if ans != count:
        tareas.pop(ans-1)
    
    print("\n")

def mostrar():
    count=1
    for i in tareas:
        print(f"  ({count}). {i}")
        count+=1
    print("\n")


while continuar:
    try:
        opcion =int(input("Menu:\n"
        "1. Agregar nueva tarea\n"
        "2. Marcar tarea como completada\n"
        "3. Mostrar tareas pendientes\n"
        "4. Salir\n"))

    except ValueError:
        print("Error: no es un numero")
        exit()

    match opcion:
        case 1:
            agregar(input("Describe la tarea: "))
        case 2:
            completar()
        case 3:
            mostrar()
        case 4:
            continuar=False
        case default:
            print("Esa Opcion no es Valida")
