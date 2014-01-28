#/usr/bin/python
#Pasarela Python para WS de Leer-e

import sys, os, json

class wsLeere:
    def __init__(self,idClienteComercio):
        if idClienteComercio != 0:
            self.token = json.loads(os.popen("php login.php %s" % (idClienteComercio,)).read())
        else:
            self.token = None
    def getLibrosCliente(self, idClienteComercio, idLibro, idModelo):
        return json.loads(os.popen("php getLibrosCliente.php %s %s %s" % (idClienteComercio, idLibro, idModelo)).read())
    def getDetalleLibro(self, idLibro, idModelo):
        return json.loads(os.popen("php getDetalleLibro.php %s %s" % (idLibro, idModelo)).read())
    def addLibroCliente(self, idClienteComercio, idLibro, idModelo, idPedido):
        return json.loads(os.popen("php addLibroCliente.php %s %s %s %s" % (idClienteComercio, idLibro, idModelo, idPedido)).read())
    def getGeneros(self):
        return json.loads(os.popen("php getGeneros.php").read())
    def getAutores(self):
        return json.loads(os.popen("php getAutores.php").read())
    def getEditoriales(self):
        return json.loads(os.popen("php getEditoriales.php").read())
    def getModelos(self):
        return json.loads(os.popen("php getModelos.php").read())
    def getCatalogo(self):
        return json.loads(os.popen("php getCatalogo.php").read())

#A partir de aquí se muestran ejemplos de uso y obtención de datos
'''
ws = wsLeere(0)

#Se obtienen los datos del catalogo
catalogo = ws.getCatalogo()

for i in catalogo:
    print "id: ", i["id"]
    print "Modelo: ", i["id_modelo"]

#Se obtiene la tabla de autores
autores = ws.getAutores()

for i in autores:
    print "id: ", i["id"]
    print "autor: ", i["titulo"]

#Se obtiene la tabla de Formatos
modelos = ws.getModelos()

for i in modelos:
    print "id: ", i["id"]
    print "Formato: ", i["titulo"]

#Se obtiene la tabla de géneros
generos = ws.getGeneros()

for i in generos:
    print "id: ", i["id"]
    print "Genero: ", i["titulo"]

#Se obtiene la tabla de editoriales
editoriales = ws.getEditoriales()

for i in editoriales:
    print "id: ", i["id"]
    print "Editorial: ", i["titulo"]

#Se obtiene el detalle de un libro
libro = ws.getDetalleLibro(504, 70)
for key in libro[0].iterkeys():
    print key, libro[0][key]

#Se obtienen los libros de un cliente y se consulta el detalle de un libro
mis_libros = ws.getLibrosCliente(1,0,0)
print mis_libros
for key in mis_libros[0].iterkeys():
    print key, mis_libros[0][key]
'''
