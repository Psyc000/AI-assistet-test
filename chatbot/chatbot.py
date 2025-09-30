import os
import sqlite3
import streamlit as st
from openai import OpenAI

# OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="KI-Chatbot Demo", page_icon="🤖")
st.title("🤖 KI-Chatbot Demo mit FAQ-Datenbank")

st.write("Dieser Bot nutzt eine FAQ-Datenbank und KI für Antworten.")

# Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Funktion: Suche in der FAQ-Datenbank
def search_faq(user_question):
    conn = sqlite3.connect("faq.db")
    c = conn.cursor()
    c.execute("SELECT answer FROM faq WHERE question LIKE ?", (f"%{user_question}%",))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Eingabe vom User
user_input = st.text_input("Deine Frage:")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # 1. In FAQ-Datenbank suchen
    faq_answer = search_faq(user_input)

    if faq_answer:
        bot_reply = faq_answer
    else:
        # 2. Falls nicht gefunden → OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du bist ein freundlicher Kundenservice-Bot für verschiedene Branchen."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200
        )
        bot_reply = response.choices[0].message.content

    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

# Chatverlauf anzeigen
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**Du:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
