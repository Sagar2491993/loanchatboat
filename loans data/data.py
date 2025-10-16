import requests
from bs4 import BeautifulSoup

# List of URLs to fetch
urls = [
    "https://bankofmaharashtra.in/personal-banking/loans/home-loan",
    "https://bankofmaharashtra.in/maha-super-housing-loan-scheme-for-construction-acquiring",
    "https://bankofmaharashtra.in/maha-super-housing-loan-scheme-for-purchase-plot-construction-thereon",
    "https://bankofmaharashtra.in/maha-super-housing-loan-scheme-for-repairs",
    "https://bankofmaharashtra.in/maha-super-flexi-housing-loan-scheme",
    "https://bankofmaharashtra.in/pradhan-mantri-awas-yojana-2",
    "https://bankofmaharashtra.in/loan-against-property",
    "https://bankofmaharashtra.in/educational-loans",
    "https://bankofmaharashtra.in/model-education-loan-scheme",
    "https://bankofmaharashtra.in/maha-bank-skill-loan-scheme",
    "https://bankofmaharashtra.in/pm-vidya-laxmi"
]

# File to save the combined extracted data
output_file = "document.txt"

with open(output_file, "w", encoding="utf-8") as file:
    for url in urls:
        print(f"Fetching data from: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f" Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Write page header
        file.write("="*80 + "\n")
        file.write(f"Source URL: {url}\n\n")

        #  Extract main title
        main_title = soup.find('h1')
        if main_title:
            file.write("Main Title:\n")
            file.write(main_title.get_text(strip=True) + "\n\n")

        #  Extract all headings (h2-h4)
        subheadings = soup.find_all(['h2', 'h3', 'h4'])
        if subheadings:
            file.write("Headings:\n")
            for sh in subheadings:
                text = sh.get_text(strip=True)
                if text and not any(kw in text.lower() for kw in ["apply", "click here", "download"]):
                    file.write("- " + text + "\n")
            file.write("\n")

        #  Extract all useful paragraphs
        file.write("Paragraphs:\n")
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text and not any(kw in text.lower() for kw in ["apply", "click here", "login", "register", "download"]):
                file.write(text + "\n\n")

        #  Extract any tables (for interest rates, tenure, etc.)
        tables = soup.find_all('table')
        if tables:
            file.write("Tables:\n")
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = [col.get_text(strip=True) for col in row.find_all(['th', 'td'])]
                    if cols:
                        file.write(" | ".join(cols) + "\n")
                file.write("\n")

        file.write("="*80 + "\n\n")

print("All useful loan scheme data successfully saved to document.txt")
