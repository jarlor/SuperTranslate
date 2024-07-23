# -*- coding: UTF-8 -*-
"""
@Author : Jarlor Zhang
@Email  : jarlor@foxmail.com
@Date   : 07/03/2024 22:25
@Desc   : OpenAI API
"""
from os import environ

from openai import OpenAI

client = OpenAI()


def universal_translate_by_gpt(text: str, prompt: str, *args, **kwargs) -> str:
    """
    GPT-based translation interface
    Args:
        text: text to be translation
        prompt: prompt word
    Returns:
        return a text what translated

    """
    return client.chat.completions.create(
        # 从环境变量中获取model 名称
        model=environ.get('OPENAI_MODEL_NAME', 'gpt-4o'),
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        # stop="4",
        temperature=0,
        max_tokens=4096
    ).choices[0].message.content
