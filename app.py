import os
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

os.environ['HF_ENDPOINT'] = 'http://huggingface.co'

@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_technical_questions(tech_stack):
    generator = load_model()
    tech_str = ', '.join(tech_stack)

    prompt = (
        f"You are a senior technical interviewer.\n"
        f"Ask ONE technical interview question specific to a candidate skilled in {tech_str}.\n"
        f"The question should be:\n"
        f"- Focused only on {tech_str}\n"
        f"- Practical, real-world, and relevant to job interviews\n"
        f"- Not general-purpose (e.g., avoid 'What is the best programming language?')\n"
        f"- Not philosophical or preference-based\n"
        f"- Not a story or paragraph — only a direct question\n"
        f"- No list, intro, explanation — just the question\n\n"
        f"Example:\n"
        f"How do you implement token-based authentication using JWT in a Flask API?\n\n"
        f"Now generate one good technical interview question:\n"
    )

    try:
        output = generator(prompt, max_length=64, do_sample=True, temperature=0.7)[0]["generated_text"]
        return output.strip()
    except Exception as e:
        return f"❌ Error generating question: {e}"

# === Streamlit App UI ===
def chatbot():
    st.set_page_config(page_title="Interview Question Generator", page_icon="💼")
    st.title("💼 Personalized Interview Question Generator")

    if "step" not in st.session_state:
        st.session_state.step = "intro"

    if st.session_state.step == "intro":
        st.write("Welcome! Get personalized interview questions based on a tech stack.")
        if st.button("Start"):
            st.session_state.step = "collect_info"

    elif st.session_state.step == "collect_info":
        st.subheader("Candidate Info")
        name = st.text_input("Candidate Full Name")
        tech_input = st.text_area("Enter Tech Stack (comma-separated):")

        if st.button("Generate Questions"):
            if name and tech_input:
                st.session_state.candidate_name = name
                st.session_state.tech_stack = [x.strip() for x in tech_input.split(",") if x.strip()]
                st.session_state.step = "generate"
            else:
                st.warning("⚠️ Please fill in both fields.")

    elif st.session_state.step == "generate":
        st.subheader("Generated Technical Questions")
        st.write(f"👤 Candidate: {st.session_state.candidate_name}")
        st.write(f"🛠 Tech Stack: {', '.join(st.session_state.tech_stack)}")

        with st.spinner("Generating questions using Transformers..."):
            questions = generate_technical_questions(st.session_state.tech_stack)
            st.text_area("📋 Questions:", questions, height=200)

        if st.button("Restart"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    chatbot()
