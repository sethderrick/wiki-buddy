import os
from dotenv import load_dotenv
from embedchain import App

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

wikipedia_bot = App()

# Embed Online Resources

wikipedia_bot.add("https://en.wikipedia.org/wiki/Donald_Trump")
wikipedia_bot.add("https://en.wikipedia.org/wiki/Barack_Obama")

while True:
    question = input("Enter your question, or 'quit' to stop the program.\n >>")

    if question == 'quit':
        break

    response = wikipedia_bot.query(question)
    print(f"\n{response}\n")
