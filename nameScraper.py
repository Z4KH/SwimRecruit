import requests
from bs4 import BeautifulSoup

urlPart1 = "https://www.swimcloud.com/team/"
urlPart2 = "/times/?dont_group=false&event=11000&gender=F&page=1&region&season_id=26&tag_id&team_id="
urlPart3 = "&year=2023"

urlPart21 = "https://www.swimcloud.com/times/iframe/?dont_group=false&event=11000&gender=F&page=1&region&season_id=26&tag_id&team_id="
urlPart22 = "&year=2023"

for team_id in range(1,656,1):
    fullURL = urlPart1 + str(team_id) + urlPart2 + str(team_id) + urlPart3
    fullURL2 = urlPart21 + str(team_id) + urlPart22

    req = requests.get(fullURL)
    soup = BeautifulSoup(req.content, "html.parser")

    req2 = requests.get(fullURL2)
    soup2 = BeautifulSoup(req2.content, "html.parser")

    time = soup2.find(class_ = "u-text-semi u-text-end")

    if time == None:
        continue

    name = soup.find(class_ = "c-toolbar__title")
    name = name.text 
    name = name + '", "'
    print(name)