import streamlit as st
from translate import Translator
from gtts import gTTS
import os
import base64
import docx2txt

# Function to extract text from a DOCX file
def process_docx_text(docx_file):
    # Extract text from the DOCX file
    text = docx2txt.process(docx_file)
    return text

# Function to translate text
def translate_text(text, target_language):
    if target_language in language_mapping:
        max_query_length = 500  # Adjust this limit as needed
        translator = Translator(to_lang=target_language)

        # Split the text into segments that fit within the query length limit
        segments = [text[i:i+max_query_length] for i in range(0, len(text), max_query_length)]

        # Translate each segment and combine the results
        translations = [translator.translate(segment) for segment in segments]
        translation = " ".join(translations)

        return translation
    else:
        return "Language not found in the mapping"

# Language mapping dictionary
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

        # Translate the extracted text
        translated_text = translate_text(docx_text, target_language_code)

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

if __name__ == "__main__":
    main()
