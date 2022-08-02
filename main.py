from time import sleep, time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import time


apikey = "5318658259:AAH71kxJ2XeWiqd2tmNf44yR-vYLp3qT9ro"

bot = telebot.TeleBot(apikey)


@bot.message_handler(commands=["consultar_valores"])
def consultar_valores(mensagem):
    bot.send_message(mensagem.chat.id, text="""
===============================
Aviso de manutenção em 01/08/2022 
===============================
Estou estudando para botar botões elegantes no bot! :D
    
    """)


@bot.message_handler(commands=["fazer_pedido"])
def fazer_pedido(mensagem):
    bot.send_message(mensagem.chat.id, text="""
===============================
Aviso de manutenção em 01/08/2022 
===============================
Estou estudando para botar botões elegantes no bot! :D
    
    """)


@bot.message_handler(commands=["continuar"])
def continuar(mensagem):
    bot.send_message(mensagem.chat.id, text=""" 
    Vamos lá! O que você deseja?
===============================
    /fazer_pedido
    /consultar_valores
    /voltar
    """)


@bot.message_handler(commands=["finalizar"])
def finalizar(mensagem):
    bot.send_message(
        mensagem.chat.id, "Se precisar de mais alguma coisa me envie um 'oi' para voltamos a conversar!")


def verificacao(mensagem):
    return True


@bot.message_handler(func=verificacao)
def responder(mensagem):
    resposta = """ 
===============================
Olá! Eu sou Eli, sua assistente virtual.

Durante nossa conversa, vou precisar
que você me informe alguns dados pessoais que serão ultilizados para 
a realização do pedido.

Fique Tranquilo, as suas informações estarão seguras e não serão utilizadas 
para nenhum outro fim!!

Vamos nessa ?
===============================
    /continuar
    /finalizar
    """

    bot.send_message(mensagem.chat.id, resposta)


sleep(1)

bot.polling()
