# 🤖 Femicase - Personal AI Assistant

A powerful, secure, and extensible AI assistant built with LangChain and LangGraph. Femicase can chat, manage files, run terminal commands, and more.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![React](https://img.shields.io/badge/React-18+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **💬 Smart Chat** - Conversational AI with memory and context
- **📁 File Management** - Browse, search, and manage files
- **💻 Terminal Commands** - Execute shell commands safely
- **🎭 Multiple Personalities** - Switch between different chat styles
- **😊 Mood Detection** - Understands user emotions
- **🌐 Multi-language** - Supports English, Hindi, Telugu, Tamil, Malayalam
- **🔒 Security** - Rate limiting, input sanitization, path validation
- **🐳 Docker Ready** - Easy deployment with Docker

## 🚀 Quick Start

### Option 1: Local Development

```bash
# Clone the repo
git clone https://github.com/yourusername/femicase.git
cd femicase

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Start the API server
python server.py
```

### Option 2: Docker

```bash
# Using docker-compose (recommended)
docker-compose up -d

# Or build and run manually
docker build -t femicase .
docker run -p 8000:8000 femicase
```

### Option 3: With React UI

```bash
# Terminal 1: Start API server
cd femicase
source venv/bin/activate
python server.py

# Terminal 2: Start React UI
cd femicase-ui
npm install
npm run dev
```

Then open http://localhost:5173

## 🔧 Configuration

All settings are in `.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_PROVIDER` | LLM provider (ollama/openai) | ollama |
| `LLM_MODEL` | Model name | phi4-mini |
| `EMBEDDING_MODEL` | Embedding model | nomic-embed-text |
| `OLLAMA_BASE_URL` | Ollama server URL | http://localhost:11434 |
| `OPENAI_API_KEY` | OpenAI API key | - |
| `RATE_LIMIT_REQUESTS` | Max requests per window | 60 |
| `RATE_LIMIT_WINDOW` | Rate limit window (seconds) | 60 |

## 🔌 Integrations

### Current Integrations
- **Telegram Bot** - Chat with Femicase on Telegram
- **Discord Webhook** - Add Femicase to Discord servers
- **REST API** - Full API for custom integrations

### 🚧 Ideas for Future Integrations

| Integration | Description | Difficulty |
|-------------|-------------|------------|
| **WhatsApp** | Bot on WhatsApp using WhatsApp Business API | Medium |
| **Slack** | Slack bot with slash commands | Easy |
| **Voice** | Voice commands using Whisper API | Medium |
| **Email** | Email assistant with IMAP/SMTP | Medium |
| **Calendar** | Google Calendar integration | Medium |
| **Notes** | Apple Notes, Evernote, Notion | Easy |
| **Code Editor** | VS Code extension | Medium |
| **Browser Extension** | Chrome/Firefox extension | Easy |
| **Calendar Events** | Create events, set reminders | Medium |
| **Spotify** | Control music playback | Easy |
| **Home Automation** | Control smart home devices | Hard |
| **Database** | Connect to SQL/NoSQL databases | Medium |
| **PDF Reader** | Read and summarize PDFs | Easy |
| **Web Scraper** | Fetch web content | Easy |
| **OCR** | Read text from images | Medium |
| **Translation** | Multi-language translation | Easy |

## 📁 Project Structure

```
femicase/
├── src/
│   ├── bot.py              # Main bot class
│   ├── graph.py            # LangGraph workflow
│   ├── security.py         # Security utilities
│   ├── core/
│   │   ├── chain.py       # LangChain components
│   │   └── mood.py        # Mood/personality detection
│   ├── memory.py          # Conversation & long-term memory
│   ├── tools/
│   │   ├── filesystem.py # File operations
│   │   └── manager.py     # Tool orchestrator
│   ├── analytics/         # Analytics & learning
│   └── integrations/      # Webhooks
├── femicase-ui/           # React frontend
├── server.py             # FastAPI server
├── config.py             # Configuration
├── Dockerfile            # Docker image
├── docker-compose.yml    # Docker Compose
└── requirements.txt     # Python dependencies
```

## 🔐 Security Features

- **Rate Limiting** - Prevents abuse
- **Input Sanitization** - Blocks malicious inputs
- **Path Validation** - Prevents directory traversal
- **API Keys** - Secure authentication
- **IP Blocking** - Block bad actors

## 📝 License

MIT License - See LICENSE file

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a PR

---

**Star ⭐ if you like this project!**
