from mutagen.id3 import ID3, TPE1
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter


def set_artist(music_path, artist):
    print('Task:')
    print('\x1b[31mmusic_path\x1b[m : \x1b[32m', music_path, '\x1b[m', sep='')
    print('\x1b[31martist\x1b[m      : \x1b[32m', artist, '\x1b[m', sep='')
    music_file = ID3(music_path)
    tag = TPE1(text=artist)
    music_file.setall('TPE1', [tag])
    music_file.save()


def main():
    completer = PathCompleter()
    music_path = prompt('音乐 > ', completer=completer)
    artist = prompt('artist > ')
    set_artist(music_path, artist)


if __name__ == '__main__':
    main()
