from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd, openpyxl, os
driver = webdriver.Chrome()
url= "https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics"
driver.maximize_window()
driver.get(url)
content = driver.page_source.encode('utf-8').strip()
soup = bs(content,"html.parser")
df = pd.read_html(content)
cols = list(df[0].columns.values)
df[1].columns = cols
print(df[1])
driver.quit()
path = r"leagueoflegendsChampions.xlsx"
writer = pd.ExcelWriter(path, engine = 'openpyxl')
if os.path.exists("leagueoflegendsChampions.xlsx"):
    book = openpyxl.load_workbook("leagueoflegendsChampions.xlsx")
    writer.book = book
df[1].to_excel(writer, sheet_name = 'Base Statistics')
writer.save()