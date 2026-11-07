from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

openai_model = init_chat_model(model="gpt-5.6-luna", reasoning_effort="none")
# print(openai_model.invoke("what is the color of rose?").content)