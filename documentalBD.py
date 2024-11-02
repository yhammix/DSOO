

class Documento():

    # f() __construct__ (paramId, paramConten)  
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else{}
        #≡
        #if contenido is not None:
        #    self.contenido = contenido
        #else:
        #    self.contenido = {}


    def obtener_valor(self, clave, valor):
        return self.contenido.get(clave, None)

    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento(id ={self.id}, contenido ={self.contenido})"