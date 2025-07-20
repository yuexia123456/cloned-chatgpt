import  os
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, model_name, api_key, base_url):
    model = ChatOpenAI(
        model = model_name,
        api_key = api_key,
        base_url = base_url
    )
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律?", memory, "qwen-plus",
#                   os.getenv("DASHSCOPE_API_KEY"), "https://dashscope.aliyuncs.com/compatible-mode/v1"))
# print(get_chat_response("我的上一个问题是什么?", memory, "qwen-plus",
#                   os.getenv("DASHSCOPE_API_KEY"), "https://dashscope.aliyuncs.com/compatible-mode/v1"))
