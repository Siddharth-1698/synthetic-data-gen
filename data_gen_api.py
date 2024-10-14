from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_ollama import ChatOllama

app = FastAPI()

# Define the input model for the API
class DataGenerationRequest(BaseModel):
    num_records: int
    data_format: str
    headers: list
    instructions: str = None

# Function to generate the prompt dynamically based on input
def generate_prompt(num_records, data_format, headers, instructions=None):
    headers_str = ", ".join(headers)
    prompt = (
        f"Generate exactly {num_records} records in {data_format} format with the following fields: {headers_str}. "
        "Make sure the data for each field is consistent, realistic, and matches typical data types for these fields. "
        f"Ensure the data is well-structured, diverse, and adheres to common standards for the {data_format} format. "
        "Output only the data without any additional text or comments."
    )
    
    # Append specific instructions if provided
    if instructions:
        prompt += f" follow below instructions/example: \n{instructions}"
    
    return prompt

# Function to generate the response from the local model
def generate_llm_response(prompts):
    '''
    Generates synthetic data
    '''
    chat_model = ChatOllama(model="llama3.1")
    return chat_model.invoke(prompts)

# POST endpoint to generate synthetic data
@app.post("/generate-synthetic-data/")
async def generate_synthetic_data(request: DataGenerationRequest):
    # Generate the prompt
    final_prompt = generate_prompt(
        request.num_records,
        request.data_format,
        request.headers,
        request.instructions
    )
    
    # Generate data using the model
    result = generate_llm_response(final_prompt)
    
    # Return the result
    return {"generated_data": result.content}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
