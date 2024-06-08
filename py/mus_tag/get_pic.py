from mutagen.id3 import ID3
from os.path import splitext
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

def get_pic(mus):
    print('deal music:', mus)
    audio = ID3(mus)
    pics = audio.getall('APIC')
    if len(pics) == 0:
        print('no picture found')
        return
    bin = pics[0].data
    save_pic(mus, bin)

def save_pic(mus, bin):
    root = splitext(mus)[0]
    picpath = root + '.jpg'
    with open(picpath, 'wb') as pic:
        pic.write(bin)

def main():
    com = PathCompleter()
    arr = []
    while True:
        mus = prompt('音乐/quit > ', completer=com)
        if mus.lower() in ('quit', 'q', ''):
            break
        arr.append(mus)
    for mus in arr:
        get_pic(mus)

if __name__ == '__main__':
    main()
