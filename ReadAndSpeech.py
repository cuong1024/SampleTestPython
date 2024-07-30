import pyttsx3
import PyPDF2

read=pyttsx3.init() 

giongs = read.getProperty('voices')
for giong in giongs:
    print(giong)

read.setProperty('voice',giongs[1].id)
read.say("Xin chào. Tôi tên là Lê Mạnh Cường")
read.runAndWait()
