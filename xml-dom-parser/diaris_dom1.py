from xml.dom import minidom 

doc = minidom.parse("diaris.xml")

print("<html><head><title>Diaris DOM</title></head><body>")

diaris = doc.getElementsByTagName("diari")
for diari in diaris:
    id = diari.getAttribute("id")
    nom = diari.getElementsByTagName("nom")[0].firstChild.data
    url = diari.getElementsByTagName("url")[0].firstChild.data
    
    print("<p>")
    print(f"<a id='{id}' href='{url}'>#{id} {nom}</a>")
    print("</p>")

print("</body></html>")
