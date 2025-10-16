# 🏦 Bank of Maharashtra Loan Data Scraper

This project extracts **clean and structured loan information** from the official [Bank of Maharashtra](https://bankofmaharashtra.in) website using **Python**, **Requests**, and **BeautifulSoup**.

It scrapes all loan scheme pages to collect essential details like **loan descriptions**, **eligibility**, **interest rates**, **features**, and **repayment details**, while filtering out unnecessary content such as navigation links and “Apply Online” buttons.

All processed data is stored in a single file — `document.txt` — which is ideal for **AI chatbot training**, **RAG (Retrieval-Augmented Generation)** systems, or **data analytics pipelines**.

---

## 🚀 Features

✅ Automatically scrapes all loan-related web pages  
✅ Extracts key HTML tags:
- `<h1>`, `<h2>`, `<h3>`, `<h4>` — Titles and subtitles  
- `<p>` — Paragraph text  
- `<table>` — Structured data (interest rates, eligibility, tenure)  
✅ Cleans irrelevant data (like “Click Here”, “Apply Online”)  
✅ Saves cleaned and structured data into `document.txt`  
✅ Can be easily integrated with **LangChain**, **Gemini**, or **RAG pipelines**

---

## 🧠 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Programming Language | Python 3.10+ |
| Web Scraping | Requests, BeautifulSoup4 |
| Environment Variables | python-dotenv |
| AI Integration (optional) | LangChain, Gemini API |
| Data Storage | Plain Text / Document File |

---

## ⚙️ Environment Setup

Create and activate a virtual environment:

<<<<<<< HEAD
```bash
Create virtual environment
Example:
=======
<<<<<<< HEAD

## Create virtual environment
=======
```bash
Create virtual environment
Example:
>>>>>>> b6e9325 (update code)
>>>>>>> cbb8b65 (update)
python -m venv sagarenv

# Activate (Windows)
sagarenv\Scripts\activate

<<<<<<< HEAD
```
###  Install dependencies
pip install -r requirements.txt

---
### Open .env in a text editor and add your personal API credentials:
=======
<<<<<<< HEAD

## Install dependencies:
pip install -r requirements.txt

## Create a .env file in the root directory and add:
=======
```
###  Install dependencies
pip install -r requirements.txt

---
### Open .env in a text editor and add your personal API credentials:
>>>>>>> b6e9325 (update code)
>>>>>>> cbb8b65 (update)
GOOGLE_API_KEY=your_gemini_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
<<<<<<< HEAD


---
### ▶️ Run the Project
python main.py


<<<<<<< HEAD
---
### 📂 Project Structure
bank_of_maharashtra_loan_scraper/
=======
## 📂 Project Structure

## bank_of_maharashtra_loan_chatboat/
=======


---
### ▶️ Run the Project
python main.py


---
### 📂 Project Structure
bank_of_maharashtra_loan_scraper/
>>>>>>> b6e9325 (update code)
>>>>>>> cbb8b65 (update)
│
├── main.py                    # Entry point script
├── scraper.py                 # Web scraping logic
├── data/
<<<<<<< HEAD
│   └── document.txt           # Output file
├── prompt/                    # LLM or chatbot templates
├── .env                       # API keys and environment variables
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation
=======
<<<<<<< HEAD
│   └── document.txt           # Output file.
>>>>>>> cbb8b65 (update)

---
### 🌱 Future Improvements
Export data in JSON or CSV formats
Implement async scraping with aiohttp for faster execution
Automatically generate short Q&A pairs from scraped content to reduce hallucinations in AI chatbots


---
### 📜 License
This project is released under the MIT License — feel free to use, modify, and distribute.


<<<<<<< HEAD
=======
AI/ML Engineer.

📧 sagarabhang276@gmail.com.
=======
│   └── document.txt           # Output file
├── prompt/                    # LLM or chatbot templates
├── .env                       # API keys and environment variables
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation

---
### 🌱 Future Improvements
Export data in JSON or CSV formats
Implement async scraping with aiohttp for faster execution
Automatically generate short Q&A pairs from scraped content to reduce hallucinations in AI chatbots


---
### 📜 License
This project is released under the MIT License — feel free to use, modify, and distribute.


>>>>>>> cbb8b65 (update)
---
### 👨‍💻 Author
Sagar Abhang
AI/ML Engineer 
📧 sagarabhang276@gmail.com
<<<<<<< HEAD
=======
>>>>>>> b6e9325 (update code)
>>>>>>> cbb8b65 (update)



