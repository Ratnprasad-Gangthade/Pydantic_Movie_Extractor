from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import List, Optional

load_dotenv(override=True)

# -------------------- Model -------------------- #

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -------------------- Schema -------------------- #

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# -------------------- Parser -------------------- #

parser = PydanticOutputParser(pydantic_object=Movie)

# -------------------- Prompt -------------------- #

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


# -------------------- Function -------------------- #

def extract_movie_info(paragraph: str):
    """
    Takes a movie paragraph and returns:
    1. Raw LLM response
    2. Parsed Movie object
    """

    final_prompt = prompt.invoke(
        {
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        }
    )

    response = model.invoke(final_prompt)

    movie_data = parser.parse(response.content)

    return response.content, movie_data


# -------------------- CLI (Optional) -------------------- #

if __name__ == "__main__":
    para = input("Give your paragraph: ")

    raw_output, movie = extract_movie_info(para)

    print("\nRaw Response:\n")
    print(raw_output)

    print("\nParsed Object:\n")
    print(movie)