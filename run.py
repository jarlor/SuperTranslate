# -*- coding: UTF-8 -*-
"""
@Author : Jarlor Zhang
@Email  : jarlor@foxmail.com
@Date   : 07/03/2024 18:32
@Desc   : 调用GPT做英翻汉
"""

from flask import Flask, request, jsonify
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

import api

with open('prompt', 'r') as f:
    prompt = f.read()


@app.route('/translate_hcfy', methods=['POST'])
def hcfy_translate():
    """
    interface to HCFY \n
    Link: https://hcfy.app/docs/services/custom-api/ \n
    """
    input = dict(request.json)
    text: str = input['text']

    translate_result = api.universal_translate_by_gpt(text, prompt=prompt)
    result = {
        "text": text,
        "from": "中文(简体)",
        "to": "英语",
        "result": [translate_result]

    }
    return jsonify(result)


@app.route('/translate_zotero', methods=['POST'])
def zotero_translate():
    """
    interface to zotero \n
    input required field and format: text:str,source_lang:str,target_lang:str
    output required field : data:str

    """
    input = dict(request.json)
    text: str = input['text']
    translate_result = api.universal_translate_by_gpt(text, prompt=prompt)
    result = {
        "data": translate_result
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
