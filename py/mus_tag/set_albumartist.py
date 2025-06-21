from mutagen.id3 import ID3, TPE2
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter


def set_albumartist(music_path, albumartist):
    print('Task:')
    print('\x1b[31mmusic_path\x1b[m  : \x1b[32m', music_path, '\x1b[m', sep='')
    print('\x1b[31malbumartist\x1b[m : \x1b[32m', albumartist, '\x1b[m', sep='')
    music_file = ID3(music_path)
    tag = TPE2(text=albumartist)
    music_file.setall('TPE2', [tag])
    music_file.save()


def main():
    completer = PathCompleter()
    music_path = prompt('音乐 > ', completer=completer)
    albumartist = prompt('albumartist > ')
    set_albumartist(music_path, albumartist)


if __name__ == '__main__':
    main()
