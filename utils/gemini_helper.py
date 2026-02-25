import vertexai
from vertexai.generative_models import GenerativeModel, Part
from config import PROJECT_ID, LOCATION

def analyze_image(image_bytes, prompt_text):

    vertexai.init(project=PROJECT_ID, location=LOCATION)

    model = GenerativeModel("gemini-1.5-pro")

    image_part = Part.from_data(image_bytes, mime_type="image/jpeg")

    response = model.generate_content(
        [prompt_text, image_part],
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 2048
        }
    )

    return response.text
