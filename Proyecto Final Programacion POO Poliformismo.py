

"""     FINAL DE PROGRAMACIÓN 1° AÑO DE DESARROLLO DE SOFTWARE Y PROGRAMACIÓN    """
"""      MARTÍN PEREZ  """



class school():                                   #Poliformismo
    def __init__(self,name):
        self.name=name
    def chores(self):
        pass
class teacher(school):
    def chores(self):
        print("Profe de matematica.")

class principal(school):
    def chores(self):
        print("Control de cursos.")

class kid(school):
    def chores(self):
        print("Estudiar")


def chores_type(person):
    person.chores()
    
myself = kid("Montoto")
chores_type(myself)