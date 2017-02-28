import spotipy
import subprocess
import time
import sys

# ARGS
song = sys.argv[1]
startTime = sys.argv[2]
endTime = sys.argv[3] # can either be end time or sleep time (depending on if its less than start time)
repeats = sys.argv[4]

# Search for the song online
sp = spotipy.Spotify()
result = sp.search(q=song, limit=20)['tracks']['items'][0]
resultid = result['id']

# Tell local spotify player to play the song
# and tell it to loop it from position a to b

apple_script_call = ['osascript', '-e', 'tell application "Spotify" to play track "spotify:track:' + resultid + '"']
subprocess.call(apple_script_call)
for num in range(0,int(repeats)):
   apple_script_call = ['osascript', '-e', 'tell application "Spotify" to set player position to ' + startTime]
   subprocess.call(apple_script_call)
   if endTime < startTime:
      time.sleep(float(endTime))
   else:
      time.sleep(float(endTime) - float(startTime))


# Some songs I've been using it with

# python spotifylooper.py "star stealers wheel" 16 50.8 2
# python spotifylooper.py "dashboard modest mouse" 0 7 20
# python spotifylooper.py "hurt johnny cash" 13 34 2
   #12 33.6 53