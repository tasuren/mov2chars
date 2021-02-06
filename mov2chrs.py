import cv2

try:from winsound import PlaySound,SND_FILENAME,SND_ASYNC
except ImportError as e:print(e)
from time import sleep,time
from sys import argv


version = 1.0
description = f"""Mov2Chrs {version} by tasuren

mov2chrs convert <MP4> <OutPutTextFileName> <Size>
    テキストファイルにします。
    <Size>には整数を入れてください。
    数がでかいほどサイズは小さくなります。
mov2chrs play <TextFileName>
    convertで出力したテキストファイルを再生します。
mov2chrs play2 <TextFileName>
    メモリにテキストファイルの中身をすべてとってから再生します。
    メモリに余裕があり快適に再生したい場合はplayでなくこちらを使用してください。
    メモリに入れるのに失敗(MemoryError)になる場合はplayを使用してください。"""


def mov2chrs(video_path,output_path,grafic=2):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():return print('ファイルの読み込みに失敗しました。')

    data,c = "",0
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    turn = grafic
    turnx,turny = 0,0

    with open(output_path,mode="w") as f:
        f.write(str(cap.get(cv2.CAP_PROP_FPS))+"|"+"\n")

    while True:
        ret,frame = cap.read()
        c += 1
        if ret:
            width, height, channels = frame.shape
            for x in range(0, width):
                turny += 1
                if turny != grafic:continue
                else:turny = 0
                for y in range(0, height):
                    turnx += 1
                    if turnx != grafic // 2:continue
                    else:turnx = 0
                    try:data += " " if frame[x,y,0] + frame[x,y,1] + frame[x,y,2] == 0 else "#"
                    except IndexError:pass
                data += "\n"
            data += "\nXXX"
            if len(data) > 593052:
                with open(output_path,mode="a") as f:
                    f.write(data)
                data = ""
            p = int(c/frames*100)
            print("\r"+str(p)+"% ["+"#"*p+"-"*(100-p)+"]",end="")
        else:
            with open(output_path,mode="a") as f:
                f.write(data)
            break


def wait(start,fps,next_,now=0,sa=0):
    while not (float(next_) / fps <= sa):sa = time() - start

def show(data,fps):
    frame,start = 0,time()
    for d in data:
        print(d[:-1],end="",flush=True)
        wait(start,fps,frame)
        frame += 1

def play2(path):
    with open(path,mode="r") as f:data = f.read()

    fps,music = float(data[:data.find("|")]),data[data.find("|")+1:data.find("\n")]
    data = data.split("XXX")
    start,frame = time(),0

    if music:
      try:PlaySound(music,SND_FILENAME | SND_ASYNC)
      except Exception as e:print(e)

    try:show(data,fps)
    except KeyboardInterrupt:pass
    print("Bye")

def play(path):
    frame,start = 0,time()
    f = open(path,mode="r")

    data = f.readline()
    fps,music = float(data[:data.find("|")]),data[data.find("|")+1:data.find("\n")]
    print(fps)
    if music:
      try:PlaySound(music,SND_FILENAME | SND_ASYNC)
      except Exception as e:print(e)

    try:
        while data:
            data = ""
            while not "XXX" in data:data += f.readline()

            print(data[:data.find("XXX")-1],end="",flush=True)
            wait(start,fps,frame)
            frame += 1
            data = f.readline()
    except KeyboardInterrupt:
        pass
    print("Bye")


if __name__ == "__main__":
    if len(argv) < 3:
        print(description)
    else:
        if argv[1] == "convert" and len(argv) == 5:
            mov2chrs(argv[2],argv[3],int(argv[4]))
        elif argv[1] == "play":
            play(argv[2])
        elif argv[1] == "play2":
            play2(argv[2])
        else:
            print(description)

