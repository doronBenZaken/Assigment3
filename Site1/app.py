from fastapi import FastAPI
import gradio as gr

from demo_site import iface

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running', 200

app = gr.mount_gradio_app(app, iface, path='/')