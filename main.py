import speech_recordnition as sr
import import pyttsx3
import random

def talk(words):
    engine pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
def command():
    r = sr.Recordnizer()
    with sr.Microphone as source:
        talk('Чё нада')
        r.adjust_for_ambient_noise(source, duration = 1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        task = r.recordnize_google(audio,language = ru-Ru).lower()
    except sr.UnknowValueError:
        talk('Чё мямлмшь, нормально говори ')
        task = command()
    return task

random1 = ['сел','шёл','стоял']
random2 = ['Обама','Илон Маск','мой знакомый Лёха']
notRandom = ['на зону','по улице','около подьезда']
hi = 0
def Make(task):
    if 'здрасте' in task and hi == 0:
        talk('Чё так грубо?')
        hi = 1
    elif 'здрасте' in task == 0 and hi == 0:
        talk('Чё не здароваешся?')
        hi = 1
    elif 'скажи что-нибудь' in task and hi == 1:
        r1 = random.choice(random1)
        r2 = random.choice(random2)
        talk(r1+r2+notRandom[random1[r1]])

talk('Я Валера, искуственный интелект')
command()
