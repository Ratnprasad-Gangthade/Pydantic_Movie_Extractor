import streamlit as st
from core import extract_movie_info

st.set_page_config(page_title="Movie Info Extractor")

st.title("🎬 Movie Info Extractor")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250
)

if st.button("Extract"):

    if paragraph.strip() == "":
        st.warning("Please enter a movie paragraph.")
    else:

        raw_response, movie = extract_movie_info(paragraph)

        st.subheader("Raw LLM Response")
        st.write(raw_response)

        st.subheader("Structured Output")

        st.json(movie.model_dump())