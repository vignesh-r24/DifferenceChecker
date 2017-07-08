import difflib
import webbrowser
import os

s1 = "Vignesh is a boy"
s2 = "Vignesh is a male"

HTMLObject = difflib.HtmlDiff()
result = HTMLObject.make_file(s1,s2)

file = open('differences.html', 'w')
file.write(result)
file.close()

webbrowser.open('file://' + os.path.realpath('differences.html'))

