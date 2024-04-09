import pyttsx3
# Inicializa o objeto de voz
engine = pyttsx3.init()
# Define o texto que será lido
texto = "Olá, mundo! Eu sou uma voz gerada por computador."
# Define a velocidade da voz
engine.setProperty('rate', 150)
# Define a voz a ser utilizada
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # muda para a voz masculina
# Lê o texto e gera a voz correspondente
engine.say(texto)
engine.runAndWait()

