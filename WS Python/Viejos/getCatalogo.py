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
    def addLibroCliente(self, idLibro, idModelo, idPedido):
        return json.loads(os.popen("php addLibroCliente.php %s %s %s" % (idLibro, idModelo, idPedido)).read())
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

ws = wsLeere(1)
print ws.token
'''
#output = os.popen("php getCatalogo.php").read()
#catalogo = json.loads(output)
catalogo = ws.getCatalogo()
#print catalogo

for i in catalogo:
    print "id: ", i["id"]
    print "Modelo: ", i["id_modelo"]

autores = ws.getAutores()
#print autores

for i in autores:
    print "id: ", i["id"]
    print "autor: ", i["titulo"]

modelos = ws.getModelos()
#print modelos

for i in modelos:
    print "id: ", i["id"]
    print "Formato: ", i["titulo"]

generos = ws.getGeneros()
#print generos

for i in generos:
    print "id: ", i["id"]
    print "Genero: ", i["titulo"]

editoriales = ws.getEditoriales()
#print editoriales

for i in editoriales:
    print "id: ", i["id"]
    print "Genero: ", i["titulo"]

libro = ws.getDetalleLibro(504, 70)
for key in libro[0].iterkeys():
    print key, libro[0][key]
'''
mis_libros = ws.getLibrosCliente(1,0,0)
print mis_libros
