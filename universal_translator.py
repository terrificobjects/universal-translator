# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import subprocess
flag = 0
  
# A tuple containing all the language and
# codes of the language will be detcted
dic = ('afrikaans', 'af', 'albanian', 'sq', 
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az', 
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo', 
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)', 
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek',  'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')
  
  
# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak the phrase you wish to translate into the microphone. Please be as clear and concise with your speech as possible for the most accurate results. When you are done speaking, wait for the system to process and recognize your speech, and then it will prompt you for the language you wish to translate to.")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing voice for recognition. Please wait...")
        query = r.recognize_google(audio, language='en-US')
        print(f"The phrase provided to the Universal Translator was: {query}\n")
    except Exception as e:
        print("Please repeat the phrase, I didn't quite catch that.")
        return "None", False

    stop_script = query.lower() == "thank you, translator"
    return query, stop_script

def destination_language():
    print("")
    print()
    to_lang, _ = takecommand()
    while (to_lang == "None"):
        to_lang, _ = takecommand()
    to_lang = to_lang.lower()
    if to_lang in dic:
        return dic[dic.index(to_lang) + 1]
    else:
        return ""


def main():
    # Input from user
    query, stop_script = takecommand()
    while (query == "None"):
        query, stop_script = takecommand()

    if stop_script:
        return False

    to_lang = destination_language()

    # Mapping it with the code
    while (to_lang not in dic):
        print("Language in which you are trying to convert is currently not available, please select another language")
        print()
        to_lang = destination_language()
        to_lang = dic[dic.index(to_lang)+1]

    print(to_lang)
    print(query)

    # invoking Translator
    translator = Translator()

    # Translating from src to dest
    text_to_translate = translator.translate(query, dest=to_lang)
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow=False)

    # Using save() method to save the translated speech in capture_voice.mp3
    speak.save("captured_voice.mp3")

    # Get the current working directory of the Python script
    cwd = os.getcwd()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captured_voice.mp3")
    subprocess.call([r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe", file_path])

    # Printing Output
    print(text)
    return True

if __name__ == "__main__":
    continue_script = True
    while continue_script:
        continue_script = main()
