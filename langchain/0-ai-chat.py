# simple program to chat with the AI assistant
# shows llm.invoke() function usage from ChatOpenAI class

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Simple chatbot loop
while True:
    user_input = input("You (type exit to stop): ")
    if user_input.lower() in ["exit", "quit"]:
        print("AI Assistant: Goodbye!")
        break
    
    response = llm.invoke(user_input)
    print(f"AI Assistant: {response.content}")
