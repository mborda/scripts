#/usr/bin/python

import sys, httplib
import lxml.etree

class book():
    def __init__(self):
        self.id = ""
        self.id_modelo = []
    def __repr__(self):
        return ("Id: %s\n\tModelos: %s\n" %(self.id, self.id_modelo))

        


SM_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope" xmlns:ns1="urn:Leere" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:enc="http://www.w3.org/2003/05/soap-encoding">
  <env:Body>
    <ns1:getCatalogo env:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
      <data xsi:type="enc:Struct">
        <IdComercio xsi:type="xsd:string">%s</IdComercio>
        <IdAutor xsi:type="xsd:int">0</IdAutor>
        <IdGenero xsi:type="xsd:int">0</IdGenero>
        <IdEditorial xsi:type="xsd:int">0</IdEditorial>
      </data>
    </ns1:getCatalogo>
  </env:Body>
</env:Envelope>
"""

SoapMessage = SM_TEMPLATE%("0")

#print SoapMessage

#construct and send the header

webservice = httplib.HTTP("ws.leer-e.es")
webservice.putrequest("POST", "/index.php/webservices/catalogo")
webservice.putheader("Host", "ws.leer-e.es")
webservice.putheader("User-Agent", "Python post")
webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
webservice.putheader("Content-length", "%d" % len(SoapMessage))
webservice.putheader("SOAPAction", "\"\"")
webservice.endheaders()
webservice.send(SoapMessage)

# get the response

statuscode, statusmessage, header = webservice.getreply()
#print "Response: ", statuscode, statusmessage
#print "headers: ", header
#res = webservice.getfile().read()
#print res
tree = lxml.etree.parse(webservice.getfile())
root = tree.getroot()
#print root.tag
body = root.find("{http://www.w3.org/2003/05/soap-envelope}Body")
#print body.tag
getCatalogoResponse = body.find("{urn:Leere}getCatalogoResponse")
#print getCatalogoResponse.tag
data = getCatalogoResponse.find("data")
#print data.tag
books = []
for b in data:
    bi = book()
    for item in b:
        if item.find("key").text == "id":
            bi.id = item.find("value").text
        elif item.find("key").text == "id_modelo":
            bi.id_modelo.append(item.find("value").text)
    l = [x for x in books if bi.id == x.id]
    if l:
        x = l[0]
        books.remove(x)
        x.id_modelo.append(bi.id_modelo[0])
        books.append(x)
        #print x
    else:
        books.append(bi)
        #print bi
print books
