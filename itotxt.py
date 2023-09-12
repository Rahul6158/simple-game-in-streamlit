import streamlit as st
import os
import base64
import docx2txt
from googletrans import Translator
from gtts import gTTS
from docx import Document
import io

# Function to extract text from a DOCX file
def process_docx_text(docx_file):
    # Extract text from the DOCX file
    text = docx2txt.process(docx_file)
    return text

# Function to translate text using Google Translate API
def translate_text_google(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Function to convert text to speech and save as an MP3 file
def convert_text_to_speech(text, output_file, language='en'):
    if text:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)

# Function to convert translated text to a Word document
def convert_text_to_word_doc(text, output_file):
    doc = Document()  # Create a new Word document
    doc.add_paragraph(text)  # Add the translated text as a paragraph

    # Save the document to a BytesIO buffer
    output_buffer = io.BytesIO()
    doc.save(output_buffer)
    output_buffer.seek(0)

    # Write the buffer contents to the specified output file
    with open(output_file, 'wb') as f:
        f.write(output_buffer.read())

# Function to generate a download link for a file
def get_binary_file_downloader_html(link_text, file_path, file_format):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    b64_file = base64.b64encode(file_data).decode()
    download_link = f'<a href="data:{file_format};base64,{b64_file}" download="{os.path.basename(file_path)}">{link_text}</a>'
    return download_link

language_mapping = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    # Add more languages as needed
}

# Main Streamlit app
def main():
    st.image("jangirii.png", width=50)
    st.title("Text Translation and Conversion to Speech (English - other languages)")

    # Add a file uploader for DOCX files
    uploaded_docx = st.file_uploader("Upload a DOCX file", type=["docx"])

    if uploaded_docx is not None:
        # Read the uploaded DOCX file and process its text content
        docx_text = process_docx_text(uploaded_docx)

        # Display the extracted text
        st.subheader("Text Extracted from Uploaded DOCX:")
        st.write(docx_text)

        target_language = st.selectbox("Select target language:", list(language_mapping.values()))

        # Check if the target language is in the mapping
        target_language_code = [code for code, lang in language_mapping.items() if lang == target_language][0]

        # Translate the extracted text using Google Translate
        translated_text = translate_text_google(docx_text, target_language_code)

        # Display translated text
        if translated_text:
            st.subheader(f"Translated text ({target_language}):")
            st.write(translated_text)
        else:
            st.warning("Translation result is empty. Please check your input text.")

        # Convert the translated text to speech
        if st.button("Convert to Speech"):
            output_file = "translated_speech.mp3"
            convert_text_to_speech(translated_text, output_file, language=target_language_code)

            # Play the generated speech
            audio_file = open(output_file, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')

            # Play the generated speech (platform-dependent)
            if os.name == 'posix':  # For Unix/Linux
                os.system(f"xdg-open {output_file}")
            elif os.name == 'nt':  # For Windows
                os.system(f"start {output_file}")
            else:
                st.warning("Unsupported operating system")

            # Provide a download link for the MP3 file
            st.markdown(get_binary_file_downloader_html("Download Audio File", output_file, 'audio/mp3'), unsafe_allow_html=True)

        # Convert the translated text to a Word document
        if st.button("Convert to Word Document"):
            word_output_file = "translated_text.docx"
            convert_text_to_word_doc(translated_text, word_output_file)

            # Provide a download link for the Word document
            st.markdown(get_binary_file_downloader_html("Download Word Document", word_output_file, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
