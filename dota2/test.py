import os
import requests
import pymysql
import time
import xml.etree.ElementTree as ET

file = open('apikey.txt')
apikey = file.read()
file.close()

r = requests.get('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v001/', 
params = {'format':'XML',
'key':apikey,
'start_at_match_seq_num':'2706339693'})
root = ET.fromstring(r.text)
matches = root.find('matches').findall('match')



endtimes = []
for match in matches:
    time = int(match.find('duration').text)+int(match.find('start_time').text)
    endtimes.append(time)
print(endtimes)
