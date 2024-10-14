from langchain_ollama import ChatOllama
import streamlit as st

# Function to generate the prompt dynamically based on user input
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

# Streamlit user interface
st.title("Synthetic Data Generator")

# Get user inputs from Streamlit interface
num_records = st.number_input("Number of records required", min_value=1, step=1)
data_format = st.selectbox("Select data format", ["JSON", "CSV", "XML", "Excel", "Custom"])
headers = st.text_area("Enter data headers/keys (comma-separated)", "from, to, credit/debit, timestamp" )

# Optional specific instructions with a placeholder/example
instructions = st.text_area(
    "Any specific instructions or example data (optional)", 
)

# Trigger prompt generation and result display
if st.button("Generate Data"):
    # Convert headers from string to list
    headers_list = [header.strip() for header in headers.split(",")]

    # Generate the final prompt
    final_prompt = generate_prompt(num_records, data_format, headers_list, instructions)

    # Display the prompt to the user (for clarity)
    # st.write("Generated Prompt:")
    # st.write(final_prompt)

    # Call the model function to generate synthetic data
    result = generate_llm_response(final_prompt)

    # Display the generated result
    st.write("Generated Data:")
    st.write(result.content)
