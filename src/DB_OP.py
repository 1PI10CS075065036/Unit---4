from pymongo import *

import pymongo

import types

import datetime

import sys

#from Validation import val_qry

from bson.objectid import ObjectId

sting=""



def read(z) :#reads all the data from list and returns a list of with proper structured data

    

    

    

    Company_Name,Ticker_Symbol,Quarter,Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year=details(z)

        

    return Company_Name,Ticker_Symbol,Quarter,Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year



def details(z):#from the crawled data list extract the data in a orderly manner




    Company_Name=z[0]

    

    Ticker_Symbol=z[1]

    

    Quarter=z[2]

    

    Eps=z[3]



    Revenue=z[4]



    SandM_Expenses=z[5]



    RandD_Expenses=z[6]



    Tax=z[7]



    Service_Expenses=z[8]



    Total_Expenses=z[9]



    Operating_Margin=z[10]



    Operating_Margin_Percentage=z[11]



    RandD_Expense_ratio=z[12]



    Growth_Rate=z[13]



    Year=z[14]





    

    return Company_Name,Ticker_Symbol,Quarter,Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year



def insert(z):#the function for inserting data into a collection and into the db



    db=con()



    #d=raw_input("enter number of companies\n")

   

    Company_Name,Ticker_Symbol,Quarter,Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year=read(z)

    #post={}

    post = {"Company_Name": Company_Name , "Ticker_Symbol": Ticker_Symbol , "Quarter":Quarter, "Eps":Eps,"Revenue":Revenue,"S&M_Expenses":SandM_Expenses,"R&D_Expenses":RandD_Expenses,"Tax":Tax,"Service_Expenses":Service_Expenses,"Total_Expenses":Total_Expenses,"Operating_Margin":Operating_Margin,"Operating_Margin_Percentage":Operating_Margin_Percentage,"R&D_Expense_ratio":RandD_Expense_ratio,"Growth_Rate":Growth_Rate,"Year":Year}

    post_id=db.fincoll.insert(post)

#    db.fincoll.update({'Company_Name':Company_Name},{"$set":{"Quarter":Quarter,'Eps':Eps,'Revenue':Revenue,'S&M_Expenses':SandM_Expenses,'R&D_Expenses':RandD_Expenses,'Tax':Tax,'Year':Year}})

    cursor= db.fincoll.find()

    getres(cursor)





def getres(cursor):#get results from object list returned from processed query

    ret=[]

    for i in cursor:

        # print i

         ret.append(i)

    return ret



def con():#make connections

    #from pymongo import MongoClient

    client=MongoClient("localhost",27017)

    db = client['findb']

    return db    



def initlist(i):#test initialisation list for debugging test

    if i== 1:

        #print "here"

        return ["pesit","pes","Q1",12345,11200,123,23,11111,23,123,23,34,23,34,1992]

    elif i==2:

        return ["pesit","pes","Q1",12345,1234,123,23,123,23,123,23,34,23,34,1994]



    elif i==3:

        return ["pesit","pes","Q1",12345,1234,123,23,123,23,123,23,34,23,34,1996]



def wbsp(a,n):#removes sp chars and spaces

    i=0

    c=[]



    while i < n :



        if a[i]!=' ' and a[i] != ',' and a[i] != '(' and a[i] != ')' :

            c.append(a[i])

        i=i+1

    d=["*"]

    c.append(d[0])

    return c



def nums(c):#number of select aruments

    n=len(c)

    i=1

    j=0

    #print c[0]

    while i+1<n :

        if c[i]!='FROM' :

            #print c[i]

            j=j+1

        else :

            break

        i=i+1

    #print j

    return j



def posw(w,n):#position of where

    i=0

    while i<n:



        if w[i]=="WHERE":

            break

        i=i+1

    return i



def numa(c):#number of ands

    n=len(c)



    j=0

    x=posw(c,n)

    i=x

    while i+1<n :

        if c[i]=='AND' :

            j=j+1

        if c[i]=='*':

            break

        i=i+1

    return j



def arwq(c,noa):#number of where arguments

    x=-2

    i=0



    if c[x]!='DB':

        while c[x]!='DB':



            if c[x]!= '=' and c[x]!= '!=' and c[x]!= '>' and c[x]!= '<' :



                i=i+1

            x=x-1

        if noa==0:



            i=i-1

        else :

            i=i-1-noa



    #print i

    return i/2







#DHIREN>PY BEGINS HERE !





def convert(x):#conversion from string to int and vice versa

    try:

        return int(x)

    except:

        return x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            







def get(a,nos,noa):#get the select and where dictionaries for querying mongodb

    #print a

    where={}

    select={}



    select=get_sel(a,nos)

    #print select

    where=get_where(a,noa)

    #print where

    return select , where 



def get_sel(a,nos):#get select dict

    s={}

    i=1

    n=len(a)

    i=0

    

    

    i=1



    while i <= nos :

        s[a[i]]=1

        i=i+1

    

    s['_id']=0

    

    return s



def get_where(a,noa):#get the where dictionary for query

    n=len(a)

    i=posw(a,n)

#    print i

    s={}

    while (i+3) < n :

        b=i+1

        if a[b+1] == '=' :

            s[a[b]]=convert(a[b+2])

            i=i+4

        elif a[b+1] == '>' :

            f={}

            f['$gt']=convert(a[b+2])

            s[a[b]]=f

            i=i+4

        elif a[b+1] == '<' :

            f={}

            f['$lt']=convert(a[b+2])

            s[a[b]]=f

            i=i+4

        elif a[b+1] == '>=' :

            f={}

            f['$gte']=convert(a[b+2])

            s[a[b]]=f

            i=i+4

        elif a[b+1] == '<=' :

            f={}

            f['$lte']=convert(a[b+2])

            s[a[b]]=f

            i=i+4

        elif a[b+1] == '!=' :

            f={}

            f['$ne']=convert(a[b+2])

            s[a[b]]=f

            i=i+4

   





    return s







def prcs(a):#processing query

    db=con()

    m=a.split()

    n=len(m)

        

    v=wbsp(m,n)

        

    nos=nums(v)

        

    noa=numa(v)

        

    arw=arwq(v,noa)

        

        

    if v[1]=='*' and noa==0 and arw==0 :#select 8

        cursor= db.fincoll.find()

        return getres(cursor)

    elif v[1]=='*' and noa==0 and arw>0 :

           

        v.pop(-1)

        select,where=get(v,nos,noa)

        cursor=db.fincoll.find(where)

        return getres(cursor)

    

    elif v[1] == 'TOP' :

#            print v

            x=convert(v[10])
              
            cursor=db.fincoll.find({"Year":x},{v[4]:1,"_id":0}).sort(v[2],1).limit(int(v[3]))

            return getres(cursor)

    elif v[1] == 'MAX' :

            x=convert(v[10])
	
            cursor=db.fincoll.find({"Year":x},{v[4]:1,"_id":0}).sort(v[2],1).limit(int(v[3]))

            return getres(cursor)  

    else :

        v.pop(-1)

        select,where=get(v,nos,noa)

        cursor=db.fincoll.find(where,select)

        return getres(cursor)



def query():#for starting the processing of query
    db=con()
    a=raw_input()
    prcs(a)

if __name__ == '__main__':
    db=con()
    i=1
    while(1):
        a=raw_input("1.to input 2.to query 3.to update\n")
        b=int(a)
        z={}
        if b==1 :
            z=initlist(i)
            insert(z)
            i=i+1
        elif b==2 :
            pass
            #query()
