# AudioStream
這是一個實驗性的音訊工具，此工具有五種不同的功能，詳細介紹如下：
### 錄製音訊
使用[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)錄製麥克風音訊，音訊格式為本工具自定義的檔案類型(.as)，此檔案類型可以確保錄音過程意外中斷時保留中斷前的所有內容。
預設檔案名稱為"audio<area>.</area>as"，預設檔案最大為10MB
### .as轉.wav
使用[ffmpeg](https://ffmpeg.org/)將自定義的<area>.</area>as檔轉為<area>.</area>wav檔，若發現轉檔後聲音變高、變低或任何預期外的狀況，請視情況調整音訊參數。
預設輸入檔案為"audio<area>.</area>as"，預設輸出檔案為"audio<area>.</area>wav"
### .mp3轉.wav
使用[pydub](http://pydub.com/)將<area>.</area>mp3檔轉為<area>.</area>wav檔。
預設輸入檔案為"audio<area>.</area>mp3"，預設輸出檔案為"audio<area>.</area>wav"
### 播放音訊
播放<area>.</area>wav類型的音訊檔。
預設播放檔案為"audio<area>.</area>wav"
### 語音辨識
使用[SpeechRecognition](https://github.com/Uberi/speech_recognition)將<area>.</area>wav音訊檔中的語音內容辨識為文字，提供Google Speech Recognition API及CMU Sphinx兩種方法進行辨識，其中CMU Sphinx需自行提供語音辨識模型。
預設語音辨識方法為Google Speech Recognition API，預設音訊檔案為"audio<area>.</area>wav"，預設辨識語言為中文
