from project.main_agent import run_agent
import gradio as gr

def process_input(text):
    return run_agent(text)

iface = gr.Interface(fn=process_input, inputs="text", outputs="text")
iface.launch()
