import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please check your .env file.")

print(f"API Key Loaded: {api_key}")  # Print the key for debugging purposes


import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=api_key)

##Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content([input, image[0], prompt])
        return response.text
    except Exception as e:
        if isinstance(e, genai.Error):
            if e.code == "RESOURCE_EXHAUSTED":
                return "Error: API rate limit exceeded. Please try again later."
            elif e.code == "INVALID_ARGUMENT":
                return "Error: Invalid input. Please check your prompt and image."
            else:
                return f"Error: {e.message}"
        else:
            return f"An unexpected error occurred: {e}"

##Function to read the Image and set the image format for Gemini Pro model Input
def input_image_setup(uploaded_file):
    #check if a file has been uploaded
    if uploaded_file is not None:
        #Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  #Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded!")

##Writing a prompt for gemini model
input_prompt = """As an expert nutritionist you need to analyze the food items presented in the image provided.
Please calculate the total caloric content and offer a detailed breakdown of each food item with its corresponding calorie count in the following format:
1. Item1 - number of calories
2. Item2 - number of calories
...
...
Additionally, provide an assessment of the meal's overall healthiness. Finally, include a percentage-based breakdown of the meal's nutritional components, including carbohydrates, fats, fibers, sugars, and other essential dietary elements necessary for a balanced diet.
After analyzing a meal, you could rate it on to 5 ⭐️ Star for healthiness.
"""

##Initialize our streamlit app
st.set_page_config(page_title="AI Nutritionist App")

st.header("AI Nutritionist App")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

##If submit button is clicked
if submit:
    if uploaded_file is not None:  # Check if a file is uploaded
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please upload an image before submitting.")


##To Launching the application run the following command: streamlit run app.py