import gradio as gr
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

# Initialize Ollama
llm = Ollama(base_url='http://localhost:11434', model="mistral")

ai_prompt = "Give me 5 ideas for exciting WEB projects with AI in Gradio."

def generate_response():
    """Generate a response using Ollama"""
    prompt = ai_prompt
    response = llm(prompt)
    return response

# Create Gradio interface
iface = gr.Interface(
    fn=generate_response,
    inputs= None,
    outputs="text",
    title="Ollama AI Assistant",
    description=ai_prompt
)

# Launch the Gradio app
iface.launch()