import os
a=os.listdir()
for b in a:
  c=os.path.splitext(b)[0]+'.mp3'
  os.system(f'ffmpeg -i {b} {c}')
