from transformers import AutoProcessor, Qwen2VLForConditionalGeneration
from PIL import Image
import easyocr
import streamlit as st
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-2B-Instruct",device_map=device)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")


def wrap_text(output_text):
    output_text = output_text[0]
    output_text = output_text.split("\n")
    output_text = "\n ".join(output_text)

    return output_text

def Image_text(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    image_text = ""
    for detection in result:
        image_text += detection[1]

    return image_text

def get_response(image, user_query, image_text):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": f"""You are an AI system tasked with generating detailed test cases for app functionalities. Based on the provided screenshots, its texts and any optional text, your goal is to produce a step-by-step guide describing everything which is mentioned below for testing the features of the app, including:
       image_text = {image_text}
       optional_text = {user_query}

  You have to Keep in mind the following definations and based on that you have to answer

  Feature Description: Briefly describe what the feature being tested does.
  Pre-conditions: Outline any setup or prerequisites required before testing the feature.
  Testing Steps: Provide clear, numbered steps that a tester should follow. describe each strps very breifly for tester to understand easily.
  Expected Results: Specify the expected outcome after each step if the feature is functioning correctly."""},
            ],
        },
                ]
    text_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=[text_prompt], images=[image], padding=True, return_tensors="pt")
    inputs = inputs.to(device)

    output_ids = model.generate(**inputs, max_new_tokens=1024)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
    output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)

    return wrap_text(output_text)


##initialize our streamlit app

st.set_page_config(page_title="MultiModel LLM")

st.header("ScreenShot Informations Provider")
input = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("explain the image to me 👇 ")

if submit:
  image_text = Image_text(image)
  response = get_response(image, input, image_text)
  st.subheader("Here The Response is")
  st.write(response)