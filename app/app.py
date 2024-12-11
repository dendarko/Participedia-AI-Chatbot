import streamlit as st
import requests

# Define the backend API URL
API_URL = "http://127.0.0.1:5001/chat"

# Title and welcome message
st.title("Participedia AI Chatbot")
st.write(
    """
    Welcome to the Participedia AI Chatbot! This tool helps you explore and understand participatory democracy, 
    including cases, methods, and organizations. Ask questions like:
    - **What is participatory budgeting?**
    - **How do citizens deliberate?**
    - **What organizations support participatory democracy?**
    """
)

# Input field for the query
query = st.text_input("Type your question below:")

# Submit button logic
if st.button("Ask"):
    if not query.strip():  # Check for empty input
        st.error("Please enter a question.")
    else:
        with st.spinner("Processing your question..."):
            try:
                # Send the query to the backend API
                response = requests.post(API_URL, json={"query": query})
                response.raise_for_status()  # Raise exception for HTTP errors
                data = response.json()

                # Display the response
st.subheader("Response")
response_text = data.get("response", "No response generated.")
st.write(response_text.capitalize())

# Display formatted examples
st.subheader("Relevant Examples")
examples = data.get("examples", [])
if examples:
    for ex in examples:
        st.markdown(f"**{ex['title'].capitalize()}**: {ex['description'].capitalize()}")
        st.markdown(f"[Learn More]({ex['url']})")
else:
    st.write("No relevant examples available.")

            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the backend: {e}")
            except ValueError:
                st.error("Invalid response format received from the backend.")
