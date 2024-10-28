from coordinate_constant import check_sensitive_content, chat_with_sensitive_check, sensitive_words
import gradio as st


def foo(text, django=False):
    chat_with_sensitive_check(text, sensitive_words)
    ret = check_sensitive_content(text)
    ret_ = "true" if ret.startswith("Có") else "false"
    if django:
        return ret_
    return st.Textbox(value=ret_, interactive=False)