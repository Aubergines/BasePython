__author__ = 'Main'

print len('abc')
s = "JKUh"
print s.__contains__("KU")
print s.lower()

myfile = open("__init__.py");
try:
    file_content = myfile.read();
finally:
    myfile.close();

print myfile