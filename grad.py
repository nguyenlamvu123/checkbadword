import gradio as st
import argparse
from checkbadword import foo


def showdata_col1():
    descri1 = st.Textbox(label="nội dung cần kiểm tra")
    return descri1


outmp4list = list()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--listen',
        type=str,
        default='0.0.0.0',
        help='IP to listen on for connections to Gradio',
    )
    parser.add_argument(
        '--server_port',
        type=int,
        default='8501',
        help='Port to run the server listener on',
    )
    args = parser.parse_args()
    server_port = args.server_port
    server_name = args.listen

    with st.Blocks() as demo:
        input = showdata_col1()
        files = st.Textbox(interactive=False)  # value
        show = st.Button(value="Check bad word")
        show.click(foo, input, files)

    demo.launch(server_port=server_port, server_name=server_name)
