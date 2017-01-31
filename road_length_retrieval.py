#this file prints the lenghts of all the roads in an openstreetmap sumo file
from lxml import etree
from xml.dom.minidom import parseString
import xml.dom.minidom
import xml.etree.ElementTree as ET
import array
import sys


old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file

doc = etree.parse ( 'busnet3.net.xml' )
edges = doc.findall ( "edge" )
root = ET.Element('Placemark')

for edge in doc.getiterator():
	if edge.tag == "lane":
		if  edge.attrib.has_key ( 'shape' ):
			shape = edge.get( 'shape' )
			S = shape.split()
			E = edge.getparent()
			EE = E.getparent()
			print edge.get( 'length' ) 
sys.stdout = old_stdout

log_file.close()
