from src.chatbot import EsportsChatbot


def main():
    bot = EsportsChatbot()

    print("Chatbot de eSports iniciado.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() == "sair":
            print("Encerrando chatbot.")
            break

        if not pergunta:
            print("Digite uma pergunta válida.")
            continue

        try:
            resposta = bot.responder(pergunta)
            print(f"Bot: {resposta}\n")
        except Exception as erro:
            print(f"Erro ao gerar resposta: {erro}\n")


if __name__ == "__main__":
    main()