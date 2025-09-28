# Campus Concierge - VT AI Voice Assistant

An AI-powered voice assistant designed specifically for Virginia Tech students to help with dining, transportation, and campus events.

## 🎯 Features

- **Voice Interaction**: Speech-to-text and text-to-speech using Web Speech API
- **AI-Powered Responses**: Natural language processing with LangChain and OpenAI
- **Real-time Data**: Web scraping for current dining, bus, and event information
- **Modern UI**: Beautiful React interface with TailwindCSS
- **Campus-Specific**: Tailored for Virginia Tech students

## 🏗️ Architecture

### Backend (FastAPI + LangChain)
- **FastAPI**: REST API with CORS support
- **LangChain**: AI orchestration and natural language processing
- **Web Scraping**: Real-time data from VT dining, Blacksburg Transit, and Gobbler Connect
- **OpenAI Integration**: GPT-powered responses

### Frontend (React + TypeScript)
- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe development
- **Web Speech API**: Voice recognition and synthesis
- **TailwindCSS**: Beautiful, responsive UI
- **Vite**: Fast development and building

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Run the backend:**
   ```bash
   python main.py
   ```
   
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```
   
   The app will be available at `http://localhost:3000`

## 📱 Usage

1. **Open the application** in your browser (Chrome or Edge recommended for voice support)
2. **Click the microphone button** to start voice input
3. **Ask questions** like:
   - "Which dining halls are open?"
   - "What bus routes are available?"
   - "What club events are coming up?"
4. **Listen to responses** - the assistant will speak answers aloud

## 🔧 API Endpoints

### POST /ask
Main endpoint for AI-powered campus queries.
```json
{
  "query": "Which dining halls are open?"
}
```

### GET /dining
Get current dining hall status.

### GET /bus
Get current bus times and schedules.

### GET /clubs
Get upcoming club events.

## 🎨 Customization

### Adding New Data Sources
1. Create a new scraper in `backend/scrapers/`
2. Add the tool to `backend/langchain_agent.py`
3. Update the frontend quick actions

### Styling
- Modify `frontend/src/index.css` for global styles
- Update `frontend/tailwind.config.js` for theme customization
- VT colors are predefined: `vt-orange` and `vt-maroon`

## 🛠️ Development

### Backend Development
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Building for Production
```bash
# Frontend
cd frontend
npm run build

# Backend
cd backend
# Use your preferred WSGI server (gunicorn, uvicorn, etc.)
```

## 📦 Dependencies

### Backend
- FastAPI: Web framework
- LangChain: AI orchestration
- OpenAI: GPT integration
- BeautifulSoup4: Web scraping
- Requests: HTTP client
- Uvicorn: ASGI server

### Frontend
- React 18: UI framework
- TypeScript: Type safety
- Axios: HTTP client
- TailwindCSS: Styling
- Lucide React: Icons
- Vite: Build tool

## 🐛 Troubleshooting

### Voice Recognition Not Working
- Ensure you're using Chrome or Edge
- Check microphone permissions
- Try refreshing the page

### API Connection Issues
- Verify backend is running on port 8000
- Check CORS settings
- Ensure OpenAI API key is set

### Scraping Issues
- Some sites may block automated requests
- Check internet connection
- Verify target websites are accessible

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Virginia Tech for campus resources
- OpenAI for GPT API
- LangChain for AI orchestration
- The open-source community for amazing tools

---

**Built with ❤️ for Virginia Tech students**
