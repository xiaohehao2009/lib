import os
from sys import exit
from mutagen.easyid3 import EasyID3


def request_bool(prompt, default):
    if default == True:
        suffix = '[Y]/n: '
    else:
        suffix = 'Y/[n]: '
    message = f'{prompt} {suffix}'
    while True:
        u = input(message).strip()
        if u == '':
            return default
        if u == 'y' or u == 'Y':
            return True
        if u == 'n' or u == 'N':
            return False


print('请确保你已经 cd 到音乐所在目录下且该目录下无其它文件或文件夹!')
print('接下来任何时间如果反悔请按 Ctrl+C 或 Ctrl+D 退出!')


musics = os.listdir()
musics.sort()
trackprefix = request_bool('是否通过音乐文件前缀指定 tracknumber?', False)
titlemidfix = request_bool('是否通过音乐文件中缀指定 title?', True)
album = input('输入 album: ')
artist = input('输入 artist: ')
albumartist = input('输入 albumartist (留空以使用 artist): ')
if albumartist == '':
    albumartist = artist
discnumber = input('输入 discnumber: ')


last_tracknumber = 0
for i, file in enumerate(musics):
    print(f'第 {i} 项: \x1b[32m{file}\x1b[0m')
    if not trackprefix:
        if last_tracknumber == 0:
            increase_track = False
        else:
            increase_track = request_bool('是否根据前面的 tracknumber 递增?', True)
        if increase_track:
            last_tracknumber += 1
            tracknumber = str(last_tracknumber)
        else:
            tracknumber = input('请指定 tracknumber: ')
            last_tracknumber = int(tracknumber)
    else:
        buf = ''
        t = file
        while len(t) != 0 and '0' <= t[0] <= '9':
            buf += t
        if len(buf) == 0:
            print('当前音乐文件无法解析前缀 tracknumber, 请自行检查')
            print('在下次运行本脚本之前, 修复你的音乐文件的文件名, 或者自己指定 tracknumber')
            exit()
        tracknumber = buf
    if not titlemidfix:
        title = input('请指定 title: ')
    else:
        title = os.path.splitext(file)[0].lstrip('0123456789 -._')
    print('接下来对音乐文件进行 entag')
    print('title:', title)
    print('album:', album)
    print('artist:', artist)
    print('albumartist:', albumartist)
    print('discnumber:', discnumber)
    print('tracknumber:', tracknumber)
    input('回车以继续...')
    m = EasyID3(file)
    m['title'] = title
    m['album'] = album
    m['artist'] = artist
    m['albumartist'] = albumartist
    m['discnumber'] = discnumber
    m['tracknumber'] = tracknumber
    m.save()
print('完毕!')
