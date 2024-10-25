from coordinate_constant import check_sensitive_content
import gradio as st


def foo(text):
    ret = check_sensitive_content(text)
    return st.Textbox(value=ret, interactive=False)