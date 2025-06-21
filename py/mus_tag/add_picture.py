from mutagen.id3 import ID3, APIC
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.validation import Validator
from os.path import splitext


def add_picture(music_path, picture_path, picture_data, save):
    print('Task:')
    print('\x1b[31mmusic_path\x1b[m   : \x1b[32m', music_path, '\x1b[m', sep='')
    print('\x1b[31mpicture_path\x1b[m : \x1b[32m', picture_path, '\x1b[m', sep='')
    music_file = ID3(music_path)
    picture_list = music_file.getall('APIC')
    if save:
        for picture in picture_list:
            save_picture(music_path, picture.data)
    tag = APIC(mime='image/jpeg', data=picture_data)
    music_file.setall('APIC', [tag])
    music_file.save()


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
    validator = Validator.from_callable(lambda x: x.lower() in ('y', 'yes', 'n', 'no', ''))
    music_path_list = []
    while True:
        music_path = prompt('音乐 > ', completer=completer)
        if not music_path:
            break
        music_path_list.append(music_path)
    picture_path = prompt('照片 > ', completer=completer)
    save_input = prompt('原图保存 (y)/n > ', validator=validator)
    if save_input.lower() in ('n', 'no'):
        save = False
    else:
        save = True
    with open(picture_path, 'rb') as picture_file:
        picture_data = picture_file.read()
    for music_path in music_path_list:
        add_picture(music_path, picture_path, picture_data, save)


if __name__ == '__main__':
    main()
