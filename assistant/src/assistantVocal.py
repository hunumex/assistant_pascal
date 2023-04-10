from gtts import gTTS 
import speech_recognition as speech 
import pyttsx3 

class AssistantVocal:

    def __init__(self):

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'french' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
        self.recognizer = speech.Recognizer()

    def ecouter_commande_vocale(self):

        with speech.Microphone() as source:
            print("Parlez")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio_text = self.recognizer.listen(source, timeout=5)
            print("Fin de l'enregistrement")
        return self.recognizer.recognize_google(audio_text, language='fr-FR')

    def executer_commande_vocale(self, commande):

        try:
            self.engine.say(commande)
            self.engine.runAndWait()
        except speech.UnknownValueError:
            print("Désolé, je n'ai pas compris.")
        except speech.RequestError:
            print("Le service de reconnaissance vocale est indisponible.")
        except ValueError as e:
            print(str(e))
    
