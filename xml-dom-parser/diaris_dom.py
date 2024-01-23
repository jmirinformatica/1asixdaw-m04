from xml.dom import minidom 

doc = minidom.parse("diaris.xml")

file = open("diaris.html", "w")
file.write("<html><head><title>Diaris DOM</title></head><body>")

diaris = doc.getElementsByTagName("diari")
for diari in diaris:
    id = diari.getAttribute("id")
    nom = diari.getElementsByTagName("nom")[0].firstChild.data
    url = diari.getElementsByTagName("url")[0].firstChild.data
    
    file.write("<p>")
    file.write(f"<a id='{id}' href='{url}'>#{id} {nom}</a>")
    file.write("</p>")

file.write("</body></html>")
file.close()