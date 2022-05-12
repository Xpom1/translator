import speech_recognition
import googletrans
from gtts import gTTS
from playsound import playsound

transe = googletrans.Translator()
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listner():
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        try:
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        except:
            listner()
    if "переведи" in query:
        trans()
    elif query == "стоп":
        exit()
    else:
        listner()


def trans():
    print("Я вас слушаю...")
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        try:
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        except:
            print("Я вас не понял, повторите пожалуйста")
            trans()
    q = query
    result = transe.translate(q, src='ru', dest='en')
    obj = gTTS(text=result.text, lang='en', slow=False)
    obj.save("exam.mp3")
    playsound("exam.mp3")
    listner()

listner()
