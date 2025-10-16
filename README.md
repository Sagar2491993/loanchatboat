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

example:

python -m venv sagarenv

sagarenv\Scripts\activate


###  Install dependencies
pip install -r requirements.txt

---
### Open .env in a text editor and add your personal API credentials:
GOOGLE_API_KEY=your_gemini_api_key

HUGGINGFACEHUB_API_TOKEN=your_huggingface_token







---
### ▶️ Run the Project
python main.py





---
### ▶️ Run the Project
python main.py


---
### 📂 Project Structure
bank_of_maharashtra_loan_scraper/
│
├── main.py                    # Entry point script

├── scraper.py                 # Web scraping logic

├── data/

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


---
### 👨‍💻 Author
Sagar Abhang

AI/ML Engineer 

📧 sagarabhang276@gmail.com




