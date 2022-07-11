# Part(1)
## Arabic-Speech-to-text
This project explains how to use Speech Recognition library in Python in order to recognize Arabic speech and how to implement this library with Flask freamwork

### Prerequisite:
1-install Python

2-PyCharm IDE.

### Steps:
1- using the terminal, paste following lines:

`pip install Flask`
install Flask microframework as a web framework

install SpeechRecognition libraries:

`pip install pipwin`

`pipwin install pyaudio`

`pip install SpeechRecognition`

2-Write html page inside templates folder.

3-Write speechRecognition code using python in main.py file.

4-Run the code.

5- `Procfile` and `requirements.txt` are used to deploy the page on Heroku platform.


### Output:

![2022-07-11](https://user-images.githubusercontent.com/73133501/178298045-25f7df98-f60b-4cae-b4a7-ef74043d50d9.png)


![2022-07-11 (1)](https://user-images.githubusercontent.com/73133501/178298177-1a9cb8ef-ccda-4b72-867f-a331fce0c377.png)



# Part(2)

## Wasdom ESP32 algorithm

### Prerequisite:

install Arduino IDE

buy ESP32 chip

### Steps:

1.Link ESP32 chip to your laptop.

2.Open Arduino IDE.

3.Go to `File` > `Prefrences`.

4.Inside `Additional Boards managers URLs` paste this link: `https://dl.espressif.com/dl/package_esp32_index.json`.

5.Go to `Tools` > `board: 'arduino uno'` > `Boards maneger`.

6.Search `ESP32` then click `install`.

7.After installing, we want to test the chip by runnong a simple code on it, from `File` > `examples` > `basics` > `Blink`.

8.Choose the port from `Tools` > `Port` > `COM6`.

9.Run the code from the right head arrow.



# References:

[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

[Using SpeechRecognition library](https://drive.google.com/file/d/16C6IJb9iOk4WbRVD8CnKfwaCfxs0qfiC/view)

[Flask SpeechRecognition project](https://www.youtube.com/watch?v=vuaolF-OSGY&list=LL&index=2&ab_channel=TheCodex)

[Smart Methods Est's لأسبوع الثاني اللقاء الخامس](https://www.youtube.com/watch?v=e-xjjn5NX-M&ab_channel=%D8%A7%D9%84%D8%A7%D8%B3%D8%A7%D9%84%D9%8A%D8%A8%D8%A7%D9%84%D8%B0%D9%83%D9%8A%D8%A9)









