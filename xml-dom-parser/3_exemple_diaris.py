from xml.dom import minidom 

doc = minidom.parse("diaris.xml")

tag_principal = doc.documentElement

file = open("diaris.html", "w")
file.write("<html><head><title>Diaris DOM</title></head><body>")

llista_tag_diari = tag_principal.getElementsByTagName("diari")
for tag_diari in llista_tag_diari:
    id = tag_diari.getAttribute("id")
    nom = tag_diari.getElementsByTagName("nom")[0].firstChild.data
    url = tag_diari.getElementsByTagName("url")[0].firstChild.data
    
    file.write("<p>")
    file.write(f"<a id='{id}' href='{url}'>#{id} {nom}</a>")
    file.write("</p>")

file.write("</body></html>")
file.close()
