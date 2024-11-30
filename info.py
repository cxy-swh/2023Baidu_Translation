import requests
import pyttsx3
def speak(text):
    # engine = pyttsx3.init()("sapi5")  # 设定语音引擎为 "sapi5"，这是 Windows 平台上的一个文本到语音 API。如果不指定参数，则会使用默认的语音引擎。
    engine = pyttsx3.init()   # 初始化语音引擎
    engine.setProperty("volume", 1)  # 设置音量（0.0-1.0之间）
    engine.setProperty("rate",150)  # 设置语速（默认为200）
    engine.say(text)       # 将文本传递给语音引擎，让它朗读出来
    engine.runAndWait()   # 等待语音引擎朗读完毕

while True:
    url = 'https://fanyi.baidu.com/sug'
    print("参数:\n"
          "[-t]朗读\n")
    s = input('中/英翻译:')
    dat = {
        "kw": s.replace("-t","").replace(" ","")
    }
    resp = requests.post(url, data=dat)
    respt = resp.json()["data"]
    shutdyy = []
    for i in respt:
        # sssjj = i["h"]
        name = i["k"]
        shuj = i["v"]
        print("{}\t\t| {} |\n".format(name,shuj))
        shutdyy.append([name,shuj])
    if s.__contains__("-t"):
        for shutdyy in shutdyy:
            shssw = shutdyy[0],"",shutdyy[1]
            speak(shssw)
    resp.close()    # 关掉resp
