# Baymax

## 📁 Project Structure

```
Baymax/
├── LICENSE                    # Project license
├── README.md                  # Project documentation
├── server/                    # Backend server code
│   ├── .env                   # Environment variables (MongoDB config)
│   ├── main.py                # FastAPI application entry point
│   ├── requirements.txt       # Python dependencies
│   │
│   ├── auth/                  # Authentication module
│   │   ├── hashing.py         # Password hashing utilities (bcrypt)
│   │   ├── models.py          # Pydantic models for requests
│   │   └── routes.py         # Authentication API endpoints
│   │
│   ├── config/               # Configuration module
│   │   └── db.py             # MongoDB connection and setup
│   │
│   └── serverenv/             # Conda virtual environment
│       ├── bin/               # Executable binaries
│       ├── lib/               # Python packages
│       ├── conda-meta/        # Environment metadata
│       └── ...                   # Other environment files
│
└── __pycache__/               # Python bytecode cache (auto-generated)
```

### 📋 Key Files Description

| File/Directory | Purpose |
|----------------|---------|
| `server/main.py` | FastAPI application with health check and auth router |
| `server/auth/routes.py` | User signup, login, and authentication endpoints |
| `server/auth/models.py` | Pydantic models for API request validation |
| `server/auth/hashing.py` | Password hashing and verification using bcrypt |
| `server/config/db.py` | MongoDB connection, database initialization |
| `server/.env` | Environment variables (MongoDB URI, credentials) |
| `server/requirements.txt` | Python package dependencies |

### 🔗 API Endpoints

- `GET /health` - Health check endpoint
- `POST /auth/signup` - User registration
- `POST /auth/login` - User authentication

### 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Authentication**: HTTP Basic Auth with bcrypt
- **Environment**: Conda virtual 


Frontend - streamlit run main.py
Backend - uvicorn main:app --reload  