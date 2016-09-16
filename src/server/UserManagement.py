import getpass
from robotparser import Entry
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import hashlib
from lxml import etree


class UserManagement:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.password = hashlib.md5(b'self.password').hexdigest()
        self.document = ElementTree.parse('\Resources_Lists\Users')

    def authentication(self):

        users = self.document.find('Users')
        for node in users.getiterator():
            if node.attrib['name'] == self.username & node.attrib['password']:
                return True
            else:
                return False

    def addUser(self):

        username = raw_input(prompt="Enter Username: ")
        password = raw_input(prompt="Enter Password: ")
        root_node = self.document.find('Users')
        child = SubElement(root_node, 'User', name='%s' %username, password='%s' %hashlib.md5(b'%s')%password.hexdigest())

        with open('/Resources_Lists/Users', 'w') as output_file:
            out = etree.fromstring(ElementTree.tostring(root_node))
            output_file.write(etree.tostring(out, pretty_print=True))
            output_file.close()






