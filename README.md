# QA API Tool

Lightweight Python-based API testing tool for basic REST API validation.

## 📌 Purpose

This project was built as a learning and portfolio exercise to simulate basic QA/API testing workflows using Python.

It focuses on:
- API response validation
- Status code checks
- Simple automated test execution
- Basic QA mindset (expected vs actual results)

---

## ⚙️ Features

- Send GET requests to API endpoints
- Validate HTTP status codes
- Basic response checks
- Simple test runner (no external frameworks)

---

## 🧪 Example Use Case

Testing GitHub API endpoints:

- Check if API root endpoint is reachable
- Validate response status codes
- Verify presence of expected JSON keys

---

## 🚀 How to Run

Make sure you have Python 3 installed.

Install dependencies:

```bash
pip install requests

```

Run the tool:

```bash
python main.py
```

📁 Project Structure

qa-api-tool/
│
├── main.py          # Entry point
├── api_client.py    # Handles API requests
├── tests.py         # QA test logic
└── config.py        # API configuration

🧠 What I learned

- How REST APIs work in practice
- How to send and handle HTTP requests in Python
- How QA thinking translates into automated checks
- Basic test structuring without frameworks


📌 Future Improvements

- Add pytest-based test structure
- Add logging of test results
- Expand to POST/PUT/DELETE requests
- Add JSON schema validation
