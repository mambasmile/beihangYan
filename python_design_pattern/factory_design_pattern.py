#coding=utf-8
'''
Created on 2017年5月2日

@author: Administrator
'''
import xml.etree.ElementTree as etree
import json
from twisted.python import filepath
from symbol import factor

class JSONConnector:
    def __init__(self,filepath):
        self.data=dict()
        with open(filepath,mode='r') as f:
            self.data = json.load(f)
            
    @property
    def parsed_data(self):
        return self.data
        
class XMLConnector:
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)
    
    @property
    def parse_data(self):
        return self.tree
    
def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
        print '没有进入吗？'
    elif filepath.endswith('xml'):
        connector = XMLConnector
        
    else:
        print '-----------'
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as e:
        print e 
    return factory

def main():
    print '%%%%%%%'
    sqlite_factory = connect_to("filepath.sq3")
    print ()
    xml_factory = connect_to(r"E:\beihang_study\respository\beihangYan\python_design_pattern\person.xml")
    xml_data = xml_factory.parse_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person','lastName', 'Liar'))
    print 'found: {} persons'.format(len(liars))
    for liar in liars:
        print 'first name: {}'.format(liar.find('firstName').text) 
        print 'last name: {}'.format(liar.find('lastName').text) 
        print ['phone number ({}):'.format(p.attrib['type']) for p in liar.find('phoneNumbers')]
    
    json_factory = connect_to(r'E:\beihang_study\respository\beihangYan\python_design_pattern\donut.json')
    if json_factory is None:
        print 'mambasmile'
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        print ['topping: {} {}'.format(t['id'], t['type']) for t in donut['topping']]
    
if __name__ == '__main__':
    main()   
        
        