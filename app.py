import streamlit as st
from collections import Counter
import re

st.set_page_config(page_title="Pocket AI Analyzer", page_icon="📊")

st.title("📊 Pocket AI Analyzer")
st.write("An educational text analysis tool.")

text = st.text_area("Enter your text here:")

if st.button("Analyze Text"):
    if text.strip():
        words = re.findall(r"\b\w+\b", text.lower())

        st.subheader("Analysis Results")
        st.write("Characters:", len(text))
        st.write("Words:", len(words))
        st.write("Unique words:", len(set(words)))

        common = Counter(words).most_common(5)
        st.subheader("Most common words")

        for word, count in common:
            st.write(f"{word}: {count}")
    else:
        st.warning("Please enter some text first.")
st.header("🖼️ Image Analysis")
uploaded_image = st.file_uploader(
    "Upload a chart image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Chart")
