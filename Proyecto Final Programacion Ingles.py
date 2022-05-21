import os

"""     FINAL DE PROGRAMACIÓN 1° AÑO DE DESARROLLO DE SOFTWARE Y PROGRAMACIÓN    """
"""      MARTÍN PEREZ  """
# Funcion para ingresar un nombre  (1)

def enter_name():
   
    while True:
        name = input(" Ingrese el nombre del estudiante : ")
        if name == "":
            print(" El nombre no puede estar vacio")
        else:
            return name.capitalize()

# Funcion para ingresar una edad

def enter_age():
    while True:
        ages = int(input(" Ingrese la edad del estudiante : "))
        if 0 <= ages <= 99 :
            return ages
        elif ages == "" :
            print(" La edad no puede estar vacia ")
        else:
            return ages

# Funcion para ingresar una nota

def enter_note():
    
    while True:
        try:
            note = float(input(" Ingrese la nota del estudiante (0-10): "))
            if 0 <= note <= 10:
                return note
            else:
                print(" La nota tiene que estar entre 0 y 10")
        except:
            print(" La nota tiene que ser un valor numerico")

# Funcion para buscar por nombre a un estudiante (2)

def search_students():
    
    while True:
        try:
            student_search = input(" Ingrese nombre del estudiante a buscar: ")
            if student_search == "":
                 print(" Ingrese un nombre ")
            else :
                return students.index(student_search.capitalize())
        except:
                print(" Por favor ingrese un alumno correcto, o el mismo no se encuentra en la lista")
                intent = input(" ¿Desea realizar otra busqueda ?: (S/N) : ").upper()
                if intent == "N":
                    break
                else:
                    continue

# Funcion para modificar la nota del estudiante  (3)

def modify_note():
    i = search_students()
    print (" La nota del " +str(students[i]) + " es de "+ str(notes[i]) )
    new_note = enter_note()
    notes[i] = new_note

    print(" La nota se cambio correctamente")

    print(" La nueva nota del alumno : " + str(students[i]) + "es de" + str(notes[i]))

# Funcion para ordenar alfabeticamente la lista de estudiantes.  (4)

def sort_by_name():
    if len(students) > 0:
        students.sort()
        for i in students:
            print(i)
    else:
        print(" La lista no contiene datos.")

#Funcion para ordenar la lista de notas de mayor a menor.   (5)

def sort_by_note():
    if len(notes) > 0 :
        for i in sorted(zip(students,notes), reverse=True):
            print(i)
    else:
        print(" La lista no contiene datos.")
            
# Funcion para mostrar el promedio de notas de los estudiantes  (6)

def average_notes(list_notes):
    
    if len(students) == 0:
        return -1
    return sum(list_notes)/len(list_notes)

# Funcion para borrar un estudiante con todos sus datos.  (7)

def delete_students():
    i = search_students()
    students.pop(i)
    notes.pop(i)
    ages.pop(i)

    print(" El alumno y datos se borraron correctamente. ")

# Funcion para calcular el promedio de edad de los estudiantes.  (8)

def average_ages(ages):
    if len(ages) > 0:
        return sum(ages) / len(ages)

def Menu():
    print("""-------------------------------------------------------
    Selecciona una opción...
    1 - Agregar estudiante
    2 - Buscar estudiante por nombre
    3 - Modificar nota
    4 - Listado ordenados por nombres
    5 - Listado ordenados por notas
    6 - Mostrar promedio de las notas
    7 - Borrar un estudiante
    8 - Calcular la edad promedio de los estudiantes
    0 - Salir""")

# --------------- Programa principal----------------------------
# definimos la lista que contendra una lista con cada estudiante

students = ["Emi","Sol","Martin"]
# definimos la lista que contendra las notas de cada estudiante

notes = [10.0,7.5,8]
# definimos la lista que contendra las edades de cada estudiante

ages = [25,21,33]

while True:
    Menu()
    try:
        option = int(input(" Ingrese el número de la opción escogida : "))
    except:
        option = -1
    if option == 1:
        students.append(enter_name())
        notes.append(enter_note())
        ages.append(enter_age())
        print(students)
        print(notes)
        print(ages)
        os.system("Pause")
    elif option == 2:
        try:
            index = search_students()
            print(f"El estudiante {students[index]}, tiene la edad de {ages[index]}, y su nota es {notes[index]}" )
            os.system("Pause")
        except:
            pass
    elif option == 3:
        try :
            modify_note()
            os.system("Pause")
        except:
            pass
    elif option == 4:
        try:
            sort_by_name()
            os.system("Pause")
        except:
            pass
    elif option == 5:
        try:
            sort_by_note()
            os.system("Pause")
        except:
            pass
    elif option == 6:
        average = round(average_notes(notes))
        print("El promedio de notas es de :", average)
        os.system("Pause")
    elif option == 7:
        try:
            delete_students()
            os.system("Pause")
        except:
            pass
    elif option == 8:
        try:
            ages_average = average_ages(ages)
            print(f"El promedio de edad de los Alumnos es de : {round(ages_average,2)}")
            os.system("Pause")
        except:
            print("erro")
    elif option == 0:
        break
    else:
        print(" La opción ingresada no es correcta, indica una opcióncorrecta ")
 