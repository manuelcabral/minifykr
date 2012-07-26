minifykr
========

A script to minify XML files in <a href="http://www.krpano.com" target="_blank">krpano</a> projects. It requires the argparse library, which is available in Python 3.2.

Usage: minifykr.py [inputFile] [outputFile]
(The default values for inputFile and outputFile are "tour.xml" and "tour.min.xml")

krpano projects often consist of a large number of XML files, which have to be loaded by the browser. This script minifies the XML code, merging all the files and removing unnecessary code, such as comments or spaces between XML tags.

This script recursively transverses all the files which are included in "inputFile" through &lt;include&gt; tags, minifies their code and writes the result to "outputFile". Minifying does the following:

- removes comments
- removes characters between tags
- removes text inside tags which are not &lt;data&gt; or &lt;action&gt;