import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import os

def ImportMatchData():
    #Przejscie przez blad SSL Certification
    """
    myssl = ssl.create_default_context();
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    """

    url="http://pilkanozna.pl/index.php/10272/LOTTO-Ekstraklasa-2016/17/showResultsRank.html"
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    respData=response.read()
    soup=BeautifulSoup(respData,"html.parser")
    MatchHistoryDataRaw=soup.find("div",attrs={"id":"wyniki"})
    MatchPattern=re.findall(r'title="(.*?)"',str(MatchHistoryDataRaw))
    MatchHistory=[]
    for i in range(len(MatchPattern)):
        j=16*i
        if i>16 and i%16!=0:
            MatchHistory.append(str(MatchPattern[i]))
    MatchResults=re.findall(r'showReport.html">(\d:\d)<',str(MatchHistoryDataRaw))
    MatchData=[]

    for i in range(len(MatchResults)):
        result=MatchHistory[i],MatchResults[i]
        MatchData.append(str(result))

    print(MatchResults)
    print(MatchHistory)
    print(MatchData)

    fname="MatchHistory.txt"
    with open(fname,"w") as file:
        for data in MatchData:
            file.write(data+os.linesep)
    file.close()

ImportMatchData()