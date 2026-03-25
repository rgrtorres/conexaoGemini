from google import genai
import streamlit as st
from streamlit_chat import message as msg
from src.config.Gemini import conexaoGemini

st.title("Chat com Gemini")
st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = []

pergunta = st.text_area("Pergunta")
btn_enviar = st.button("Enviar")
sessionState = st.session_state.hst_conversa

if btn_enviar:
    sessionState.append({"pergunta": pergunta})
    retornoGemini = conexaoGemini(pergunta)
    if retornoGemini == False:
        st.error("Aconteceu algum erro...")
        st.stop()
    else:
        sessionState.append({"resposta": retornoGemini})
        
if len(sessionState) > 0:
    for i in range(len(sessionState)):
        if i % 2 == 0:
            msg(st.session_state.hst_conversa[i]['pergunta'], is_user=True)
        else:
            msg(st.session_state.hst_conversa[i]['resposta'])