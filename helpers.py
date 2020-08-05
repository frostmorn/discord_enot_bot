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

def get_apm_message(replay_file):
    w3g_object = w3g.File(replay_file)
    bug_timecodes = []
    acts = {p.id: 0 for p in w3g_object.players}
    chats = []
    for e in w3g_object.events:
        if e.apm:
            acts[e.player_id] += 1
        if isinstance(e, w3g.Chat):
            if "!bug" in str(e):
                chats.append(e) 
                if "00.000" not in e.strtime():
                    bug_timecodes.append(e.strtime()) 
    mins = w3g_object.clock / (60 * 1000.0)
    
    m = "Actions per minute over {0:.3} min\r\n".format(mins)
    print('-' * len(m))
    message = m
    for pid, act in sorted(acts.items()):
        if act == 0:
            continue
        message = message + "  {0}\t:\t{1:.5}\r\n".format(w3g_object.player_name(pid), act/mins)
    while '/' in replay_file:
        replay_file = replay_file[replay_file.find('/')+1:]
    if len(bug_timecodes) > 0:
        message = message + "Bug Timecodes detected! \r\n"+"Timecodes: " + " ".join(bug_timecodes)+"\r\n"
    message = '```'+"Replay "+replay_file + "\r\n "+ message+'```'
    return message

def calc_sha(filename):
    file_hash = hashlib.sha1()
    with open(filename, 'rb') as f:
        fb = f.read(1024) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(1024) # Read the next block from the file
        f.close()
        return file_hash.hexdigest()