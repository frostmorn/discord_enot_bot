import json
import w3g
import requests
import hashlib
import os
import platform

def monospace_message(message):
    return "```"+message+"```"

def monospace_solarized_green_message(message):
    return "```CSS\r\n"+message+"```"

def monospace_solarized_cyan_message(message):
    return "```yaml\r\n"+message+"```"

def monospace_solarized_yellow_message(message):
    return "```fix\r\n"+message+"```"

def monospace_solarized_red_message(message):
    return "```diff\r\n- "+message+"```"        

async def get_request(url):
    r = requests.get(url)
    return r



async def download_file(url,  filename):
    print('Downloading new file to bot')
    r = requests.get(url, filename)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        f.close()

def get_apm_data(replay_file):
    # map_data_file = open("map_data.txt")
    # map_data = json.loads(map_data_file.read())

    w3g_object = w3g.File(replay_file)
    # bug_timecodes = []
    acts = {p.id: 0 for p in w3g_object.players}
    # chats = []
    
    for e in w3g_object.events:


        # event = str(e)
        # for key in map_data.keys():
        #     if key in event:
        #         try:
        #             event = event.replace(key, map_data[key]["Level 1 - Text - Name"])
        #         except:
        #             event = event.replace(key, map_data[key]["Text - Name"])
        # shit = ["PreSubselect","AbilityPositionObject","ScenarioTrigger", "AssignGroupHotkey", "ChangeSelection", "MapTriggerChatCommand", "HeroSkillSubmenu"]
        # skip = 0
        # for shitness in shit:
        #     if shitness in event:
        #         skip = 1
        # if not skip:
        #     print(event.replace("b'","").replace("'", ""))
        if e.apm:
            acts[e.player_id] += 1
                        # for player in w3g_object.players:
                        #     if player.id == e.player_id and e.apm:

                        #         if hasattr(e, "loc"):
                        #             print("[",e.strtime(),"]",player.name, "used an ability", ability_data[e.ability.decode()]["Text - Name"], "at location",e.loc)
                        #         else:
                        #             print("[",e.strtime(),"]",player.name, "used an ability", ability_data[e.ability.decode()]["Text - Name"])
                    
        # if isinstance(e,w3g.Ability):
        #     if hasattr(e, "loc"):
        #         # print(e)
        #         print( e.loc[0], ";",e.loc[1],";")
        # if isinstance(e, w3g.Chat):
        #     print(e)
            # if "!bug" in str(e):
            #     chats.append(e) 
            #     if "00.000" not in e.strtime():
            #         bug_timecodes.append(e.strtime()) 
    mins = w3g_object.clock / (60 * 1000.0)
    
    m = "Actions per minute over {0:.3} min\r\n".format(mins)
    print('-' * len(m))
    apm_data = []
    for pid, act in sorted(acts.items()):
        if act == 0:
            continue
        apm_data.append(
                    {   
                        "player":w3g_object.player_name(pid),
                        "apm":act/mins
                    })
    return apm_data

def calc_sha(filename):
    file_hash = hashlib.sha1()
    with open(filename, 'rb') as f:
        fb = f.read(1024) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(1024) # Read the next block from the file
        f.close()
        return file_hash.hexdigest()
def get_leaderboard():
    headers = {
        'authority': 'mee6.xyz',
        'accept': 'application/json',
        'x-fingerprint': '742980895044280320.7WHPgTg-JWtDc2dr4FEwl6rV2aw',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'authorization': 'YTE4YjNiZTAzODAwMDAz.NWYzMzgwZTY=.71n0AXc2F-OBiEvVE9damnepNhc',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mee6.xyz/leaderboard/598903919602696202',
        'accept-language': 'en-GB,en;q=0.9,ru-UA;q=0.8,ru;q=0.7,uk-UA;q=0.6,uk;q=0.5,en-US;q=0.4',
        'cookie': '__cfduid=d560f24d29c6159686715f22ab7f7e9bc1597210843; session=eyJzdGF0ZSI6IjQ2R0NVc2lQazVFNzJrSDlwbHRNWGZIVEMxd25WYyJ9.XzOA4w.A6Wj9OWsMTz1Vn2n3WzgwnxxLu4; crisp-client%2Fsession%2F12794dee-08f5-4047-ac85-6ea6b8af6005=session_d54f9e52-1a0a-4961-bd47-1754837a9ff2',
    }

    response = requests.get('https://mee6.xyz/api/plugins/levels/leaderboard/598903919602696202', headers=headers)
    exp_data = json.loads(response.content.decode('utf-8'))
    return exp_data

if __name__ == "__main__":
    print(get_apm_data("GHost_2020-08-31_07-56__Life_In_Arena_-vc4__l_09m05s.w3g"))