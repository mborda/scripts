#/usr/bin/python

import csv, time
from datetime import date

def create_product(book):
    xml_string = """	<product>
		<productidentifier>
			<b221 refname="ProductIDType">15</b221>
			<b244 refname="IDValue">%s</b244>
		</productidentifier>
		<title>
			<b202 refname="TitleType">01</b202>
			<b203 refname="TitleText">%s</b203>
		</title>
		<contributor>
			<b034 refname="SequenceNumber">1</b034>
			<b035 refname="ContributorRole">A01</b035>
			<b036 refname="PersonName">%s</b036>
			<b037 refname="PersonNameInverted">%s</b037>
		</contributor>
		<language>
			<b253 refname="LanguageRole">01</b253>
			<b252 refname="LanguageCode">%s</b252>
		</language>
		<salesrights>
			<b089 refname="SalesRightsType">01</b089>
			<b388 refname="RightsTerritory">WORLD</b388>
		</salesrights>
		<b064 refname="BASICMainSubject">%s</b064>
		<othertext>
			<d102 refname="TextTypeCode">01</d102>
			<d103 refname="TextFormat">02</d103>
			<d104 refname="Text">%s</d104>
		</othertext>
		<publisher>
			<b291 refname="PublishingRole">01</b291>
			<b081 refname="PublisherName">%s</b081>
		</publisher>
		<b394 refname="PublishingStatus">04</b394>
		<b003 refname="PublicationDate">20120215</b003>
		<supplydetail>
			<j143 refname="OnSaleDate">20120215</j143>
			<price>
				<j148 refname="PriceTypeCode">04</j148>
				<j151 refname="PriceAmount">%s</j151>
				<j152 refname="CurrencyCode">EUR</j152>
			</price>
		</supplydetail>
	</product>""" % (book['isbn'].replace("-",""), 
    book["publication_title*"], 
    book["author*"].rsplit(", ")[1]+" "+book["author*"].rsplit(", ")[0], 
    book["author*"],
    language[book["language*"].rsplit("-")[0]],
    genre[book["genre*"].rsplit("-")[0]],
    book["publication_desc*"],
    book["publisher*"],
    book["content_price*"])
    return xml_string

language = {"87": "spa", "88": "bqa", "89": "eng", "90": "fre",
    "484": "ger", "485": "dut", "486": "ita", "2417": "cat",
    "9745": "cat", "487": "spa"}
genre = { "1607": "FIC022000", "1610": "FIC004000", "1612": "FIC001000", 
    "1614": "FIC007000", "1616": "FIC014000", "1618": "PER011000", 
    "1620": "LIT000000", "1627": "JUV000000", "1629": "FIC019000", 
    "1631": "POL000000", "1633": "HIS000000", "1646": "FIC027000", 
    "1651": "HEA000000", "1662": "FIC029000", "1664": "CKB000000", 
    "1673": "NON000000", "1676": "PHI000000", "1679": "BIO000000", 
    "1683": "FIC015000", "1685": "EDU000000", "1691": "SPO000000", 
    "1703": "REL000000", "1705": "TRV000000", "1708": "POE000000", 
    "1710": "SOC000000", "1714": "FIC000000", "1718": "MUS000000", 
    "1720": "SEL000000", "1728": "BUS000000", "1729": "BUS050000", 
    "1733": "REF010000", "1739": "SCI030000", "1741": "SCI000000", 
    "1774": "REF008000", "1796": "FIC016000", "1805": "HIS003000", 
    "1817": "FIC030000", "1834": "FIC026000", "1847": "FIC028000", 
    "1864": "NAT000000", "1886": "FIC009000", "1918": "LAN000000", 
    "1943": "FIC021000", "1960": "GAM000000", "1993": "CUR000000", 
    "2002": "FIC005000", "2005": "LAW000000", "2011": "ART000000", 
    "2020": "FAM000000", "2035": "TEC000000", "2047": "REF000000", 
    "2069": "MED000000", "2111": "LAN004000", "2533": "NON000000", 
    "10246": "NON000000", "6006": "NON000000", "10579": "NON000000" }

r = csv.DictReader(open("pr.csv", 'rb'), delimiter=";", quotechar='"')
xml = """<?xml version="1.0" encoding="UTF-8"?>
<ONIXmessage xmlns="http://www.editeur.org/onix/2.1/short"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.editeur.org/onix/2.1/short/ONIX_BookProduct_Release2.1_short.xsd">
	<header>
		<m174 refname="FromCompany">Leer-e</m174>
		<m182 refname="SentDate">%s</m182>
	</header>""" % (date.today().strftime("%Y%m%d"),)
for row in r:
    xml = xml + create_product(row)
xml = xml + "</ONIXmessage>"

print xml
f = open("out.xml", 'w')
f.write(xml)
f.close()
