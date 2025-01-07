# QnA Chatbot

A Streamlit-based question-answering chatbot powered by Ollama that provides concise, informative responses.

## Features

- Real-time question answering with responses limited to 6 sentences
- Model selection between Gemma 2:2b and LLama3.2
- Adjustable temperature (creativity level) from 0.00 to 1.00
- Token-optimized responses for faster conversation speed
- Dark mode interface
- Streamlit-powered web application

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Access the settings panel using the ">" button in the top left
2. Select your preferred model (Gemma2:2b or LLama3.2)
3. Adjust the temperature slider to control response creativity
4. Enter your question in the text input field
5. Click "ask" or press Enter to generate a response

## Technical Details

- Framework: Streamlit
- Backend: Ollama
- Models: Gemma2:2b, LLama3.2
- Response Limit: 6 sentences maximum
- Temperature Range: 0.00 - 1.00
- Token Optimization: Enabled for faster responses

## Requirements

See requirements.txt for complete dependencies
