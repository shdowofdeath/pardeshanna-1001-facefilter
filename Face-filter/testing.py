import xml.etree.ElementTree as ET
fiker='xmlFile'
root = ET.parse(fiker).getroot()
for something in root:
    print(something.tag )

for type_tag in root.findall('bar/type'):
    value = type_tag.get('foobar')
    print(value)
