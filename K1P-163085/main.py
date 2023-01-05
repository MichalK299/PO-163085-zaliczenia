from element import Element
from file import File
from directory import Directory

element1 = Element('element1', 1990)
print(element1)

element2 = File('element2', 2000, 123)
print(element2)
element4 = File('element2', 2000, 123)
element5 = File('element2', 2000, 123)

element3 = Directory('element3', 2002, 321, [element2, element4])
print(element3)

print(element2 == element4)
