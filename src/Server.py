#!C:\Python27\python.exe
from Start import Start
import cgi, cgitb 
form = cgi.FieldStorage() 
query = form.getvalue('query')
import types
if type(query) == types.NoneType:#for testing 
	query = 'SELECT TOP ( Revenue , 3 ) Company_Name FROM DB WHERE Year = 1994'#testing query
print Start(query)