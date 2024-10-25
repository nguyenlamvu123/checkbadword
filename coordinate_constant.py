from openai import OpenAI
import json, os


def readfile(file="uid.txt", mod="r", cont=None, jso: bool = False):
    if not mod in ("w", "a", ):
        assert os.path.isfile(file), str(file)
    if mod == "r":
        with open(file, encoding="utf-8") as file:
            lines: list = file.readlines()
        return lines
    elif mod == "_r":
        with open(file, encoding="utf-8") as file:
            contents = file.read() if not jso else json.load(file)
        return contents
    elif mod == "rb":
        with open(file, mod) as file:
            contents = file.read()
        return contents
    elif mod in ("w", "a", ):
        with open(file, mod, encoding="utf-8") as fil_e:
            if not jso:
                fil_e.write(cont)
            else:
                json.dump(cont, fil_e, indent=2, ensure_ascii=False)


# Hàm kiểm tra từ nhạy cảm thông qua ChatGPT API
def check_sensitive_content(text):
    message_content = (
            f"Kiểm tra đoạn văn sau để xác định xem có chứa nội dung nhạy cảm không:\n\n'{text}'\n\n"
            "Các nội dung nhạy cảm cần kiểm tra bao gồm:\n"
            "- **Chính trị**: các từ liên quan đến bầu cử, chính quyền, phản động hoặc cách mạng.\n"
            "- **Bạo lực**: từ liên quan đến hành vi bạo lực, giết người, đánh đập, hoặc khủng bố.\n"
            "- **Khiêu dâm**: nội dung tình dục, khiêu dâm, đồi trụy hoặc nhạy cảm.\n\n"
            "Nếu đoạn văn có chứa bất kỳ loại nội dung nào trên, hãy trả lời 'Có' kèm theo loại nội dung. "
            "Nếu không, hãy trả lời 'Không'."
        )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message_content}
        ],
        max_tokens=5,
        temperature=0
    )
    result = response.choices[0].message.content.strip()
    return result


apikey:str = readfile('apikey.txt', '_r')
client = OpenAI(
    # This is the default and can be omitted
    api_key=apikey,
)
