import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq

load_dotenv(override=True)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

st.title("Movie Info Extractor")

para = st.text_area("Give your paragraph:")

if st.button("Extract"):
    final_prompt = prompt.invoke(
        {
            "paragraph": para,
            "format_instructions": parser.get_format_instructions()
        }
    )

    response = model.invoke(final_prompt)

    st.write(response.content)