minifykr
========

A script to minify XML files in <a href="http://www.krpano.com" target="_blank">krpano</a> projects

Usage: minifykr.py inputFile outputFile

krpano projects often consist of a large number of XML files, which have to be loaded by the browser. This script minifies the XML code, merging the code and removing unecessary code, such as comments or spaces between XML tags.

This script recursively transverses all the files which are included in "inputFile" through &lt;include&gt; tags, minifies their code and writes the result to "outputFile"