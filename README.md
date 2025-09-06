📂 Document Data Extractor
A cross-platform Python application that automates the extraction of structured data from specific document formats (e.g., Belarc HTML reports). The application features a lightweight file upload interface and exports the extracted information into structured Excel sheets for easy access and analysis.

🚀 Features
📂 Upload multiple files at once
🕵️ Automated parsing with BeautifulSoup and Selenium
📊 Export results into Excel sheets using pandas, openpyxl, and xlsxwriter
💻 Cross-platform support (works on desktops & laptops)
⚙️ Installation & Setup

Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create a virtual environment:
python -m venv venv

Activate it:
Windows (PowerShell):
.\venv\Scripts\activate

Linux/Mac:
source venv/bin/activate
Install dependencies:
pip install pandas openpyxl xlsxwriter beautifulsoup4 selenium
Run the application:
python app.py

📤 Usage
Launch the app (python app.py).
Use the interface to upload Belarc HTML files (or other supported formats).
Click Submit to process.
Extracted data will be saved into an Excel sheet in the project folder.

🛠 Tech Stack
Python
BeautifulSoup, Selenium – Data parsing
pandas, openpyxl, xlsxwriter – Excel export
