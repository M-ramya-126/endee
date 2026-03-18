import streamlit as st
from endee_store import search
from llm import generate_answer
import json

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Study Assistant", page_icon="🤖", layout="wide")

# ---------- SESSION ----------
if "messages" not in st.session_state:
    try:
        with open("chat_history.json", "r") as f:
            st.session_state.messages = json.load(f)
    except:
        st.session_state.messages = []

# ---------- SIDEBAR ----------
st.sidebar.title("📜 Chat History")

# New Chat Button
if st.sidebar.button("🆕 New Chat"):
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.sidebar.write(f"🧑 {msg['content'][:30]}...")

# Clear Chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    with open("chat_history.json", "w") as f:
        json.dump([], f)

# ---------- STYLE ----------
st.markdown("""
<style>
.block-container {
    max-width: 1000px;
    margin: auto;
}

.stTextInput>div>div>input {
    border-radius: 12px;
    padding: 14px;
}

.stButton>button {
    background: linear-gradient(90deg,#6366f1,#4f46e5);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
}

.user-msg {
    background: linear-gradient(90deg,#6366f1,#4f46e5);
    color: white;
    padding: 14px;
    border-radius: 14px;
    margin: 10px 0;
    text-align: right;
    width: fit-content;
    max-width: 75%;
    margin-left: auto;
}

.bot-msg {
    background: #ffffff;
    color: #000000;
    padding: 14px;
    border-radius: 14px;
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    width: fit-content;
    max-width: 75%;
}

/* Dark mode fix */
@media (prefers-color-scheme: dark) {
    .bot-msg {
        background: #1e1e1e;
        color: #ffffff;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align:center; color:#4f46e5;'>🤖 AI Study Assistant</h1>
<p style='text-align:center; color:#6b7280;'>Smart AI assistant using RAG + Endee 🚀</p>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
with st.form("chat_form", clear_on_submit=True):

    col1, col2 = st.columns([5,1])

    with col1:
        question = st.text_input("🔍 Ask your question")

    with col2:
        submitted = st.form_submit_button("🚀")

    if submitted:
        if question.strip() == "":
            st.warning("⚠ Please enter a question")
        else:
            with st.spinner("🤖 Thinking..."):

                # Search
                results = search(question)

                # Context
                if not results or results[0][0] < 0.2:
                    context = "No relevant notes found"
                else:
                    context = "\n\n".join([doc for _, doc in results])

                # Generate answer
                answer = generate_answer(context, question)

                # Format answer (BLACK BULLETS)
                formatted_answer = answer.replace("**", "")
                formatted_answer = formatted_answer.replace("* ", "● ")
                formatted_answer = formatted_answer.replace("- ", "● ")

                # Save messages
                st.session_state.messages.append({"role": "user", "content": question})
                st.session_state.messages.append({"role": "assistant", "content": formatted_answer})

                # Save file
                with open("chat_history.json", "w") as f:
                    json.dump(st.session_state.messages, f)

# ---------- CHAT DISPLAY ----------
st.markdown("## 💬 Conversation")

messages = st.session_state.messages

pairs = []
for i in range(0, len(messages), 2):
    if i + 1 < len(messages):
        pairs.append((messages[i], messages[i+1]))

for user_msg, bot_msg in reversed(pairs):

    # User message
    st.markdown(f"""
    <div class="user-msg">
    👤 {user_msg["content"]}
    </div>
    """, unsafe_allow_html=True)

    # Bot message
    st.markdown(f"""
    <div class="bot-msg">
    🤖 {bot_msg["content"]}
    </div>
    """, unsafe_allow_html=True)

    # Copy button
    st.code(bot_msg["content"])

# ---------- DOWNLOAD ----------
if st.session_state.messages:
    last_answer = None
    for msg in reversed(st.session_state.messages):
        if msg["role"] == "assistant":
            last_answer = msg["content"]
            break

    if last_answer:
        st.download_button(
            "📥 Download Latest Answer",
            last_answer,
            file_name="ai_notes.txt"
        )

# ---------- CONTEXT ----------
if submitted and results:
    with st.expander("📄 Retrieved Context"):
        for score, doc in results:
            st.write(f"Score: {round(score, 3)}")
            st.write(doc)
            st.write("---")