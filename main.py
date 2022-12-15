import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Humain:
    def __init__(self, name='Humain'):
        self.name = name
        self.question = None

    def ask(self, question):
        if question == 'stop':
            exit()
        return "Humain: {question}\n".format(question=question)

class AI:
    def __init__(self, name='Assistant'):
        self.name = name

    def answer(self, response):
        return "Assistant: {response}\n".format(response=response)

class Conversation:
    def __init__(self, humain, ai):
        self.humain = humain
        self.ai = ai
        self.context = "Ce qui suit est une conversation avec un assistant IA d'un service informatique. L'assistant est serviable, créatif, intelligent et très sympathique.\n\n"

    def ask(self, question):
        self.context += self.humain.ask(question)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="{context}\n\nHumain: {question} \nAssistant:".format(context=self.context, question=question),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Humain:", " Assistant:"]
        )
        self.context += self.ai.answer(response.choices[0].text)
        return self.ai.answer(response.choices[0].text)

if __name__ == "__main__":
    humain = Humain()
    ai = AI()
    conversation = Conversation(humain, ai)
    while True:
        question = input("Votre question: ")
        print(conversation.ask(question))