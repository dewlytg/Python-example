#!/usr/bin/env python
#-*-coding:utf-8-*-

import xml.etree.ElementTree as ET

tree = ET.parse("./testfile/test.xml")
root = tree.getroot()
print root.tag

# 遍历xml文档
for child in root:
    print child.tag,child.attrib
    for i in child:
        print i.tag,i.text,i.attrib

# 只遍历year节点
for node in root.iter('year'):
    print node.tag,node.text

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated_by", "Alex")

tree.write("./testfile/test.xml")

# 删除node
for country in root.findall ('country'):
    rank = int (country.find ('rank').text)
    if rank > 50:
        root.remove (country)

tree.write('./testfile/output.xml')

# 创建
new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "Alex Li"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Oldboy Ran"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("./testfile/testnew.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式