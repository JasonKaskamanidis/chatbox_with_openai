import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=300,
            temperature=0.1
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)
