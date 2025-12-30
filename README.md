# Questar Streamlit

Streamlit web application that provides a **chat-based interface** secured by login, used to send questions to a backend API and display structured responses.

The application manages authentication, session state, and chat history entirely on the frontend, while delegating business logic to external services.

---

## What This App Does

- Requires **user authentication** before access
- Provides a **chat interface** for user questions
- Sends questions to an external API service
- Displays:
  - Assistant text responses
  - Optional SQL queries
  - Optional tabular results
- Maintains conversation state during the session

---

## Project Structure

```text
src/
├── app.py                 # Streamlit entry point
├── components/
│   ├── login.py           # Login form and authentication flow
│   └── sidebar.py         # Sidebar UI and logout
├── services/
│   ├── api.py             # API request handler
│   └── auth.py            # User authentication logic
└── utils/
    └── session.py         # Session state initialization
```

Other important files:

- `.env` – credentials and configuration
- `.streamlit/config.toml` – Streamlit configuration
- `Dockerfile` – containerized execution
- `Makefile` – execution shortcuts

---

## Authentication

- Users are validated using credentials loaded from environment variables
- Login state is stored in `st.session_state`
- Logout clears the session and forces rerun

---

## Environment Variables

Create a `.env` file with valid credentials and backend configuration.

Example:

```env
VALID_USERS=user1:password1,user2:password2
API_URL=http://backend-service/endpoint
```

---

## Run Locally

```bash
pip install -e .
streamlit run src/app.py
```

---

## Run with Docker

```bash
docker build -t questar-streamlit .
docker run --env-file .env -p 8501:8501 questar-streamlit
```

---

## Notes

- No backend logic lives in this repository
- The API response format is assumed and not validated
- Session data is not persisted across reloads

---

## Author
Leonardo Vilela Ribeiro
