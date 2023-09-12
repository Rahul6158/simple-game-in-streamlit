import streamlit as st
from translate import Translator
from gtts import gTTS
import os
import base64
from docx import Document

# Define the language mapping
language_mapping = {
    "en": "English",
    "es": "Spanish",
    # Add more languages as needed
}

# Function to translate text
def translate_text(text, target_language):
    if target_language in language_mapping:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
    else:
        return "Language not found in the mapping"

# Function to convert text to speech and save as an MP3 file
def convert_text_to_speech(text, output_file, language='en'):
    if text:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)
    else:
        st.warning("No text to speak")

def get_binary_file_downloader_html(link_text, file_path, file_format):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    b64_file = base64.b64encode(file_data).decode()
    download_link = f'<a href="data:{file_format};base64,{b64_file}" download="{os.path.basename(file_path)}">{link_text}</a>'
    return download_link

def main():
    st.image("jangirii.png", width=50)
    st.title("Document Translation and Conversion to Speech")

    # Allow users to upload a DOCX file
    uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

    if uploaded_file:
        # Read the uploaded DOCX file and extract text
        doc = Document(uploaded_file)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    else:
        text = ""

    target_language = st.selectbox("Select target language:", list(language_mapping.values()))

    # Check if the target language is in the mapping
    target_language_code = [code for code, lang in language_mapping.items() if lang == target_language][0]

    # Translate the extracted text
    translated_text = translate_text(text, target_language_code)

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

        # Provide download link for the MP3 file
        st.markdown(get_binary_file_downloader_html("Download Audio File", output_file, 'audio/mp3'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
