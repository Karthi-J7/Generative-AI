# import the necessary modules

import streamlit as st
from langchain.llms import GPT4All
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, T5ForConditionalGeneration
from diffusers import StableDiffusionPipeline


# Defining Model for LLM
path = r'paste your gpt4all path'
model = path + r'\gpt4all-falcon-q4_0.gguf'

# Creating LLM using falcon model
llm = GPT4All(model=model, verbose=True)

# Defining PromptTemplate for our llm model
prompt = PromptTemplate(input_variables=['question'],
                        template='''
                        Question : {question},
                        Answer: "Let's think as a creative agent'''
                        )

# Creating a LLM chain with the llm and prompt template(designed)
chain = LLMChain(prompt=prompt, llm=llm)

# Defining Model for Text Summerizer
text_model = 'grammarly/coedit-large'
tokenizer = AutoTokenizer.from_pretrained(text_model)
summerize = T5ForConditionalGeneration.from_pretrained(text_model)

# Defining text to image model
# if you have a dedicated graphics card (GPU) use device as 'CUDA'
# if you have only CPU use device as 'CPU'

device = 'cpu'
img_model = 'Compvis/stable-diffusion-v1-4'

pipe = StableDiffusionPipeline.from_pretrained(model)
pipe.to(device)

# Creating Streamlit Sidebar
with st.sidebar:

    # Declaring Streamlit Sidebar for task
    st.info('Choose Your Appropriate Task')
    option = st.radio('Hello', ['Text to Image', 'Text Summarizer', 'Generative AI'])
    st.write(option)

# Choosing Model based on user options
if option == 'Generative AI':
    prompt = st.text_area('Enter the Queries....')
    response = chain.run(prompt)
    st.write(response)

if option == 'Text Summarizer':
    prompt = st.text_area('Enter the Queries....')

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    response = summerize.generate(input_ids, max_length=256)
    response = tokenizer.decode(response, skip_special_tokens=True)

if option == 'Text to Image':
    prompt = st.text_area('Enter the Queries....')
    st.image(pipe(prompt).images[0])

