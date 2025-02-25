
# Shows how to us PromptTemplate from langchain.prompts to generate a multiple-choice quiz question using OpenAI's GPT-3.5 model.
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')


# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Define a prompt template for quiz generation
quiz_prompt = PromptTemplate.from_template(
    "Generate a multiple-choice quiz question about {topic}. Provide four options and mark the correct answer."
)

# Get user input
topic = input("Enter a quiz topic: ")
formatted_prompt = quiz_prompt.format(topic=topic)

# Get response from the AI
response = llm.invoke(formatted_prompt)
print("\nQuiz Question:\n", response.content)
