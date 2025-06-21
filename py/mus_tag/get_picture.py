from mutagen.id3 import ID3, APIC
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from os.path import splitext


def get_picture(music_path):
    print('Task:')
    print('\x1b[31mmusic_path\x1b[m   : \x1b[32m', music_path, '\x1b[m', sep='')
    music_file = ID3(music_path)
    picture_list = music_file.getall('APIC')
    for picture in picture_list:
        save_picture(music_path, picture.data)


picture_id = 0
def save_picture(music_path, picture_data):
    global picture_id
    picture_id += 1
    picture_path = splitext(music_path)[0] + f'_picture{picture_id}.jpeg'
    print('Save:')
    print('\x1b[31mpicture_path\x1b[m : \x1b[32m', picture_path, '\x1b[m', sep='')
    with open(picture_path, 'wb') as picture_file:
        picture_file.write(picture_data)


def main():
    completer = PathCompleter()
    music_path = prompt('音乐 > ', completer=completer)
    get_picture(music_path)


if __name__ == '__main__':
    main()
