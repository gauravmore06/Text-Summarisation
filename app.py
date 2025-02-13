import validators
import streamlit as st
import yt_dlp
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader

# Streamlit App Config
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize a YouTube Video or Webpage")

# Sidebar for API Key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("Enter a YouTube or Website URL", placeholder="Paste your link here...")

# Model
llm = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key=groq_api_key)

# Prompt Template
prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Function to Get YouTube Transcript Using yt-dlp
def get_youtube_transcript(url):
    ydl_opts = {"quiet": True, "writeautomaticsub": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            subtitles = info_dict.get("subtitles", {})
            if subtitles:
                return subtitles
            else:
                return "Transcript not available."
        except Exception as e:
            return f"Error fetching transcript: {e}"

# Summarization Process
if st.button("Summarize Content"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the API key and a valid URL.")
    elif not validators.url(generic_url):
        st.error("Invalid URL. Please enter a valid YouTube or Website URL.")
    else:
        try:
            with st.spinner("Processing..."):
                # Loading the YouTube Video or Website
                if "youtube.com" in generic_url:
                    transcript = get_youtube_transcript(generic_url)
                    docs = [{"text": transcript}]
                else:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False)
                    docs = loader.load()

                # Summarization Chain
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success(output_summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")
