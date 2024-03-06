import streamlit as st
from sydney import SydneyClient
import asyncio
async def getResponseFromAI(chatInput):
    async with SydneyClient() as sydney:
        response = await sydney.ask(chatInput, citations=True)
    return response



async def main():
    st.title("AI CHATBOT")
    # getting inputs from the user
    chatInput= st.text_input("What Do U want to Ask Today?")
    if (chatInput.strip() == ""):
        st.info("please enter something!!")

    # results
    predictedAIResponse = ""
    if (st.button("ASK AI")):
        st.write("GENERATED AI RESPONSE")
        st.write(await getResponseFromAI(chatInput))
        print(await getResponseFromAI(chatInput))


if __name__ == '__main__':
    asyncio.run(main())