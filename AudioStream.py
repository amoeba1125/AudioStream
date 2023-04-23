import os
import pyaudio
import wave
import keyboard
from pydub import AudioSegment
from pydub.playback import play
import io
import subprocess
import time

CHUNK_SIZE = 1024  # 每個音訊分段的大小
FILE_NAME = "audio.as"  # 設定音訊檔案名稱
OUTPUT_NAME = "audio.wav"   # 設定轉檔後名稱
FILE_SIZE_LIMIT = 1024 * 1024 * 10  # 設定檔案大小上限，10MB

def write_audio_chunk(data):
    # 確定檔案是否存在
    if os.path.isfile(FILE_NAME):
        # 確定檔案大小是否已達上限
        if os.path.getsize(FILE_NAME) > FILE_SIZE_LIMIT:
            print("檔案大小已達上限，無法寫入。")
            return
        # 開啟檔案並寫入音訊分段資料
        with open(FILE_NAME, "ab") as f:
            f.write(data)
    else:
        # 檔案不存在，建立新檔案並寫入音訊分段資料
        with open(FILE_NAME, "wb") as f:
            print("建立新檔")
            f.write(data)

def record_audio():
    # 刪除現有的檔案
    if os.path.isfile(FILE_NAME):
        os.remove(FILE_NAME)
    # 初始化PyAudio
    p = pyaudio.PyAudio()
    # 開啟音訊輸入
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)
    # 循環讀取音訊資料並寫入到檔案中
    while True:
        data = stream.read(CHUNK_SIZE)
        write_audio_chunk(data)
        # 檢查是否偵測到Enter鍵被按下
        if keyboard.is_pressed('enter'):
            break

def transformat_audio():
    # 刪除現有的檔案
    if os.path.isfile(OUTPUT_NAME):
        os.remove(OUTPUT_NAME)
    # 使用ffmpeg將音訊檔案轉換成WAV格式
    subprocess.call(["ffmpeg", "-f", "s16le", "-ar", "44100", "-ac", "1", "-i", FILE_NAME, OUTPUT_NAME])

def play_audio():
    audio_chunks = []
    # 檢查檔案是否存在
    if os.path.isfile(OUTPUT_NAME):
        with open(OUTPUT_NAME, "rb") as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                audio_chunks.append(data)
    else:
        print("音訊檔案不存在。")

    audio_data = b"".join(audio_chunks)
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
    play(audio_segment)

char = input("r:錄製音訊\nt:音訊轉檔\np:播放音訊\n\n輸入：")
if char == "r":
    record_audio()
elif char == "t":
    transformat_audio()
elif char == "p":
    play_audio()
else:
    print("輸入錯誤")
