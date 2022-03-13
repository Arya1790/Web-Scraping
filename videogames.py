import requests, openpyxl
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best"

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel. active
sheet.title = 'Top video games'
sheet.append(['Game','Genre','Platform'])
print(excel.sheetnames)

try:
    source = requests.get(url)
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,'html.parser')
    
    game = soup.find('table',class_='wikitable sortable').find('tbody').findAll('tr')
    
    
    for g in game:
        cell = g.findAll('td')
        year = g.findAll('th')
        print(len(cell))
        if len(cell) == 5:
            name = cell[0].find(text=True)
            genre = cell[1].find(text=True)
            publisher = cell[2].find(text=True)
            #  y = year[0].find(text=True)
            print(name)
            print(genre)
            print(publisher)
            
            sheet.append([name, genre, publisher])
 
except Exception as e:
    print(e)
    
excel.save('game.xlsx')

