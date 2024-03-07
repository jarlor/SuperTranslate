# -*- coding: UTF-8 -*-
"""
@Author : Jarlor Zhang
@Email  : jarlor@foxmail.com
@Date   : 07/03/2024 18:32
@Desc   : 调用GPT做英翻汉
"""

from openai import OpenAI
from flask import Flask, request, jsonify

ori_text = ''

client = OpenAI()
app = Flask(__name__)

prompt=open("prompt", "r").read()

@app.route('/translate_hcfy', methods=['POST'])
def hcfy_translate():
    """
    对接划词翻译的接口
    Returns:

    """
    input = dict(request.json)
    ori_text: str = input['text']

    translate_result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ori_text}
        ],
        # stop="4",
        temperature=0,
        max_tokens=4096
    ).choices[0].message
    result = {
        "text": ori_text,  # 翻译的文本
        "from": "中文(简体)",  # 翻译文本的源语种，这个语种会显示在翻译名称右侧并且可以切换
        "to": "英语",  # 翻译结果的语种
        "result": translate_result.content  # 翻译结果，可以有多条，一个段落对应一个翻译结果。可选。

    }
    return jsonify(result)

@app.route('/translate_zotero', methods=['POST'])
def zotero_translate():
    """
    对接zotero的接口
    Returns:

    """
    input = dict(request.json)
    ori_text: str = input['text']

    translate_result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ori_text}
        ],
        # stop="4",
        temperature=0,
        max_tokens=4096
    ).choices[0].message
    result = {
        "text": ori_text,  # 翻译的文本
        "from": "中文(简体)",  # 翻译文本的源语种，这个语种会显示在翻译名称右侧并且可以切换
        "to": "英语",  # 翻译结果的语种
        "data": translate_result.content  # 翻译结果，可以有多条，一个段落对应一个翻译结果。可选。

    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
