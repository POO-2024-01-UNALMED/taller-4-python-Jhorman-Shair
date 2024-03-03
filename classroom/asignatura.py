class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon
    
    def getSalon(self):
        return self._salon
        
    def getNombre(self):
        return self._nombre
    
    def __str__(self):
        return self.getNombre()+" "+self.getSalon()
