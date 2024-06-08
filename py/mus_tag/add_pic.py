from mutagen.id3 import ID3, APIC
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.validation import Validator
from sys import argv
from os.path import join, dirname

def add_picture(pic, mus, cov):
    print('deal music:', file, 'picture:', pic)
    audio = ID3(mus)
    audio.update_to_v23()
    pics = audio.getall('APIC')
    if len(pics) > 0 and cov:
        path = save_pic(pics[0].data)
        print('saved to', path)
        return
    audio.setall('APIC', [APIC(
        encoding=0,
        mime='image/jpeg',
        type=3,
        data=pic
    )])
    audio.save()

def save_pic(bin):
    file = join(dirname(__file__), 'last.jpeg')
    with open(file, 'wb') as f:
        f.write(bin)
    return file

def main():
    com = PathCompleter()
    val = Validator.from_callable(lambda x: x.strip().lower() in ('y', 'yes', 'n', 'no', 'q', 'quit', ''))
    pic = prompt('照片/quit > ', completer=com)
    if pic.lower() in ('quit', 'q'):
        return
    arr = []
    while True:
        mus = prompt('音乐/quit > ', completer=com)
        if mus.lower() in ('quit', 'q', ''):
            break
        arr.append(mus)
    cov_ = prompt('强制覆盖 (n)/y/quit > ', validator=val)
    if cov_.lower() in ('quit', 'q'):
        return
    if cov_.lower() in ('y', 'yes'):
        cov = True
    else:
        cov = False
    with open(pic, 'rb') as file:
        bin = file.read()
    for mus in arr:
        set_song_picture(bin, mus, cov)

if __name__ == '__main__':
    main()
