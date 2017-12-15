#coding=utf-8

import xml.dom.minidom

dom = xml.dom.minidom.parse('D:\\Repositories\\littleTools\\data\\test.xml')
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)

bb =root.getElementsByTagName('title')
b=bb[0]
print(b.getAttribute('name'))
b=bb[1]
print(b.getAttribute('name'))

