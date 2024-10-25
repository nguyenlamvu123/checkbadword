from coordinate_constant import check_sensitive_content
import gradio as st


def foo(text):
    ret = check_sensitive_content(text)
    ret_ = "Có" if ret.startswith("Có") else "Không"
    ret_ += f'\n{ret}'
    return st.Textbox(value=ret_, interactive=False)