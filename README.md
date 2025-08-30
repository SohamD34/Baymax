# Baymax

## Project Structure

```
Baymax/
├── LICENSE                    # Project license
├── README.md                  # Project documentation
│
├──  server/                   # Backend server code
│   ├── .env                   # Environment variables (MongoDB, Pinecone, Google API)
│   ├── main.py                # FastAPI application entry point
│   ├── requirements.txt       # Python dependencies
│   │
│   ├── auth/                  # Authentication module
│   │   ├── hashing.py         # Password hashing utilities (bcrypt)
│   │   ├── models.py          # Pydantic models for requests
│   │   └── routes.py         # Authentication API endpoints
│   │
│   ├── chat/                  # Chat functionality module
│   │   ├── chat_query.py      # Chat query processing
│   │   └── routes.py         # Chat API endpoints
│   │
│   ├──  config/               # Configuration module
│   │   └── db.py             # MongoDB connection and setup
│   │
│   ├── docs/                  # Document management module
│   │   ├── routes.py         # Document upload API endpoints
│   │   └── vectorstore.py     # Pinecone vectorstore operations
│   │
│   ├── uploaded_docs/         # Directory for uploaded PDF files
│   │
│   └── serverenv/             # Conda virtual environment
│       ├── bin/               # Executable binaries
│       ├── lib/               # Python packages
│       ├── conda-meta/        # Environment metadata
│       └── ...                   # Other environment files
│
├── client/                    # Frontend client code
│   ├── .env                   # Client environment variables (API_URL)
│   ├── main.py                # Streamlit application entry point
│   ├── config.py             # Client configuration settings
│   ├── requirements.txt       # Python dependencies
│   │
│   ├── templates/             # UI templates and components
│   │   ├── __init__.py        # Package initialization
│   │   ├── auth.py            # Authentication UI components
│   │   └── index.py           # Main dashboard/home page
│   │
│   └── clientenv/             # Conda virtual environment
│       ├── bin/               # Executable binaries
│       ├── lib/               # Python packages
│       └── ...                   # Other environment files
│
└── __pycache__/               # Python bytecode cache (auto-generated)
```

### Key Files Description

| File/Directory | Purpose |
|----------------|---------|
| **Backend (Server)** |
| `server/main.py` | FastAPI application with health check, auth, chat, and docs routers |
| `server/auth/routes.py` | User signup, login, and authentication endpoints |
| `server/auth/models.py` | Pydantic models for API request validation |
| `server/auth/hashing.py` | Password hashing and verification using bcrypt |
| `server/chat/routes.py` | Chat API endpoints for AI interactions |
| `server/chat/chat_query.py` | Chat query processing and AI response generation |
| `server/docs/routes.py` | Document upload and management endpoints |
| `server/docs/vectorstore.py` | Pinecone vectorstore operations for document embeddings |
| `server/config/db.py` | MongoDB connection, database initialization |
| `server/.env` | Environment variables (MongoDB, Pinecone, Google API keys) |
| `server/requirements.txt` | Python package dependencies for backend |
| **Frontend (Client)** |
| `client/main.py` | Streamlit application entry point with session management |
| `client/templates/auth.py` | Authentication UI components (login/signup forms) |
| `client/templates/index.py` | Main dashboard and home page components |
| `client/config.py` | Client configuration settings and constants |
| `client/.env` | Client environment variables (API_URL) |
| `client/requirements.txt` | Python package dependencies for frontend |

### API Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/` | GET | Welcome message and API information | No |
| `/health` | GET | Health check endpoint | No |
| `/signup` | POST | User registration | No |
| `/login` | POST | User authentication | Basic Auth |
| `/chat` | POST | AI chat interaction | Basic Auth |
| `/upload_docs` | POST | Document upload (admin only) | Basic Auth (Admin) |

### Technology Stack

**Backend:**
- **Framework**: FastAPI (Python)
- **Database**: MongoDB Atlas
- **Vector Database**: Pinecone
- **Authentication**: HTTP Basic Auth with bcrypt
- **AI/ML**: Google Generative AI (Gemini), LangChain
- **Document Processing**: PyPDF, RecursiveCharacterTextSplitter
- **Environment**: Conda virtual environment

**Frontend:**
- **Framework**: Streamlit (Python)
- **UI Components**: Streamlit widgets and layouts
- **HTTP Client**: Requests library
- **Session Management**: Streamlit session state

### Setup and Running

**Backend Server:**
```bash
cd server
conda activate serverenv  # or your environment name
uvicorn main:app --reload
```

**Frontend Client:**
```bash
cd client
conda activate clientenv  # or your environment name
streamlit run main.py
```

**Access Points (Dev)**
- **Backend API**: `http://127.0.0.1:8000`
- **Frontend UI**: `http://localhost:8501`
- **API Documentation**: `http://127.0.0.1:8000/docs`  