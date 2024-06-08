from mutagen.easyid3 import EasyID3
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

artist = prompt('艺术家/quit > ')
if artist.lower() in ('quit', 'q'):
    return
com = PathCompleter()
arr = []
while True:
    mus = prompt('音乐/quit > ', completer=com)
    if mus.lower() in ('quit', 'q', ''):
        break
    arr.append(mus)

for mus in arr:
    print('deal music:', mus)
    id3 = EasyID3(mus)
    id3['albumartist'] = artist
    id3.save()
