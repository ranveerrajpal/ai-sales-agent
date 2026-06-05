# AI Sales Agent

An AI-powered voice sales agent that can converse with customers, understand their requirements, retrieve information from a product catalog, and respond naturally using speech.

The system combines:

- Speech-to-Text (Whisper)
- Retrieval-Augmented Generation (RAG)
- Large Language Models (Groq Llama 3.3 70B)
- Text-to-Speech (Microsoft Edge TTS)

This project is designed to simulate a real sales representative capable of answering customer questions, recommending products, handling objections, and assisting with order inquiries.

---

## Features

### Voice Interaction

- Push-to-talk using the SPACE key
- Voice recording from microphone
- Automatic speech transcription

### Product Knowledge

- Upload PDF product catalogs
- Automatic catalog ingestion
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)

### AI Sales Intelligence

- Understand customer requirements
- Recommend relevant products
- Answer product-related questions
- Handle customer objections
- Encourage purchase decisions

### Voice Responses

- Natural speech generation
- Microsoft Edge Neural Voices
- Real-time spoken responses

---

## Architecture

```text
Customer Voice
        ↓
Microphone
        ↓
Whisper STT
        ↓
Customer Text
        ↓
RAG Retrieval
(PDF Catalog)
        ↓
Groq LLM
        ↓
Sales Response
        ↓
Edge TTS
        ↓
Voice Output
```

---

## Tech Stack

### Speech-to-Text

- Faster Whisper

### Retrieval

- LangChain
- ChromaDB
- Sentence Transformers

### Language Model

- Groq API
- Llama 3.3 70B

### Text-to-Speech

- Microsoft Edge TTS

### Programming Language

- Python

---

## Project Structure

```text
sales_agent/
│
├── main.py
├── stt.py
├── tts.py
├── llm.py
├── rag.py
│
├── catalog/
│   └── products.pdf
│
├── chroma_db/
│
├── recordings/
│
├── requirements.txt
│
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Get a free Groq API key from:

https://console.groq.com

---

## Add Product Catalog

Place your catalog PDF inside:

```text
catalog/products.pdf
```

Example:

```text
catalog/
└── products.pdf
```

---

## Run the Application

```bash
python main.py
```

---

## Usage

1. Launch the application.
2. Hold the SPACE key.
3. Speak your question.
4. Release the SPACE key.
5. The AI will:
   - Transcribe your speech
   - Search the catalog
   - Generate a sales response
   - Speak the response aloud

Example:

Customer:

```text
Do you have butyl truck tubes?
```

AI:

```text
Yes, we offer heavy-duty butyl truck tubes designed for long service life and superior air retention. Would you like information about available sizes?
```

---

## Future Improvements

Planned features include:

- Real-time conversation mode
- Continuous listening
- Noise suppression
- Silero VAD integration
- Customer memory
- Lead qualification
- Order extraction
- CRM integration
- Multi-language support
- Call-center integration
- Live analytics dashboard

---

## Example Use Cases

- Manufacturing Sales
- B2B Product Enquiries
- Customer Support
- Product Recommendation Systems
- AI Call Assistants
- Virtual Sales Representatives

---

## License

This project is licensed under the MIT License.

---

## Author

Ranveer Rajpal

B.Tech Information Technology  
Guru Nanak Dev Engineering College, Ludhiana

Interested in AI, Voice Agents, Retrieval-Augmented Generation (RAG), and Intelligent Sales Automation.
