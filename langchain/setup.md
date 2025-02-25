# 🚀 Setting Up Your Conda Environment for the LangChain Course

This guide will walk you through setting up your development environment using Conda for the LangChain & LangGraph course. This setup ensures all dependencies are installed correctly and keeps your environment isolated from system-wide Python packages.

---

## **📌 Step 1: Install Conda**

If you haven't installed Conda yet, download and install **Miniconda** or **Anaconda**:
- **Miniconda (Recommended for Lightweight Install)**: [Download Here](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda (Includes More Preinstalled Packages)**: [Download Here](https://www.anaconda.com/download/)

After installation, verify Conda is installed:
```bash
conda --version
```

---

## **📌 Step 2: Create the Conda Environment and Install Dependencies**

Run the following command to create the Conda environment and install all dependencies in one step:
```bash
conda env create -n langchain-env -f environment.yml
```

Once created, activate the environment:
```bash
conda activate langchain-env
```

If you don’t have the `environment.yml` file, manually install the key packages:
```bash
conda create -n langchain-env python=3.9 -y
conda activate langchain-env
pip install langchain langchain-openai langgraph chromadb faiss-cpu fastapi flask uvicorn torch transformers sentence-transformers numpy pandas jupyterlab
```

---

## **📌 Step 3: Verify the Installation**

Check if everything is correctly installed by running the following:
```bash
python -c "import langchain; print('LangChain is installed successfully!')"
```

For Jupyter Notebook users, ensure Jupyter is installed and works within the environment:
```bash
jupyter lab
```

---

## **📌 Step 4: Setting Up Environment Variables**

Create a `.env` file to store sensitive API keys:
```bash
touch .env
```

Add the following content to `.env`:
```
OPENAI_API_KEY=your-api-key-here
PINECONE_API_KEY=your-pinecone-key-here
```

To load environment variables, install **`python-dotenv`**:
```bash
pip install python-dotenv
```

---

## **📌 Step 5: Run a Quick Test**

Test LangChain with OpenAI by running this script:
```python
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke("Hello, how can I use LangChain?")
print(response)
```

If everything runs without errors, your setup is complete! 🚀

---

## **📌 Step 6: Keeping Your Environment Updated**

To update your Conda environment:
```bash
conda env update --file environment.yml --prune
```

To update individual packages:
```bash
pip install --upgrade langchain langgraph
```

---

## **📌 Step 7: Deactivating and Removing the Environment (If Needed)**

To deactivate the Conda environment:
```bash
conda deactivate
```

To remove the environment completely:
```bash
conda env remove -n langchain-env
```

---

🎯 **Congratulations!** You have successfully set up your Conda environment for LangChain & LangGraph. You’re now ready to dive into the course! 🚀

