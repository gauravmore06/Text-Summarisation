# Text-Summarisation

LangChain YouTube & Webpage Summarizer

This is a Streamlit-based web application that allows users to summarize content from YouTube videos and web pages using LangChain and Groq's LLMs.

Features

Summarize YouTube video transcripts automatically.

Extract text from web pages and generate concise summaries.

Uses langchain with ChatGroq for text summarization.

Supports YouTube transcript extraction via yt-dlp and youtube_transcript_api.

User-friendly Streamlit interface for easy input and output.

Installation

Prerequisites

Python 3.8+

A Groq API Key (sign up at Groq)

Setup

Clone the repository and navigate to the project directory:

git clone https://github.com/your-repo/langchain-summarizer.git
cd langchain-summarizer

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py

Enter your Groq API key in the sidebar.

Paste a YouTube video URL or a webpage URL.

Click "Summarize Content" and wait for the result.

Configuration

If using environment variables for API keys, set them before running the app:

export GROQ_API_KEY=your_api_key

On Windows (PowerShell):

$env:GROQ_API_KEY="your_api_key"

Dependencies

streamlit

yt-dlp

youtube_transcript_api

validators

langchain

langchain_groq

langchain_community

