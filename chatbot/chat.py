import json
from nltk.chat.util import Chat, reflections

nome = input("Digite seu nome: ")
contexto = int(input("Digite o número do serviço: \n" 
"1 - Conversa padrão: \n" 
"2 - Linguagens que já mexi na faculdade: \n" 
"3 - Professores na faculdade: \n" 
"4 - Campeões no lol: \n"))

match contexto:
    case 1:
        with open("C:/Users/filho/OneDrive/Área de Trabalho/Programação/Python/chatbot/case1.json", encoding="utf-8") as file:
            intents = json.load(file)
    case 2:
        with open("C:/Users/filho/OneDrive/Área de Trabalho/Programação/Python/chatbot/case2.json", encoding="utf-8") as file:
            intents = json.load(file)
    case 3:
        with open("C:/Users/filho/OneDrive/Área de Trabalho/Programação/Python/chatbot/case3.json", encoding="utf-8") as file:
            intents = json.load(file)
    case 4:
        with open("C:/Users/filho/OneDrive/Área de Trabalho/Programação/Python/chatbot/case4.json", encoding="utf-8") as file:
            intents = json.load(file)
        

combinacoes = [[item["padrao"], item["respostas"]] for item in intents]

chatbot = Chat(combinacoes, reflections)
print("Olá! Digite algo para começar")

chatbot.converse()