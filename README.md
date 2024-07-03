# Generative AI using LLM and Stable Diffusion

## Overview
This repository contains the source code for a project aimed at leveraging Generative AI techniques to generate text and images based on user input. It utilizes Large Language Models (LLMs) and Stable Diffusion for text generation and image synthesis, respectively. Additionally, the project includes a text summarizer capable of correcting grammatical mistakes in input text.

## Features
- **Generative AI**: Users can input queries or prompts, and the system generates creative responses using a Large Language Model (LLM).
- **Text Summarizer**: Utilizes a state-of-the-art text summarization model to condense input text while maintaining its essential meaning.
- **Text to Image**: Transforms text input into corresponding images using Stable Diffusion, a powerful image synthesis model.

## Installation
1. Clone this repository to your local machine:
```commandline
git clone https://github.com/Karthi-J7/Generative-AI.git
```
2. Install the required dependencies:
```commandline
pip install -r requirements.txt
```

## Usage
### Running the Application
1. Navigate to the project directory:
```commandline
cd Generative-AI
```
2. Run the Streamlit application:
```commandline
streamlit run app.py
```
3. Access the application via your web browser at `http://localhost:8501`.

### Choosing Tasks
- Upon accessing the application, users are presented with a sidebar to choose from the following tasks:
    - Generative AI: Enter a query or prompt, and the system generates creative responses based on the input.
    - Text Summarizer: Input text that needs summarization, and the system provides a condensed version.
    - Text to Image: Enter text, and the system generates corresponding images.

## Configuration
### Model Paths
- Ensure that the paths to the models are correctly configured in the app.py file:
    - `path`: Path to the LLM model.
    - `text_model`: Identifier for the text summarization model.
    - `img_model`: Identifier for the image synthesis model.
## Device Configuration
Adjust the device variable in the **app.py** file based on your hardware configuration (**'cpu'** for CPU-only or **'cuda'** for GPU-accelerated).

## Example
Sample working example for [User workflow](https://drive.google.com/file/d/1hvfE45xeaotDQ0uKjQjr9sIMNMo25WbF/view?usp=sharing))

## Contributing
Contributions are welcome! If you have any ideas for improvements, open an issue or submit a pull request.

## License
This project is licensed under the **MIT License.**
