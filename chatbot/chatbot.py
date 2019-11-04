#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:17:19 2019

@author: evanildodejesus
"""
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot import filters

chatbot = ChatBot(
    "Bdata",
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    filters=[filters.get_recent_repeated_responses],
    response_selection_method=get_most_frequent_response
)

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    '/home/evanildodejesus/PycharmProjects/gestaoclinicas/chatbot/adm.yml',
    'chatterbot.corpus.portuguese.conversations'
)

print('Qual a sua maior dor...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break