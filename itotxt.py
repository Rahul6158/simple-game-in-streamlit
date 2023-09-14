import streamlit as st

# ... (rest of your code)

# Main Streamlit app
def main():
    # Add custom CSS to change text color to white
    st.markdown(
        """
        <style>
        .stTextInput,
        .stTextArea,
        .stMarkdown {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
            word_output_file = "translated_text.docx"
            convert_text_to_word_doc(translated_text, word_output_file)

            # Display the Word document as HTML
            with open(word_output_file, "rb") as f:
                html_data = convert_word_doc_to_html(f)
            st.subheader("Preview of Translated Text as Word Document:")
            st.components.v1.html(html_data, width=600, height=800)
            
            # Provide a download link for the Word document
            st.markdown(get_binary_file_downloader_html("Download Word Document", word_output_file, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
