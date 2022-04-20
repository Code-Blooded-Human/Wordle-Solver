#!/usr/bin/env python
# encoding: utf-8
import json
import random
import numpy as np
import pandas as pd
from tqdm import tqdm

from bot import Agent
from wordle import Wordle


from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


ROWS = 6
LETTERS = 5
GAMES = 10

w_bank = pd.read_csv('data/words.csv')
w_bank = w_bank[w_bank['words'].str.len()==LETTERS]
w_bank['words'] = w_bank['words'].str.upper() #Convert all words to uppercase


game = None
bot = None
i =0
guess = None

    # for i in range(ROWS):
    #     guess = bot.choose_action()
    #     print(f'\nSuggested Word = {guess}\n')
    #     u_inp = input('What were the colours returned [ex. ybggy]?\n')
    #     game.colours[i] = [s for s in str(u_inp).upper()]
    #     game.board[i] = [s for s in str(guess).upper()]
    #     game.g_count += 1
    #     for x, s in enumerate(game.colours[i]):
    #         if s == 'Y':
    #             if guess[x] in bot.y_letters:
    #                 bot.y_letters[guess[x]].append(x)
    #             else:
    #                 bot.y_letters[guess[x]] = [x]
    #         elif s == 'B':
    #             if guess[x] in bot.g_letters:
    #                 bot.g_letters.append(guess[x])
    #         elif s == 'G':
    #             bot.prediction[x] = guess[x]
@app.route('/start')
@cross_origin()
def start():
    global game
    global bot
    global i
    global guess


    game = Wordle(
        None,
        rows=ROWS,
        letters=LETTERS
    )
    bot = Agent(game)
    guess = bot.choose_action()
    return jsonify({'guess': guess})

@app.route('/play')
@cross_origin()
def play():
    global game
    global bot 
    global i
    global guess

    u_inp = request.args.get('out')
    print(u_inp)
    if u_inp == None:
        print("WRONG PARAMS PASSED")
        return jsonify({'msg': "WRONG PARAM PASSED"})

    game.colours[i] = [s for s in str(u_inp).upper()]
    game.board[i] = [s for s in str(guess).upper()]
    game.g_count += 1
    for x, s in enumerate(game.colours[i]):
        if s == 'Y':
            if guess[x] in bot.y_letters:
                bot.y_letters[guess[x]].append(x)
            else:
                bot.y_letters[guess[x]] = [x]
        elif s == 'B':
            if guess[x] in bot.g_letters:
                bot.g_letters.append(guess[x])
        elif s == 'G':
            bot.prediction[x] = guess[x]

    guess = bot.choose_action()
    
    return jsonify({'guess': guess})


app.run()