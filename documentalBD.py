

class Documento:

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
    
    
    
class Coleccion:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
        
    def añadir_documento(self, documento):
        self.documentos[documento.id] = documento
        
    def eliminar_documento(self, id_documenro):
        if id_documento in self.documentos:
            del self.documentos[id_documento]
            
    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
        
    def __str__(self):
        return f"Colección {self.nombre} con {len(self.documentos)} documentos"
    
    
class BaseDeDatosDocumental:
    
    def __init__(self):
        self.colecciones = {}
        
    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
            
    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones"
    

