import streamlit as st

from langchain.memory import ConversationBufferMemory
from utils import get_chat_response

st.title("💬克隆ChatGPT")

with st.sidebar:
    api_key = st.text_input("请输入你的api密钥", type="password")
    st.markdown("[申请你的api密钥](https://www.aliyun.com/product/bailian)")
    restart = st.button("新建对话")

if restart:
    st.session_state.clear()

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好,我是你的ai助手,有什么可以帮你的吗?"}]
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not api_key:
        st.info("请输入你的api密钥")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中,请稍等..."):
        response = get_chat_response(prompt,st.session_state["memory"], "qwen-plus",
                          api_key,base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)