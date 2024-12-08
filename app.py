import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from docx import Document

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file.")

# Configure API key for Google
genai.configure(api_key=api_key)

# Helper functions for file processing
def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Function to check if a query is related to Data Science dynamically
def is_data_science_topic_dynamic(query):
    try:
        # Use Google Generative AI to classify the query
        prompt = (
            f"Determine if the following query is related to the field of Data Science. "
            f"Query: '{query}'\n"
            f"Respond with 'Yes' if it is related to Data Science, 'No' if it is not, and provide a short explanation."
        )
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        response_text = response.text.strip().lower()
        
        # Parse the response
        if "yes" in response_text:
            return True, response.text
        return False, response.text
    except Exception as e:
        print(f"Error in dynamic query classification: {e}")
        return False, "Error determining the relevance of the query."

# Function to generate a response for Data Science queries
def generate_response_with_google(query):
    try:
        prompt = (
            f"Explain the topic '{query}' in a detailed, structured way. "
            "Please provide the following sections in this order: \n"
            "1. **Complete Theory Description:** Provide a detailed theoretical explanation of the topic. \n"
            "2. **Mathematical Description:** Include the relevant mathematical equations and explanations. \n"
            "3. **Python Code Snippet:** Provide a Python code example that demonstrates how to implement this concept, along with a detailed explanation of the code. \n"
            "Make sure each section is clearly marked, and provide all necessary details in a clean and readable format."
        )
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating response with Google AI: {e}")
        return "Error generating response. Please try again."

# Streamlit UI
def main():
    st.title("Project: Freedom")
    st.markdown(
        "<p style='font-size:20px;'>Hello! I am Freedom, your personal Data Science tutor powered by Gemini. How may I assist you today?</p>",
        unsafe_allow_html=True,
    )

    # Maintain the chat history in session state
    if "history" not in st.session_state:
        st.session_state.history = []

    # Sidebar displays the history of queries
    st.sidebar.title("Search History")
    for entry in st.session_state.history:
        # Make each query clickable
        if st.sidebar.button(f"Query: {entry['query']}"):
            # Display the corresponding response in the main area when clicked
            st.session_state.selected_query = entry
            st.markdown(f"**User:** {entry['query']}")
            st.markdown(f"**Freedom:** {entry['response']}")

    # Instruction statement in small font in the sidebar
    st.sidebar.markdown(
        """
        <hr style="margin: 10px 0;">
        <p style="font-size: 14px; font-style: bold; color: gray;">
        Instructions:<br>
        - Upload a file (image, PDF, or Word document) to analyze its content.<br>
        or<br>
        - Enter a Data Science topic to receive a detailed explanation.<br>
        - View query history in the sidebar.<br>
        </p>
        """,
        unsafe_allow_html=True,
    )

    # File uploader
    file = st.file_uploader("Upload a file (image, PDF, or Word document):", type=["png", "jpg", "jpeg", "pdf", "docx"])
    query = None
    uploaded_image = None

    if file:
        # Process the uploaded file
        if file.type.startswith("image"):
            uploaded_image = Image.open(file)
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)  # Display the uploaded image
            query = extract_text_from_image(file)
        elif file.type == "application/pdf":
            query = extract_text_from_pdf(file)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            query = extract_text_from_docx(file)
        else:
            st.error("Unsupported file type!")

    # Text input for manual topic
    if not query:
        query = st.text_input("Or enter a Data Science topic:")

    if query and st.button("Generate Response"):
        is_relevant, explanation = is_data_science_topic_dynamic(query)
        if is_relevant:
            response = generate_response_with_google(query)
            # Add the query and response to session history
            st.session_state.history.append({"query": query, "response": response})
            st.markdown(f"**User:** {query}")
            if uploaded_image:
                st.image(uploaded_image, caption="Uploaded Image for Reference", use_container_width=True)
            st.markdown(f"**Freedom:** {response}")
        else:
            st.warning(f"Sorry, I can only answer Data Science-related queries. Here's why: {explanation}")

if __name__ == "__main__":
    main()
