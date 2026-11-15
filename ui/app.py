import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8080")
st.set_page_config(page_title="MarkovLab", page_icon="🧪", layout="wide")
st.title("MarkovLab")
st.caption("Explore how probabilistic rules generate text.")

default_corpus = (
    "The moon moves across the quiet sky. The stars shine above the quiet earth. "
    "A curious observer watches the stars and records the changing sky. "
    "The quiet earth waits beneath the moon."
)
with st.sidebar:
    st.header("Experiment settings")
    order = st.selectbox("Markov order", [1, 2], format_func=lambda x: f"Order {x}")
    length = st.slider("Additional tokens", 10, 150, 40)
    seed = st.number_input("Random seed (repeatable)", min_value=0, max_value=999999, value=42)
    st.info("Order 1 uses one previous token. Order 2 uses two.")

corpus = st.text_area("Corpus", value=default_corpus, height=180,
                      help="Paste text that the model will learn transitions from.")
if st.button("Generate text", type="primary"):
    try:
        response = requests.post(
            f"{API_URL}/generate",
            json={"corpus": corpus, "order": order, "length": length, "seed": int(seed)},
            timeout=20,
        )
        if response.ok:
            st.subheader("Generated output")
            st.write(response.json()["text"])
        else:
            st.error(response.json().get("detail", response.text))
    except requests.RequestException as exc:
        st.error(f"API unavailable: {exc}")

st.divider()
st.subheader("How it works")
st.markdown("1. Corpus is tokenized into words and punctuation.\n"
            "2. Engine counts transitions between tokens.\n"
            "3. A next token is sampled according to observed transition frequencies.\n"
            "4. The process repeats to produce a new sequence.\n\n"
            "This is probabilistic generation, not search or semantic understanding.")
