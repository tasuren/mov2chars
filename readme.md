# Mov2Chrs in Python
映像を文字に変換して再生できるやつ
Movie to Characters. And Play.

OpenCVが必要です。
OpenCV is required.

Only black and white movies are supported yet.

# How to use
### 日本語
mov2chrs convert <MP4> <OutPutTextFileName> <Size>
    テキストファイルにします。
    <Size>には整数を入れてください。
    数がでかいほどサイズは小さくなります。
    音楽を付けたいなら完成したテキストファイルの最初の数字の横に音楽ファイル名を書いてください。
    音楽ファイルはwav形式の必要があります。
mov2chrs play <TextFileName>
    convertで出力したテキストファイルを再生します。
mov2chrs play2 <TextFileName>
    メモリにテキストファイルの中身をすべてとってから再生します。
    メモリに余裕があり快適に再生したい場合はplayでなくこちらを使用してください。
    メモリに入れるのに失敗(MemoryError)になる場合はplayを使用してください。
### English (Translated by みらい翻訳)
```
mov2chrs convert <MP4> <OutPutTextFileName> <Size>
    Make it a text file.
    must be an integer.
    The larger the number, the smaller the size.
    If you want to add music, write the music file name next to the first number in the completed text file.
    Music files must be in wav format.
mov2 chrs play <TextFileName>
    Play the text file output by convert.
mov2 chrs play2 <TextFileName>
    Takes all the contents of the text file to memory and plays it.
    If you have enough memory and want to play it comfortably, use this instead of play.
    If memory fails (MemoryError), use play.
```
