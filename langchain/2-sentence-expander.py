from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')




from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence


def preprocess(input):
    input["topic"] = input["topic"].lower()
    return input 

def postprocess():
    return "end of story"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

template = PromptTemplate.from_template("Expand the following topic into a 3-sentence paragraph shown as bullet points: {topic}")

pipeline = RunnableSequence(preprocess, template,llm)
sentence = input("Enter a topic: ")

response = pipeline.invoke({"topic": sentence})

print("\nResult:\n", response.content)
