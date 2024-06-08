from mutagen.id3 import ID3, USLT, Encoding
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.validation import Validator

def add_lyric(music_file, lyric_file, encoding):
    print('deal music:', music_file, 'lyric:', lyric_file)
    music = ID3(music_file)
    with open(lyric_file) as file:
        lyric = file.read().strip('\n\r')
    music.setall('USLT', [USLT(format=1, type=2, text=lyric, encoding=encoding)])
    music.save()

def main():
    com = PathCompleter()
    val = Validator.from_callable(lambda x: x.lower() in ('y', 'yes', 'n', 'no', 'q', 'quit'))
    mus = prompt('音乐/quit > ', completer=com)
    if mus.lower() in ('quit', 'q'):
        return
    lyr = prompt('歌词/quit > ', completer=com)
    if lyr.lower() in ('quit', 'q'):
        return
    uni = prompt('Unicode (y/n/quit) > ', validator=val)
    if uni.lower() in ('quit', 'q'):
        return
    if uni.lower() in ('y', 'yes'):
        enc = Encoding.UTF8
    else:
        enc = Encoding.UTF16
    add_lyric(mus, lyr, enc)

if __name__ == '__main__':
    main()
