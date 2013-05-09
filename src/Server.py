#!/usr/bin/python
from Start import Start
import cgi, cgitb 
form = cgi.FieldStorage() 
query = form.getvalue('query')
import types
if type(query) == types.NoneType:#for testing 
	query = 'SELECT Company_Name , Eps FROM DB WHERE Year = 1995'#testing query
print Start(query)
