# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
#
# if __name__=="__main__"  :
#     speak("hello everyone")


# Akhbaar padhke sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__=="__main__" :
    speak("news for today")
    url="https://newsapi.org/v2/everything?q=apple&from=2021-08-02&to=2021-08-02&sortBy=popularity&apiKey=86b9d52e0b664c14b41d208e4c254ac5"
    news=requests.get(url).text # request module is used to get url(http)
    news_dict=json.loads(news) # json is used to get key values of data
    print(news_dict["articles"])
    arts=news_dict["articles"]
    for articles in arts:
        speak(articles["title"])
        speak("moving on to next news")
    speak("end of the news")




