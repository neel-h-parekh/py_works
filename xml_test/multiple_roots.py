import xml.etree.ElementTree as ET

xml_root = []

xml_str = ''

with open("multiple_roots.xml") as f:
    for line in f:
        line = line.strip()
        xml_str = xml_str.strip() + line.strip()
        if line.endswith("</collection>"):
            # print("endswith")
            xml_root.append(xml_str)
            # print(xml_str)
            xml_str = ''

for i in xml_root:
    print(i)
    tree = ET.ElementTree(ET.fromstring(i))
    root = tree.getroot()
    for item in root.iter():
        print(item.attrib)


