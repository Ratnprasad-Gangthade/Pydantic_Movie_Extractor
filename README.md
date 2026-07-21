# 🎬 Pydantic Movie Extractor

A small project built to understand **Pydantic Output Parsers** in LangChain — how they work, and how they guide an LLM to return clean, structured data instead of free-form text.

## 🎯 Motive

LLMs return plain text by default. But real applications usually need **structured data** (JSON, objects, typed fields) that can be directly used in code. This project explores how `PydanticOutputParser` from LangChain solves that problem by:

- Defining a schema (`Movie`) using a Pydantic `BaseModel`
- Auto-generating format instructions from that schema
- Injecting those instructions into the prompt sent to the LLM
- Getting back a response that matches the schema

## 🧠 How It Works

1. A `Movie` Pydantic model is defined with fields like `title`, `release_year`, `genre`, `director`, `cast`, `rating`, and `summary`.
2. `PydanticOutputParser(pydantic_object=Movie)` is created from this model.
3. `parser.get_format_instructions()` generates instructions telling the LLM exactly what JSON structure to output.
4. These instructions are injected into a `ChatPromptTemplate` (system message), along with the user's paragraph (human message).
5. The final prompt is sent to a Groq-hosted LLM (`llama-3.3-70b-versatile`) via `ChatGroq`.
6. The model returns movie information in the requested structured format.

## 📁 Project Structure
├── core.py # Core logic: model, schema, parser, prompt (CLI version)
├── app.py # Streamlit UI wrapper around core.py logic
├── .env # Environment variables (GROQ_API_KEY)
└── README.md

## ⚙️ Setup

1. Clone the repo and create a virtual environment.
2. Install dependencies:
```bash
   pip install langchain langchain-core langchain-groq pydantic python-dotenv streamlit
```
3. Create a `.env` file in the root directory:
## ▶️ Usage

### CLI version
```bash
python core.py
```
You'll be prompted to enter a paragraph describing a movie, and the extracted info will be printed to the terminal.

### Streamlit UI version
```bash
streamlit run app.py
```
Enter a paragraph in the text area, click **Extract**, and the structured movie information will be displayed.

## 📥 Example Input
Inception is a science fiction thriller released in 2010 and directed by
Christopher Nolan. The film stars Leonardo DiCaprio, Joseph Gordon-Levitt,
Ellen Page, Tom Hardy, and Ken Watanabe. It follows Dom Cobb, a skilled
thief who specializes in stealing secrets from people's subconscious
through dream-sharing technology. Cobb is offered a chance to erase his
criminal record by performing an impossible task known as "inception"—
planting an idea into someone's mind instead of stealing one. The movie
received widespread critical acclaim for its storytelling, visual effects,
and musical score, earning a rating of 8.8/10 on IMDb.

## 📤 Example Output

```json
{
  "title": "Inception",
  "release_year": 2010,
  "genre": ["science fiction", "thriller"],
  "director": "Christopher Nolan",
  "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page", "Tom Hardy", "Ken Watanabe"],
  "rating": 8.8,
  "summary": "The film follows Dom Cobb, a skilled thief who specializes in stealing secrets from people's subconscious through dream-sharing technology, as he is offered a chance to erase his criminal record by performing an impossible task known as 'inception'—planting an idea into someone's mind instead of stealing one."
}
```

## 🛠️ Tech Stack

- **LangChain** – prompt templating & output parsing
- **LangChain-Groq** – LLM integration (`llama-3.3-70b-versatile`)
- **Pydantic** – schema definition & validation
- **Streamlit** – UI layer
- **python-dotenv** – environment variable management

## 📚 Key Learning

The core takeaway from this project is understanding `PydanticOutputParser`:
- It bridges the gap between **unstructured LLM text output** and **structured, typed Python objects**.
- `get_format_instructions()` tells the model *how* to format its response so it's parseable.
- This pattern is foundational for building reliable LLM-powered applications where downstream code depends on consistent, validated data structures.
