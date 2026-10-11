# QR Code Generator and Scanner

A lightweight web application built with Python and Streamlit to generate custom QR codes and decode existing ones instantly.

## Project Structure
```
QR_Code_Generator_Scanner/
│
├── backend/
│   ├── __init__.py
│   └── qr_processor.py
├── frontend/
│   ├── __init__.py
│   └── app.py
├── requirements.txt
└── README.md
```

## How to Run in VS Code

1. Extract this ZIP folder and open the `QR_Code_Generator_Scanner` folder in **Visual Studio Code**.
2. Open the integrated terminal in VS Code (`Ctrl + ~` or `Cmd + ~`).
3. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Streamlit application:
   ```bash
   streamlit run frontend/app.py
   ```
