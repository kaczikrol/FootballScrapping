import urllib.request
import urllib.parse
import re
import codecs
from bs4 import BeautifulSoup
import os




def LoadDataFromWebsite():
    website_url="http://ekstrastats.pl/sezon-201617/"
    request=urllib.request.Request(website_url)
    response=urllib.request.urlopen(request)
    respData=response.read()
    respData=respData.decode("utf-8")
    soup=BeautifulSoup(respData,"html.parser")
    PlayersData=soup.find("table",attrs={"class":"tablepress tablepress-id-297"})
    PlayerNameSurname=re.findall(r'<td class="column-1">(.*?)</td>',str(PlayersData))
    PlayerTeam=re.findall(r'<td class="column-2">(.*?)</td>',str(PlayersData))
    PlayerPosition=re.findall(r'<td class="column-3">(.*?)</td>',str(PlayersData))
    Player=[]
    for i in range(len(PlayerNameSurname)):
        SubPlayer=(i+1,PlayerNameSurname[i],PlayerTeam[i],PlayerPosition[i])
        Player.append(SubPlayer)

    fname="Players.txt"
    with codecs.open(fname,"w","utf-8") as file:
        for indicator in range(len(Player)):
            file.write(str(indicator+1)+",")
            file.write(PlayerNameSurname[indicator]+",")
            file.write(PlayerTeam[indicator]+",")
            file.write(PlayerPosition[indicator]+os.linesep)
    file.close()


    print(Player)





LoadDataFromWebsite()