import requests
import json
from urllib.request import Request, urlopen

link = input("➤ Provide cfx.re link: ")
response = requests.get("https://" + link)

try:
    ip = response.headers['X-Citizenfx-Url']
    print("IP: " + ip)
except:
    print("server blocked ip fetching")

req = Request('https://servers-frontend.fivem.net/api/servers/single/' + link.replace('cfx.re/join/', ''), headers={'User-Agent': 'Mozilla/5.0'})
sopen = urlopen(req, timeout=10)
data = json.loads(sopen.read())

class values:
    serversname = "\nServer hostname: " + data['Data']['hostname']
    gametype = "Gametype: " + data['Data']['gametype']
    onlineplayers = "\nOnline players: " + str(data['Data']['clients'])
    maxplayers = str(data['Data']['sv_maxclients'])
    resources = "\nServer resources: " + str(data['Data']['resources'])
    cbanner = "\nConnecting banner img path: " + data['Data']['vars']['banner_connecting']
    dbanner = "Detail banner img path: " + data['Data']['vars']['banner_detail']
    description = "\nServer description: " + data['Data']['vars']['sv_projectDesc']
    players = data['Data']['players']

print(values.serversname)
print(values.gametype)
print(values.onlineplayers + " / " + values.maxplayers)
print(values.resources)
print(values.cbanner)
print(values.dbanner)
print(values.description)
print("\nPlayers online:\n")

for name in values.players:
    print(name['name'])






