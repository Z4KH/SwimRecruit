import requests
from bs4 import BeautifulSoup

urlPart1 = "https://www.swimcloud.com/times/iframe/?dont_group=false&event=11000&gender=F&page=1&region&season_id=26&tag_id&team_id="
urlPart2 = "&year=2023"

for team_id in range(1, 656, 1):
    fullURL = urlPart1 + str(team_id) + urlPart2

    req = requests.get(fullURL)
    soup = BeautifulSoup(req.content, "html.parser")

    time = soup.find(class_ = "u-text-semi u-text-end")

    if time == None:
        continue
    
    timeArray = soup.findAll(class_ = "u-text-semi u-text-end", limit = 8)

    timeLength = len(timeArray)

    if timeLength < 2:
        time = str(timeArray[timeLength - 1].text)

        if time.find(':') != -1:
            minute = int(time.split(':')[0])
            time = minute * 60 + float(time.split(':')[1])
        time = str(time) + ','
        print(time)
    else:
        time = str(timeArray[1].text)
        if time.find(':') != -1:
            minute = int(time.split(':')[0])
            time = minute * 60 + float(time.split(':')[1])
        time = str(time) + ","
        print(time)
        
