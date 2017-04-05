import os
import requests

r = requests.get('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/', 
params = {'format':'XML',
'key':'A2378FD5FA20FDC79CC0BAA78675F631',
'skill':'1',
'min_players':'10',
'league_id':'0',
'start_at_match_id':'3099116571'})
print(r.text)
