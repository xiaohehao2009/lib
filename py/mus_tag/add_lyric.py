from mutagen.id3 import ID3, USLT, Encoding
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.validation import Validator


def add_lyric(music_path, lyric_path, encoding):
    print('Task:')
    print('\x1b[31mmusic_path\x1b[m : \x1b[32m', music_path, '\x1b[m', sep='')
    print('\x1b[31mlyric_path\x1b[m : \x1b[32m', lyric_path, '\x1b[m', sep='')
    music_file = ID3(music_path)
    with open(lyric_path) as lyric_file:
        lyric_text = lyric_file.read().strip('\n\r')
    tag = USLT(text=lyric_text, encoding=encoding)
    music_file.setall('USLT', [tag])
    music_file.save()


def main():
    completer = PathCompleter()
    validator = Validator.from_callable(lambda x: x.lower() in ('y', 'yes', 'n', 'no', ''))
    music_path = prompt('音乐 > ', completer=completer)
    lyric_path = prompt('歌词 > ', completer=completer)
    utf16 = prompt('UTF16 (y)/n > ', validator=validator)
    if utf16.lower() in ('n', 'no'):
        encoding = Encoding.UTF8
    else:
        encoding = Encoding.UTF16
    add_lyric(music_path, lyric_path, encoding)


if __name__ == '__main__':
    main()
