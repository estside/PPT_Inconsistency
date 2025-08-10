# AI Inconsistency Detector: Django Web App

This is a web-based tool built with Django that analyzes a multi-slide PowerPoint presentation (`.pptx`) to find factual or logical inconsistencies. It provides a user-friendly interface for file uploads, real-time feedback, and a downloadable analysis report.

## Features
- **Intuitive Web UI**: A simple and clean interface for uploading `.pptx` files.
- **Live Analysis Log**: The app streams a log of the analysis process in real-time to the browser, providing instant feedback and a sense of progress.
- **Comprehensive Inconsistency Detection**: The backend script performs an exhaustive pairwise analysis of all slides to detect conflicting numerical data, contradictory textual claims, and timeline mismatches.
- **Clean, Downloadable Report**: The final report consolidates all findings into a single, de-duplicated, and well-structured text file (`final_report.txt`) that can be downloaded by the user.

## How It Works
The application uses a client-server architecture with a streaming response to achieve real-time feedback:
1.  **File Upload**: A user uploads a `.pptx` file via the web form.
2.  **Server-Side Processing**: The Django server receives the file and initiates a streaming process. It uses `python-pptx` to extract text and images from the presentation.
3.  **Real-Time Analysis**: The server iterates through every possible pair of slides (`O(n^2)` complexity) and sends a detailed prompt to the Gemini 2.5 Flash API for inconsistency detection.
4.  **Live Log**: The server sends a live log of its progress to the browser via **Server-Sent Events (SSE)**.
5.  **Final Report**: Once all comparisons are complete, the server consolidates all findings, removes duplicates, and generates a single, final report. This report is sent as a final data chunk to the browser and saved for download.
6.  **Download**: The user can download the final `inconsistency_report.txt` file, which is the same report displayed in the live log.

## Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/estside/PPT_Inconsistency/
    cd https://github.com/estside/PPT_Inconsistency/inconsistency_app
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Set your Gemini API key:**
    Obtain a key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and set it as an environment variable.
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

## Usage
1.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
2.  **Access the app:** Open your web browser and navigate to `http://127.0.0.1:8000`.
3.  **Upload and Analyze**: Use the form to upload a `.pptx` file. The live log will show the analysis in real-time, and a download link will appear upon completion.

## Limitations
- **Scalability**: The `O(n^2)` pairwise comparison can be slow for very large presentations (e.g., decks with hundreds of slides).
- **API Rate Limits**: The script's performance is subject to the Gemini API's rate limits.
- **Image Resolution**: The accuracy of text extraction from images depends on the resolution and clarity of the images within the deck.
