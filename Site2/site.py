import gradio as gr
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

# Initialize Ollama
llm = Ollama(base_url='http://127.0.0.1:11434', model="mistral")

def generate_recipe(dietary_preferences, available_ingredients, skill_level):
    """Generate personalized recipe suggestions using Ollama"""
    prompt = f"""As an AI-powered recipe finder, suggest a personalized recipe based on the following information:
    Dietary Preferences: {dietary_preferences}
    Available Ingredients: {available_ingredients}
    Cooking Skill Level: {skill_level}

    Please provide a recipe name, ingredients list, and step-by-step instructions."""

    response = llm(prompt)
    return response

# Create Gradio interface
iface = gr.Interface(
    fn=generate_recipe,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter dietary preferences (e.g., vegetarian, gluten-free, low-carb)", label="Dietary Preferences"),
        gr.Textbox(lines=3, placeholder="List available ingredients, separated by commas", label="Available Ingredients"),
        gr.Radio(["Beginner", "Intermediate", "Advanced"], label="Cooking Skill Level")
    ],
    outputs=gr.Textbox(label="Personalized Recipe Suggestion"),
    title="AI-Powered Personalized Recipe Finder",
    description="Get personalized recipe suggestions based on your dietary preferences, available ingredients, and cooking skill level."
)

# Launch the Gradio app
iface.launch()
