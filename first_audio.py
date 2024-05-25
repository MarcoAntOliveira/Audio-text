from gtts import gTTS
from playsound import playsound

language = 'pt-br'

audio = gTTS(
    text = 'essa é uma apresentação do grupo 2 do projeto integrador',
    lang = language
)

audio.save('audio.mp3')
playsound('audio.mp3')