from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None,estudiantes=None):
        self._grupo = grupo
        if asignaturas==None:
            asignaturas=[]
        self._asignaturas = asignaturas
        if estudiantes==None:
            estudiantes=[]
        self.listadoAlumnos = estudiantes

    def getAsignaturas(self):
        return self._asignaturas
    
    def setAsignaturas(self,a):
        self._asignaturas=a

    def listadoAsignaturas(self, **kwargs):
        if self.getAsignaturas()==None:
            self.setAsignaturas([])
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
            lista=[]
        if self.listadoAlumnos==None:
            self.listadoAlumnos=[]
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        
    def getGrupo(self):
        return self._grupo

    def __str__(self):
        return "Grupo de estudiantes: "+self.getGrupo()

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
