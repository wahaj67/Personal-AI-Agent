# 🤖 Personal Assistant AI Agent

An intelligent, async-powered AI agent built using custom agent orchestration logic and Google's Gemini models. This assistant understands your requests and executes tasks based on natural language instructions — acting like a reliable, real-time digital co-pilot.

---

## 🌟 Features

- 🔮 **Gemini-Powered Intelligence**  
  Leverages Google's Gemini model (`gemini-2.0-flash`) for fast and contextual AI responses.

- ⚡ **Async Execution**  
  Built using `AsyncOpenAI` client (custom-configured), ensuring non-blocking performance for better concurrency and speed.

- 🧠 **Agent-Based Architecture**  
  Modular `Agent`, `Runner`, and `Model` classes allow clean separation of concerns and easy scalability.

- 🔐 **Secure Configuration with `.env`**  
  API keys and environment variables are safely managed via `python-dotenv`.

---

## 📦 Requirements

Install dependencies:

```bash
pip install openai python-dotenv
```
## Getting Started

Clone the repository.

Create a .env file:
GEMINI_API_KEY=your_google_gemini_api_key_here

## Run the agent:
python3 main.py

## 🤝 Credits
Built with ❤️ using:

Google Gemini API

Custom agent architecture

Async Python + OpenAI SDK

## 📫 Contact
For business inquiries, suggestions or collaborations:

📧 wahaj0574@gmail.com

