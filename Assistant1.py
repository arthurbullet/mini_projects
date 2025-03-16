import speech_recognition as sr
import webbrowser
import os

def voice_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Чо те включить надо?: (Один, Два, Три)")
        audio_data = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio_data, language="ru-RU").lower()
        print(f"ты сказал: {command}")

        if "один" in command:
            youtube_link = "https://www.youtube.com/watch?v=1ZGkkAggRUg"
            webbrowser.open(youtube_link)

        elif "два" in command:
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

        elif "три" in command:
            os.startfile(r"C:\Users\Admin\Desktop\Soundpad\Soundpad.exe")

        else:
            print("Говори внятнее")

    except sr.UnknownValueError:
        print("Не получилось,сорян")
    except sr.RequestError as e:
        print(f"Ошибка распознавания речи: {e}")

if __name__ == "__main__":
    voice_assistant()
