import gradio as gr
import pandas as pd
import numpy as np
import random

df = pd.DataFrame({
    'height': np.random.randint(50, 70, 25),
    'weight': np.random.randint(120, 320, 25),
    'age': np.random.randint(18, 65, 25),
    'city': [random.choice(["New York", "Los Angeles", "Chicago"]) for _ in range(25)]
})

with gr.Blocks() as demo:
    with gr.Row():
        city = gr.Dropdown(["all", "New York", "Los Angeles", "Chicago"], value="all")
        max_age = gr.Slider(18, 65, value=65)

    def filtered_df(city, age):
        _df = df if city == "all" else df[df["city"] == city]
        _df = _df[_df["age"] < age]
        return _df

    gr.ScatterPlot(filtered_df, inputs=[city, max_age], x="weight", y="height", title="Weight x Height")
    gr.LinePlot(filtered_df, inputs=[city, max_age], x="age", y="height", title="Age x Height")


demo.launch()