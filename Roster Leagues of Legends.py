import requests, xlsxwriter
from bs4 import BeautifulSoup as bs
import pandas as pd
r = requests.get("https://leagueoflegends.fandom.com/wiki/Champion")
soup = bs(r.text, 'html.parser')
champ = soup.find("ol", {"class": "champion_roster"})
name = [] #data-champion
title = [] #data-search
games = [] #data-game games a part of
type_champ = [] #data-type
role = [] #data-role
link = [] #'https://leagueoflegends.fandom.com/'+href
for roster in champ.findAll("li"):
	for tag in roster.findAll('span'):
		name.append(tag.get('data-champion'))
		title.append(tag.get('data-search'))
		games.append(tag.get('data-game'))
		type_champ.append(tag.get('data-type'))
		role.append(tag.get('data-role'))
	for tag2 in roster.findAll('a'):
		link.append('https://leagueoflegends.fandom.com/'+tag2.get('href'))

list_champs = pd.DataFrame(
    {'Name': name,
     'Title': title,
     'Games': games,
     'Champ Type': type_champ,
     'Role':role,
    })
path = r"leagueoflegendsChampions.xlsx"
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
list_champs.to_excel(writer, sheet_name = 'Roster')
writer.save()