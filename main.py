from flask import Flask,render_template,request
import speech_recognition as sr

Speech_app = Flask(__name__) #define app name

@Speech_app.route("/" ,methods=['GET', 'POST'])
def home():
    text =""
    if request.method == "POST":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ar-AR')
        except sr.UnknownValueError as U:
            print(U)
        except sr.RequestError as R:
            print(R)

    return render_template("home.html",text=text)

if __name__ == "__main__":
    Speech_app.run(debug=True)

