# Project-Freedom
An AI Powered One Stop Solution Application for all Data Science Related queries
# 📚 Project Freedom: Your Personal Data Science Tutor

Welcome to **Project Freedom** – a powerful, AI-driven application designed to simplify and enhance your Data Science learning experience. Whether you're diving into theoretical concepts, mathematical insights, or Python implementation, Freedom is here to guide you every step of the way.

---

## 🚀 Features

- **AI-Powered Assistance**: Get detailed answers to your Data Science queries using Google’s Gemini Generative AI.
- **Dynamic Query Recognition**: Automatically identifies whether a query is related to Data Science.
- **File Processing**: Extracts and processes text from:
  - Images (using Tesseract OCR)
  - PDFs (using PyMuPDF)
  - Word documents (using Python-Docx)
- **Comprehensive Responses**: Outputs structured answers with:
  1. Theoretical explanations.
  2. Mathematical descriptions and equations.
  3. Python code snippets with explanations.
- **Search History**: Keeps track of your past queries for quick access.
- **User-Friendly Interface**: Built with **Streamlit**, providing an intuitive, professional UI.

---

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Framework**: Streamlit
- **AI Model**: Google Generative AI (Gemini)
- **Libraries**:
  - `pytesseract` for Optical Character Recognition (OCR)
  - `fitz` (PyMuPDF) for PDF processing
  - `python-docx` for Word document parsing
  - `dotenv` for environment variable management
  - `Pillow` for image handling

---

## 🔧 Installation and Setup

Follow these steps to get the project up and running on your local system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/project-freedom.git
cd project-freedom
```

### 2️⃣ Install Dependencies

It’s recommended to use a virtual environment for this project:

```bash
# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key

- Create a `.env` file in the project root.
- Add your Google Generative AI API key in the following format:

```
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

### 5️⃣ Access the Application

Open your browser and navigate to:  
`http://localhost:8501`

---

## 📂 Project Structure

```
project-freedom/
│
├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── .env.example           # Example for environment variables
├── README.md              # Project documentation
│
├── utils/                 # Utility functions for processing files
    ├── ocr_utils.py       # OCR-related helper functions
    ├── pdf_utils.py       # PDF text extraction
    └── docx_utils.py      # Word document text extraction

```

---

## ✨ How to Use the Application

1. **Upload a File**: Upload

a PDF, Word document, or image for text extraction.  
2. **Ask a Query**: Enter a Data Science-related question in the query box.  
3. **Choose Output Type**: View the response in your preferred format (Theory, Math, or Python Code).  
4. **View History**: Access past queries from the sidebar.  

---

## 🌟 Future Enhancements

- Integration of more advanced AI models for improved responses.  
- Support for additional file formats (e.g., Excel).  
- Multi-language query support.  
- Enhanced visualization for mathematical explanations.  

---

## 🤝 Contributions

Contributions are welcome! If you'd like to improve the project or add new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork this repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

- **Email**: kingsukh.amit@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/amitkmazumdar/

---

**Thank you for checking out Project Freedom! Happy Learning!** 🎉

--- 

Customize the placeholders (e.g., API keys, email, and links) with your details before uploading. This structure is clear, professional, and easy for users to follow.
