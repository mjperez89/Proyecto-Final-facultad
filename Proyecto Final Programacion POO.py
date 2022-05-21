

"""     FINAL DE PROGRAMACIÓN 1° AÑO DE DESARROLLO DE SOFTWARE Y PROGRAMACIÓN    """
"""      MARTÍN PEREZ  """


# Programacion Orientada a Objetos

class Students():    # Superclase
    def __init__(self):

        self.nationality = (input("Ingrese nacionalidad del alumno: ")).capitalize()     #atributo
        self.gender = (input("Ingrese genero del alumno: ")).capitalize()       #atributo
        self.height = float(input("Ingrese altura del alumno: "))      #atributo

    def enter_notes(self):  #Metodo
        self.notes = float(input("Ingrese la nota del alumno : "))
        list_notes = []
        list_notes.append(self.notes)
        print(list_notes)

    def enter_name(self):   #Metodo
        self.name = (input("Ingrese nombre del alumno : ")).capitalize()
        list_name = []
        list_name.append(self.name)
        print(list_name)

    def enter_age(self):   #Metodo
        self.age = int(input("Ingrese edad del alumno : "))
        list_age = []
        list_age.append(self.age)
        print(list_age)

    def dates(self):   #Metodo
        print("El nombre del estudiante es: ",self.name, "\ntiene la edad de :",self.age,"años","\ny su nota es : ",self.notes,"\nsu nacionalidad es : ",self.nationality,"\nsu genero es : ",self.gender,"\ny su altura es: ",self.height,"cms.")

class first_grade_students(Students):   #Subclase que hereda los metodos

    def study(self,study):   #Metodo Subclase
        self.study= study
        if (self.study) == True:
            return print("El Alumno si estudia")

        else:
            return print("El alumno no estudia")


student = Students()
student.enter_name()
student.enter_age()
student.enter_notes()
student.dates()

newStudent = first_grade_students()
newStudent.enter_name()
newStudent.enter_age()
newStudent.enter_notes()
newStudent.dates()
newStudent.study(False)



