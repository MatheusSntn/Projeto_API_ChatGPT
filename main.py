import asyncio
import speech_recognition as sr
import openai


openai.api_key = "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"


mensagens = [{"role":"system", "content": "Voce é um assistente FURIOSO."}]

def gerar_respostas(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1024,
        temperature=0.4,
    )
    return [response.choices[0].message.content, response.usage]

gerar_respostas(mensagens)

# fazer o python falar