import argparse
from checkbadword import foo, addtojson, st


def showdata_col1():
    sensi_word = st.Textbox(label="từ nhạy cảm cần thêm vào danh sách")
    sw = st.Textbox(label="biến thể tự phát hiện")
    sensi_word.change(
        lambda x: '-'.join([c for c in tuple(x) if c not in (' ', ',', '.', )]),
        sensi_word,
        sw,
    )
    sw_ = st.Textbox(label="biến thể tự phát hiện")
    sensi_word.change(
        lambda x: '.'.join([c for c in tuple(x) if c not in (' ', ',', '.', )]),
        sensi_word,
        sw_,
    )
    s_w_ = st.Textbox(label="biến thể tự phát hiện")
    sensi_word.change(
        lambda x: '_'.join([c for c in tuple(x) if c not in (' ', ',', '.', )]),
        sensi_word,
        s_w_,
    )
    sw__ = st.Textbox(label="biến thể chỉ định")
    sw___ = st.Textbox(label="biến thể chỉ định")
    sw____ = st.Textbox(label="biến thể chỉ định")
    return sensi_word, sw, sw_, s_w_, sw__, sw___, sw____

def showdata_col2():
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
        with st.Row():
            with st.Column():
                sens_w = showdata_col1()
                jso = st.Textbox(interactive=False)
                tojson = st.Button(value="Thêm vào danh sách loại trừ")
                tojson.click(addtojson, sens_w, jso)
            with st.Column():
                input = showdata_col2()
                files = st.Textbox(interactive=False)
                show = st.Button(value="Kiểm tra nội dung nhạy cảm")
                show.click(foo, input, files)

    demo.launch(server_port=server_port, server_name=server_name)
