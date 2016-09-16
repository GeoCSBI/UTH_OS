import getpass
from robotparser import Entry
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import hashlib
from lxml import etree

#<Stock_Exchangers>
stock_exchangers = Element('Stock_Exchangers')

#<Stock_Exchangers><Users/>
users = SubElement(stock_exchangers, "Users")

#<Stock_Exchangers><Users/><Username/>
username = SubElement(users, 'User', name = 'admin', password = '%s' %hashlib.md5(b'psw').hexdigest())
raw_input("Enter A Password: ")

username2 = SubElement(users, 'User', name = 'test', password = '%s' %hashlib.md5(b'100').hexdigest())

with open('Users', 'w') as output_file:
    output_file.write('<?xml version="1.0" encoding="UTF_8" standalone="no"?>' + '\n')
    output_file.write('<!DOCTYPE Stock_Exchangers SYSTEM "Stock_Exchangers.dtd">' + '\n')
    out = etree.fromstring(ElementTree.tostring(stock_exchangers))
    output_file.write(etree.tostring(out, pretty_print=True))
    output_file.close()


stocks = Element('Stocks')
stock_details = SubElement(stocks, 'Stock_Details')
stock_name = SubElement(stock_details, 'Company_Name', company_name ='Test')
stock_price = SubElement(stock_details, 'Stock_Price', stock_price='500$')
stock_number = SubElement(stock_details, 'Number_Of_Stocks', number_of_stocks='1400')
stock_phase = SubElement(stock_details, 'Stock_Phase', stock_phase= 'up', percentage='50%')

with open('Stocks', 'w') as output_file:
    output_file.write('<?xml version="1.0" encoding="UTF_8" standalone="no"?>' + '\n')
    output_file.write('<!DOCTYPE Stock_Exchangers SYSTEM "Stock_Exchangers.dtd">' + '\n')
    out = etree.fromstring(ElementTree.tostring(stocks))
    output_file.write(etree.tostring(out, pretty_print=True))
    output_file.close()