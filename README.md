# Qwen-MultiModel

## Overview
This application uses a multimodal large language model (LLM) to analyze screenshots and generate step-by-step, detailed test cases for app features. By uploading an image (such as an app screenshot) and providing optional text, you'll receive a concise testing guide describing the app’s functionalities, steps, and expected outcomes.

## Features
- Extracts text from uploaded images using OCR (Optical Character Recognition) through EasyOCR.  
- Processes user queries (optional text) and combines it with extracted image text to produce a detailed, AI-generated test procedure.  
- Generates a clear list of pre-conditions, testing steps, and expected results for your application’s feature testing.

## How It Works
1. Upload an image containing relevant content (e.g., a screenshot of your app).  
2. (Optional) Enter a text prompt describing any additional context or details you’d like included.  
3. Click the “explain the image to me” button to run your input through the model.  
4. View the AI-generated testing procedure, which outlines feature description, pre-conditions, testing steps, and expected outcomes.

## Requirements
- Python 3.7 or higher  
- PyTorch (with CUDA support if GPU acceleration is desired)  
- Transformers  
- Pillow (for image handling)  
- EasyOCR  
- Streamlit  

Make sure you have a working CUDA setup if you want to leverage GPU acceleration.

## Installation & Setup
1. Clone or download this repository to your local machine.  
2. Navigate to the folder in your terminal.  
3. Install the necessary packages (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   Replace “app.py” with the filename if you saved the script under a different name.

## Usage
1. Open the app in your web browser (a local URL will be provided in the terminal).  
2. Enter your prompt in the text box if you have additional instructions or context.  
3. Upload an image (PNG, JPG, or JPEG).  
4. Click “explain the image to me” to generate the test procedure.  
5. Review the output, which gives you a comprehensive breakdown of the feature, pre-conditions, test steps, and expected results for validation.

## What You Get
- A clear and concise explanation of what is displayed in the screenshot.  
- A ready-made, AI-generated testing procedure tailored to your specific app context and any optional instructions you provide.  
- A faster and more structured approach to documenting pre-conditions, steps, and expectations for feature testing.
