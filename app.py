# app.py
import streamlit as st

from agent import answer_question

st.set_page_config(
    page_title="Agentic AI Support Bot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Agentic AI Support Bot")
st.write(
    "Ask questions about the product, and an AI agent will search the FAQ knowledge base "
    "and use an LLM to answer."
)

st.markdown("### Ask a question")
user_query = st.text_input(
    "Type your question here:",
    placeholder="e.g., How do I reset my password? What is agentic AI?",
)

if st.button("Ask Bot"):
    if not user_query.strip():
        st.error("Please type a question first.")
    else:
        with st.spinner("Agent is thinking..."):
            result = answer_question(user_query)

        st.markdown("### 🧠 Bot Answer")
        st.write(result["answer"])

        if result.get("used_context"):
            st.markdown("### 📚 Retrieved FAQ Matches")
            for match in result["matches"]:
                st.write(f"**Similarity:** {match['similarity']}")
                st.write(f"**Q:** {match['question']}")
                st.write(f"**A:** {match['answer']}")
                st.markdown("---")
        else:
            st.info("No relevant FAQ context was found. Answer is generic.")
