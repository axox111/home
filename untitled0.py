import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

print('start после закрытия драйвера, хром остается в процессах и жрет проц. надо убить')
rep_link = ''
rep_name = ''
col_name = 'имя'
start_date = False
start_date = datetime.date(2024, 4, 14)

url_guild = 'https://www.warcraftlogs.com/guild/reports-list/609627'
url_report = 'https://www.warcraftlogs.com'

url_kills = '#boss=-2&difficulty=0&wipes=2'
url_wipes = '#boss=-2&difficulty=0&wipes=1'
url_all_encounters = '#boss=-2&difficulty=0'

url_damage_done = '&type=damage-done'
url_damage_taken = '&type=damage-taken'

response = requests.get(url_guild)
soup = BeautifulSoup(response.text, 'html.parser')
reports = soup.find_all('tr')
arr_rep_link = []
arr_rep_date = []
arr_rep_name = []
arr_link_size = 0
arr_names = []
arr_damage =[]
all_raids_members = []
uniq_raids_members = pd.Series()
i = 0
j = 0
dataframes = []
dd_cols = []
dt_cols = []
type_of_reports = int(input('kills - type "1"/wipes - type "2" /all - type "3"? '))
print('ok, lets go')

while i < len(reports):
    rep_time = int(reports[i].find('span').text[:-1])
    convert_rep_time = datetime.date.fromtimestamp(rep_time)
    if start_date is not False:
        if convert_rep_time < start_date:
            break
    rep_link = reports[i].find('a').get('href')
    rep_name = reports[i].find('a').text
    arr_rep_date.append(convert_rep_time)
    arr_rep_link.append(rep_link)
    arr_rep_name.append(rep_name)
    i += 1
    
arr_link_size = len(arr_rep_link)

if type_of_reports == 1:
    url_option = url_kills
elif type_of_reports == 2:
    url_option = url_wipes
elif type_of_reports == 3:
    url_option = url_all_encounters
    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  # Запуск в headless режиме (без графического интерфейса)
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--disable-javascript")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-prefetch")
chrome_options.add_argument("--disable-accelerated-2d-canvas")


for rep in range(arr_link_size):
    print(arr_link_size)
    driver = webdriver.Chrome(options=chrome_options)
    arr_names_dd = []
    arr_names_dt = []
    driver.get(url_report + arr_rep_link[rep] + url_option + url_damage_done)
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "main-table-0_wrapper"))
        )
    soup_dd = BeautifulSoup(driver.page_source, 'html.parser') 
    table_dd = soup_dd.find(id="main-table-0_wrapper")
    # time.sleep(60)
    field_name_dd = table_dd.find_all(class_="main-table-name report-table-name")
    field_damage_dd = table_dd.find_all(class_="tooltip report-table-amount main-table-amount sorting_1")
    for name_dd, damage in zip(field_name_dd, field_damage_dd):
        player_name_dd = str(name_dd.text).replace('\n', '')
        player_damage = str(damage.text)[
            0:str(damage.text).find('$')
            ].replace('\n', '')
        all_raids_members.append(player_name_dd)
        uniq_raids_members = pd.Series(data=all_raids_members)
        arr_names_dd.append(player_name_dd + ',' + str(float(player_damage)/1000000))
    driver.close()
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_report + arr_rep_link[rep] + url_option + url_damage_taken)
    soup_dt = BeautifulSoup(driver.page_source, 'html.parser')
    table_dt = soup_dt.find(id="main-table-0_wrapper")
    # time.sleep(60)
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "main-table-0_wrapper"))
        )
    field_name_dt = table_dt.find_all(class_="main-table-name report-table-name")
    field_dtaken = table_dt.find_all(class_="tooltip report-table-amount main-table-amount sorting_1")
    for name_dt, dtaken in zip(field_name_dt, field_dtaken):
        player_name_dt = str(name_dt.text).replace('\n', '')
        player_dtaken = str(dtaken.text)[
            0:str(dtaken.text).find('$')
            ].replace('\n', '')
        arr_names_dt.append(player_name_dt + ',' + str(float(player_dtaken)/1000000))
    driver.close()

    file_dd_name = str(arr_rep_date[rep]) + arr_rep_name[rep] +' damage_done'
    file_dt_name = str(arr_rep_date[rep]) + arr_rep_name[rep] +' damage_taken'
    
    arr_names_dd = [dd_item.split(',') for dd_item in arr_names_dd]
    arr_names_dt = [dt_item.split(',') for dt_item in arr_names_dt]
    df_dd = pd.DataFrame(arr_names_dd, 
                         columns=['имя' , 
                                  f'{arr_rep_name[rep]} {arr_rep_date[rep]} урон'])
    dd_cols.append(f'{arr_rep_name[rep]} {arr_rep_date[rep]} урон')
    df_dt = pd.DataFrame(arr_names_dt, 
                         columns=['имя', 
                                  f'{arr_rep_name[rep]} {arr_rep_date[rep]} полученый урон'])
    dt_cols.append(f'{arr_rep_name[rep]} {arr_rep_date[rep]} полученый урон')
    uniq_raids_members = pd.Series(uniq_raids_members.unique(), name=col_name)
    
    merge_df = pd.merge(uniq_raids_members, df_dd, on = 'имя')    
    merge_df = pd.merge(merge_df, df_dt, on = 'имя')    
    dataframes.append(merge_df)
    arr_link_size -= 1

attendance = []
for player in uniq_raids_members:
        attendance.append(
            {
                'имя' : player,
                'посещаемость': str(all_raids_members.count(player))
            }
            )
df_attendance = pd.DataFrame(data = attendance)
for df in dataframes:
    df_attendance = pd.merge(df_attendance,  df, how = 'left', on = 'имя')
df_attendance[dd_cols] = df_attendance[dd_cols].astype (float)
df_attendance[dt_cols] = df_attendance[dt_cols].astype (float)
df_attendance['посещаемость'] = df_attendance['посещаемость'].astype (int)

df_attendance['dd_sum'] = df_attendance[dd_cols].sum(axis=1)
df_attendance['dt_sum'] = df_attendance[dt_cols].sum(axis=1)
df_attendance['NU CHE POJDESH V MYTHIC?????'] = (
    (
     df_attendance['dd_sum'] - df_attendance['dt_sum']
     ) /
    df_attendance['посещаемость']
    )
sort_df_attendance = df_attendance.sort_values(by=['NU CHE POJDESH V MYTHIC?????'], ascending = False)
sort_df_attendance.to_csv('all_data.csv', index=False)
sort_df_attendance.to_csv('names_coefs.csv', index=False, columns=
                     [
                         'имя',
                         'посещаемость',
                         'NU CHE POJDESH V MYTHIC?????'
                         ]
                     )

print('DONE! после закрытия драйвера, хром остается в процессах и жрет проц. надо убить')