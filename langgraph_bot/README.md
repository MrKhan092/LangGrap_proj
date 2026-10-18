# LangGraph Chatbot with Gemini and Streamlit

A conversational AI chatbot built using **LangGraph, Google Gemini, and Streamlit**. The application provides a chat interface and uses LangGraph to manage conversation flow and maintain conversation state.

## Features

- **Google Gemini:** Generates AI-powered responses using Gemini 2.5 Flash.
- **LangGraph:** Manages the chatbot workflow using a state graph.
- **Conversation Memory:** Uses LangGraph's `InMemorySaver` checkpointing to retain conversation state.
- **Thread-Based Conversations:** Uses a thread ID to identify a conversation.
- **Streamlit UI:** Provides an interactive chat interface.
- **Environment Variables:** Stores API credentials in a `.env` file.

## Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini
- Streamlit
- Python-dotenv

## Project Structure

```text
Chat_bot_LG/
└── langgraph-project/
    ├── langgraph_backend.py
    ├── streamlit_frontend.py
    ├── .env
    ├── .gitignore
    └── README.md
```

## Prerequisites

Before starting, install:

- Python 3.10 or later
- Git
- A Google Gemini API key

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd langgraph-project
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv myenv
source myenv/bin/activate
```

**Windows**

```powershell
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install langchain langgraph langchain-google-genai streamlit python-dotenv
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_actual_gemini_api_key
```

Replace the placeholder with your own API key.

**Important:** Never commit your `.env` file or share your API key publicly.

### 5. Run the application

Make sure your virtual environment is activated and you are inside the project directory.

```bash
streamlit run streamlit_frontend.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to use the chatbot.

## How It Works

1. The user enters a message through the Streamlit chat interface.
2. The frontend passes the message to the LangGraph chatbot.
3. LangGraph executes the chatbot node.
4. The chatbot node sends the conversation to Google Gemini.
5. Gemini generates a response.
6. LangGraph updates the conversation state and checkpoints it using `InMemorySaver`.
7. Streamlit displays the response to the user.

## Conversation Memory

The project uses LangGraph's `InMemorySaver` checkpointing and a configurable `thread_id` to associate messages with a conversation.

For example:

```python
config = {
    "configurable": {
        "thread_id": "thread-1"
    }
}
```

Using the same thread ID allows LangGraph to retrieve the corresponding conversation state while the in-memory checkpointer remains available.

**Note:** `InMemorySaver` stores checkpoints in memory. They are lost when the backend process restarts, and they are not persistent across application restarts.

## Troubleshooting

### Gemini API key error

- Check that `.env` exists in the project root.
- Verify that `GOOGLE_API_KEY` contains a valid key.
- Ensure `load_dotenv()` runs before initializing the Gemini model.

### Module not found

Activate the virtual environment and reinstall dependencies:

```bash
python -m pip install langchain langgraph langchain-google-genai streamlit python-dotenv
```

### Streamlit command not found

Run Streamlit through Python:

```bash
python -m streamlit run streamlit_frontend.py
```

### Conversation history is not maintained

Ensure the frontend passes the same `thread_id` for messages belonging to the same conversation.

## Future Improvements

- Persistent conversation storage using SQLite or PostgreSQL.
- Multiple conversation threads.
- Streaming responses.
- Chat history management.
- Deployment to a cloud platform.

## License

This project is available for learning and personal development. Add a license if you intend to distribute it publicly.
