from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableLambda

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# New memory approach using BaseChatMessageHistory
memory = ChatMessageHistory()

# Define a Prompt Template
template = PromptTemplate.from_template(
    "Chat History:\n{chat_history}\n\nUser: {user_input}\nAI:"
)

# Preprocessing: Load Memory
def preprocess_fn(inputs):
    chat_history = "\n".join([msg.content for msg in memory.messages])  # Extract past messages
    return {"chat_history": chat_history, "user_input": inputs["user_input"]}

# Postprocessing: Save Memory
def postprocess_fn(response, inputs):
    memory.add_user_message(inputs["user_input"])
    memory.add_ai_message(response.content)
    return response.content

# Define RunnableSequence Pipeline (Fixed with RunnableLambda)
pipeline = RunnableSequence(
    RunnableLambda(preprocess_fn),
    template,
    llm,
    RunnableLambda(postprocess_fn)
)

# Run Chatbot
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("AI Assistant: Goodbye!")
        break

    response = pipeline.invoke({"user_input": user_input})
    print(f"AI Assistant: {response}")  # Prints AI response
