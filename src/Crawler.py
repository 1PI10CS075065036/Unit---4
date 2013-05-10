import urllib2
import copy
import thread
import datetime
from Miner import Get_Data
import re
from bs4 import BeautifulSoup

Base_URL='http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=ORCL&type=10-Q&dateb=2013&owner=exclude&count=100'

def Start_Crawler():
    for tick in open('Ticker_Sym.txt'):
        tick.strip()
        temp=Base_URL
        temp=temp.replace('XXXXX',tick)
        temp=temp.replace('\n', '')
        temp=temp+'\n'#Generate The Required URLS to be Crawled
        usock = urllib2.urlopen(temp)
        data = usock.read()
        usock.close()
        soup = BeautifulSoup(data)
        tick=tick.strip()
        url,c_name,year,quarter= Get_Urls(soup)
        print "url:\n",url,"\nc_name:\n",c_name,"\nyear:\n",year,"\nQ:\n",quarter
        #count=count+1
        Fin_url = Get_Archive_From_Url(url)
        print "\nfinalurl:\n",Fin_url
        if len(Fin_url) == 4:
            Get_Data(year,quarter,[c_name,tick],Fin_url)

def Get_Quarter(year):
    return "Q"+str(((int(year[5:7])-1)//3)+1)

def Get_Urls(soup):
    url=[]
    year=[]
    quarter=[]
    try:
        copysoup = soup
        company_name = str(soup.find("span", class_="companyName").contents[0])
        company_name = company_name.strip()
        Url = soup.find_all('a',id="interactiveDataBtn",limit=4)
        for i in Url:
            pattern = r'"(.*?)"'
            robj = re.search(pattern, str(i), re.S|re.I)
            url.append("http://www.sec.gov"+robj.group(1))
        td = copysoup.find_all('td')
        count = 0
        for i in td:
            pattern = r'([0-9]{4})-([0-9]{2})-([0-9]{2})'
            robj1 = re.search(pattern,str(i),re.S|re.I)
            if robj1:
                    if int(robj1.group(1))<=2013 and count<4:
                            year.append(robj1.group(1))
                            count = count+1
                            quarter.append(Get_Quarter(str(robj1.group())))
                    else:
                            pass
            else:
                    pass
        
        return url,company_name,year,quarter
    except Exception,e:
        print e
        return [],"",[],[]

def Get_Archive_From_Url(url):
    Fin_url=[]
    try:
        for u in url:
            usock = urllib2.urlopen(u)
            data = usock.read()
            copydata=data
            usock.close()
            soup = BeautifulSoup(data)
            copysoup = soup
            soup = str(soup)
            temp = copysoup.find("a",text=re.compile(r'(.*?)((statemen(ts|t)\sof\s(income|earnings|operatio(ns|n)))|(income\sstatemen(ts|t)))(.*?)',re.S|re.M|re.I))
            robj = re.search(r'href="javascript\:loadReport\((.*?)\)\;"',str(temp), re.S|re.I|re.M)
            temp = robj.group(1)
            copydata=copydata[copydata.index(''+temp+'] ='):]
            copydata=copydata[copydata.index('"')+1:]
            copydata=copydata[:copydata.index(';')-1]
            copydata="http://www.sec.gov"+copydata
            Fin_url.append(copydata);
    finally:
        return Fin_url

if __name__ == '__main__':
   # a = datetime.datetime.now().replace(microsecond=0)
    Start_Crawler()
    #b = datetime.datetime.now().replace(microsecond=0)
    #print(b-a)
