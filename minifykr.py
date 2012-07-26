import argparse
from xml.etree.ElementTree import ElementTree, Element

MAXIMUM_INDEX = 99999999999999


def copyElementTag(element):
	return Element(element.tag, element.attrib)



def mergeInto(root, newRoot):

	for e in root.getchildren():
		
		if e.tag == "include":
			includedFile = e.get('url')

			#Get the root element of the included file
			tree = ElementTree()
			try:
				tree.parse(includedFile)
			except:
				print("Error parsing file: %s" % includedFile)
				return
			includedRoot = tree.getroot()

			#Merge the tags of the included file
			mergeInto(includedRoot, newRoot)

		else:
			#print("TAIL: ",e.tail)
			#print("TEXT: ", e.text)
			e.tail = None
			newRoot.insert(MAXIMUM_INDEX, e) #gigantic number ensures that the tags will always be added to the end of the file

	return newRoot

def minifyKr(source, destination):
	tree = ElementTree()
	tree.parse(source)
	root = tree.getroot()
	
	#Copy the root node that we'll copy the elements into
	newRoot = copyElementTag(root)
	mergeInto(root, newRoot)
	
	
	minTree = ElementTree(newRoot)
	#merged, tree = getFileContents("tour.xml")
	minTree.write(destination)


parser = argparse.ArgumentParser(description='Minify XML files in krpano projects')

parser.add_argument('inputFile', default="tour.xml")
parser.add_argument('outputFile', default="tour.min.xml")

options = parser.parse_args()

minifyKr(options.inputFile, options.outputFile)