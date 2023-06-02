import speech_recognition as sr

# Створюємо об'єкт recognizer
r = sr.Recognizer()

# Вказуємо параметри мікрофону
mic = sr.Microphone(device_index=0)

# Запитуємо користувача про дозвіл на доступ до мікрофону
while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Скажіть щось!")
        audio = r.listen(source)

    # Конвертуємо звук в текст за допомогою Google Speech Recognition
    try:
        text = r.recognize_google(audio, language="uk-UA")
        print(text)
        words_list = text.lower().split()
        if 'quit' in words_list:
            print("".join(text))
            break
        print("".join(text))
    except sr.UnknownValueError:
        print("Google Speech Recognition не зміг розпізнати текст")
    except sr.RequestError as e:
        print("Помилка сервісу Google Speech Recognition; {0}".format(e))
