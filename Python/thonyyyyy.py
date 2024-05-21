testhtml="""
<!doctype html>
<head>
    <meta charset="utf-8">
    <title>HTML Parsing: A Primer</title>
    <style> body {background-color: beige; } </style>
</head>
<body>
<h1>Some Content!</h1>
<ul>
<li>You can use python to automatically process webpages.</li>
<li>This is <a id="link" href="http://wikipedia.org">Wikipedia</a></li>
<li><a id="link" href="http://wikipedia.org/wiki/Opossum">All about possums</a></li>
<li><p>Here's a possum:</p>
<img width=200 src="http://homer.stuy.edu/~jvorob/images/possum.jpg">
</li>
</ul>
</body>
</html>
"""

def extractHTMLTags(html):
    newHtml = ""
    bracket = None
    for i in range(len(html)):
        if html[i] == "<":
            bracket = True
        if html[i] == ">":
            bracket = False
        if bracket == True and html[i] != "<":
            newHtml += html[i]
        else:
            continue
    return newHtml

#print(extractHTMLTags(testhtml))

def extractText(html):
    newHtml = ""
    bracket = None
    for i in range(len(html)):
        if html[i] == ">":
            bracket = True
        if html[i] == "<":
            bracket = False
        if bracket == True and html[i] != ">":
            newHtml += html[i]
        else:
            continue
    return newHtml

#print(extractText(testhtml))

def getAllLinks(html):
    newHtml = ""
    bracket = None
    for i in range(len(html)):
        if html[i:i + 6] == 'href="':
            bracket = True
        if html[i] == '"':
            bracket = False
        if bracket == True and html[i] != 'href="':
            newHtml += html[i]
        else:
            continue
    return newHtml

print(getAllLinks(testhtml))