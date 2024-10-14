# Synthetic Data Generator

This project provides a synthetic data generator using the LangChain Ollama model integrated with Streamlit for UI and FastAPI for API-based data generation. The system allows users to specify the number of records, data format, and headers to generate realistic and well-structured synthetic data.

## Prerequisites

1. **Python 3.8+**
2. **Ollama**: The `llama3.1` model from Ollama for local inference.

## Initial Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Download and Install Ollama

Visit [ollama.com](https://ollama.com) to download and install Ollama on your system.

### Step 3: Pull the `llama3.1` Model

After installing Ollama, run the following command to download the `llama3.1` model (8B version):

```bash
ollama pull llama3.1
```

### Step 4: Test the Model

To ensure the model is working, run:

```bash
ollama run llama3.1
```

This will start the model and allow you to interact with it locally.

### Step 5: Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# For Windows users:
# venv\Scripts\activate
```

### Step 6: Install Dependencies

Install all required packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Application

### Streamlit App (UI)

To launch the Streamlit-based synthetic data generation UI:

```bash
streamlit run demo.py
```

This will start the app, and you can access it through your web browser to interactively generate synthetic data.

### FastAPI Endpoint (API)

To run the FastAPI-based API for synthetic data generation:

```bash
python3 data_gen_api.py
```

The FastAPI server will start, and you can use tools like Postman or cURL to interact with the `http://localhost:8000/generate-synthetic-data/` endpoint.

## Project Structure

- **`demo.py`**: The main Streamlit app file for the UI interface.
- **`data_gen_api.py`**: The FastAPI application exposing an API endpoint for data generation.
- **`requirements.txt`**: Contains the required dependencies for both Streamlit and FastAPI.

## Usage

- **Streamlit App**: You can generate synthetic data interactively by selecting the number of records, data format (CSV, JSON, etc.), and specifying field headers.
- **FastAPI API**: Programmatically generate synthetic data by sending a `POST` request with parameters like the number of records, data format, and headers.

### Example API Call (via Postman or cURL):

```json
{
    "num_records": 5,
    "data_format": "CSV",
    "headers": ["from", "to", "credit/debit", "timestamp"],
    "instructions": "Ensure 'from' and 'to' fields are names, and 'credit/debit' should be either 'credit' or 'debit'."
}
```

This request will generate 5 records in CSV format with the specified headers.

