import os
import json
from PIL import Image
import google.generativeai as genai

# to get the file path directly
working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load( open(config_file_path))
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]
genai.configure( api_key = GOOGLE_API_KEY)


# loading the gen ai model

def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model

def gemini_pro_vision_response( prompt , image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt , image])
    result = response.text
    return result
# this s test code for gemini-pro-vision working or not
# image = Image.open("abc.jpg")
# prompt = " generate me short caption about the image"
# res = gemini_pro_vision_response( prompt , image )
# print(res )

def simple_QA(prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(prompt)
    result = response.text
    return result
