import clr
clr.AddReference('System.Xml')

import os
import time
import datetime
from PythonFileReader import PythonFileReader
from CreateBackup import createBackup
from System.Xml import XmlReader

DB_HOST = ''
DB_USER = ''
DB_USER_PASSWORD = ''
DB_NAMES = ''
BACKUP_PATH = ''

f = open('configuracion.xml')
fr = PythonFileReader(f)
xr = XmlReader.Create(fr)

while xr.Read():
    if xr.IsStartElement(): 
    	if xr.Name=='host' : DB_HOST= xr.GetAttribute("name")
    	if xr.Name=='user' : DB_USER= xr.GetAttribute("name")
    	if xr.Name=='pass' : DB_USER_PASSWORD= xr.GetAttribute("name")
    	if xr.Name=='path' : BACKUP_PATH= xr.GetAttribute("name")
    	if xr.Name=='database' : DB_NAMES += ','+xr.GetAttribute("name")
    	
print DB_HOST,DB_USER,DB_USER_PASSWORD,DB_NAMES,BACKUP_PATH

ARRAY_DB_NAME = DB_NAMES.split(',')


for DB_NAME in ARRAY_DB_NAME:
	if DB_NAME:
		createBackup(DB_NAME,DB_HOST,DB_USER,DB_USER_PASSWORD,BACKUP_PATH)
		print DB_NAME

raw_input()
