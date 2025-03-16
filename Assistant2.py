import speech_recognition as sr
import webbrowser
import os

def voice_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # Калибровка под фоновый шум (исправление №2)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Чо те включить надо?: (музыка, браузер, звуки)")
        audio_data = recognizer.listen(source)

    try:
        # Распознавание речи без преобразования в нижний регистр
        command = recognizer.recognize_google(audio_data, language="ru-RU")
        print(f"ты сказал: {command}")

        if "музыка" in command:
            youtube_link = "https://www.youtube.com/watch?v=1ZGkkAggRUg"
            webbrowser.open(youtube_link)

        elif "браузер" in command:
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

        elif "звуки" in command:
            os.startfile(r"C:\Users\Admin\Desktop\Soundpad\Soundpad.exe")

        else:
            print("Говори внятнее")

    except sr.UnknownValueError:
        print("Не получилось, сорян")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")

if __name__ == "__main__":
    voice_assistant()
