import chart_studio.plotly as py
import chart_studio.presentation_objs as pres
from googletrans import Translator
import speech_recognition as sr

translator = Translator()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text_speech = r.recognize_google(audio, None, "nl_NL")
    print("Google Speech Recognition thinks you said " + text_speech)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(
        e))

translation_en = translator.translate(text_speech, dest='en')
print(translation_en.origin, translation_en.text)

translation_tr = translator.translate(translation_en.text, dest='tr')

print(translation_tr.origin, translation_tr.text)

text_tr = translation_tr.text
print("Google translate thinks you said " + text_tr)

filename = 'simple-pres'
markdown_string = "{}".format(text_tr)

my_pres = pres.Presentation(markdown_string)
pres_url_0 = py.presentation_ops.upload(my_pres, filename)