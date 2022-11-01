# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:22:38 2020

@author: 23820
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# 生成机器人，指定输入输出和训练器
chatbot = ChatBot(
    'CrossinBot',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
# 以中文语料进行训练
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.chinese')
print('你好，请问需要什么帮助？')
# 循环问答
while True:
    try:
        bot_input = chatbot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        # CTRL-C/CTRL-D 中断退出
        break
