import openai
import dotenv
import os

# conexão via api do chatgpt 3.5
dotenv()
openai.api_key = os.getenv("api_key")

# função que conversa com o chatgpt (armazena e envia a mensagem do usuário; retorna a resposta do chatgpt)
def send_message(user_message, list_message=[]):
    # adiciona à lista de mensagens a mensagem do usuário
    list_message.append(
        {"role" : "user", "content" : user_message}
    )

    # gera a mensagem do chatgpt
    ai_message = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = list_message
    )

    # retorna a mensagem da IA na função
    return ai_message["choices"][0]["message"]

# inicia a lista de mensagens
list_message = []

# cria a conversa com a IA que só acaba quando o usuário quer
while True:
    # mensagem do usuário
    text = input("Escreva aqui sua mensagem: ")
    
    # teste condicional do input
    if text == "sair":
        break
    else:
        # resposta da IA gerada pela captura da mensagem do usuário
        ai_message = send_message(text, list_message)
        list_message.append(ai_message)
        print("Chatbot: ", ai_message["content"])
