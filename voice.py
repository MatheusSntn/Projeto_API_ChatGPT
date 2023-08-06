from main import gerar_respostas, mensagens
import speech_recognition as sr
import asyncio

# Funcao para ouvir e reconher a fala

async def main():
    while True:
        microfone = sr.Recognizer()
        # Usa mic
        print("\nPergunte ao ChatGPT: (Diga 'sair' para sair)")
        with sr.Microphone() as source:
            # Chama algoritmo para reducao de ruido
            microfone.adjust_for_ambient_noise(source)

            # Armazena o que foi dito
            audio = microfone.listen(source)
            
            
        try:
            # para variavel para algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio, language='pt-BR')
            print(frase)
            
            if frase == 'sair':
                print('saindo...')
                break
            
            if frase != '':
                mensagens.append({"role": "user", "content":frase})
                print('Pergunta: ', frase)
                resposta = gerar_respostas(mensagens)
                print('ChatGPT: ', resposta[0], '\ncusto: \n', resposta[1])
                mensagens.append({"role":"assistant", "content": resposta[0]})    

        except sr.UnknownValueError:
            print('Não entendi a sua pergunta, poderia repetir?')
            # send_result, receive_result = await asyncio.gather(send(), receive())

asyncio.run(main())