# Friday Night Funkin Cheat - this is for fun, play the game some time lazy ass
import os
import re
print('[+] Getting funkin.sol file...')
appdata = os.getenv('APPDATA')
with open(appdata + '\\ninjamuffin99\\Funkin\\ninjamuffin99\\funkin.sol', 'r') as o:
    data = o.read()
    o.close()

# Parsing Scores

scores = ['0']
print('[+] Done! Scores Read.')
scoretoset = str(input('What score would you want to set to all songs?\n> '))
print('[+] Setting Scores...\n')
for d in range(10, len(data.split(':'))):
    songdata = data.split(':')[d]
    t = re.compile('i[0-9]+y')
    if t.search(songdata) != None:
        songnscore = songdata.rsplit('y', 1)[0].rsplit('i', 1)
        data = data.replace(songnscore[1], scoretoset, 1)
        print('[-] Modified Score for ' + songnscore[0] + ': ' + songnscore[1] + '->' + scoretoset)
    else:
        pass


# Writing Scores
print('\n[+] Done! Replacing funkin.sol with Modified Data...')
with open(appdata + '\\ninjamuffin99\\Funkin\\ninjamuffin99\\funkin.sol', 'w') as o:
    o.write(data)
    o.close()
print('[+] Written! Check your scores :P')
