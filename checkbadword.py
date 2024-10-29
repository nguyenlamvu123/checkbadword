import gradio as st
import json

from coordinate_constant import check_sensitive_content, chat_with_sensitive_check, readfile, load_sensitive_words, \
    swjson


def addtojson(*args):
    args_ = tuple(a for a in args if a)
    assert len(args_) > 3
    jso: dict = {
        "word": args_[0],
        "variants": list(args_[1:])
    }
    sen_word: dict = readfile(file=swjson, mod="_r", jso=True)
    sen_word["sensitive_words"].append(jso)
    readfile(file=swjson, mod="w", cont=sen_word, jso=True)
    ret_: list = load_sensitive_words()
    return st.Textbox(value=json.dumps(ret_, indent=2, ensure_ascii=False), interactive=False)


def foo(text, django=False):
    if chat_with_sensitive_check(text):
        ret_ = "true"
    else:
        ret = check_sensitive_content(text)
        ret_ = "true" if ret.startswith("Có") else "false"
    if django:
        return ret_
    return st.Textbox(value=ret_, interactive=False)
