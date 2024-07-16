# Projeto de Exemplo

## Requisitos
- **Python version**: 3.11.9
- **Git version**: 2.45.2

## Convenções de Nomeação
- **Variáveis em inglês; comunicação (comentários e outputs para o usuário) em português**
- **Padrão das variáveis**: verbo/advérbio_subjetivo
  - Exemplo: `mandar_mensagem` -> `send_message`
- **Para variáveis com dois subjetivos**, considerar o que mais pode repetir
  - Exemplo: `mensagem_do_usuário` -> `user_message`

## Notas Importantes
- Para sinalizar erros, chamar atenção ou sanar dúvidas, deixem um comentário com um monte de !.
  - Exemplo: !!!!!!!!!!!!!!!!!!!!!!!! (deem crtl+c ctrl+v aqui pfv)
  
## Exemplo de Código

```python
def send_message(user_message):
    # Este é um exemplo de função que envia uma mensagem
    print("Mensagem enviada: ", user_message)

# Função principal
if __name__ == "__main__":
    user_message = "Olá Mundo!"
    send_message(user_message)
