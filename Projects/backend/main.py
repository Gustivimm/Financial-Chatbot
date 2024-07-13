# python version: 3.11.9
# pip install openai (cmd)
# variáveis em inglês; comunicação (comentários e outputs para o usuário) em português
# padrão das variáveis: verbo/advérbio_subjetivo. Ex: mandar_menssagem -> send_message
# para variáveis com dois subjetivos considerar o que mais pode repetir. Ex: menssagem_do_usuário -> user_message
# para sinalizar erros, chamar atenção ou sanar dúvidas, deixem um comentário com um monte de !. !!!!!!!!!!!!!!!!!!!!!!!!! (deem crtl+c ctrl+v aqui pfv)

import openai

api_key = ""
openai.api_key = api_key

def send_message(user_message, list_message=[]):
    list_message.append(
        {"role" : "user", "content" : user_message}
    )

    ai_message = openai.ChatCompletion.create(
        model = ""gpt-3.5-turbo",
        messages = list_message
    )

    return ai_message["choices"][0]["message"]

list_message = []
while True:
    text = input("Escreva aqui sua mensagem: ")
    
    if text == "sair":
        break
    else
        ai_message = send_message(text, list_message)
        list_message.append(ai_message)
        print("Chatbot: ", ai_message["content"])
