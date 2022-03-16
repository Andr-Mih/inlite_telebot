import telebot
from config import token
from telebot import types
import re, wikipedia

wikipedia.set_lang('ru')

bot = telebot.TeleBot(token)

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:600]
        
        return wikitext

    except Exception as e:
        return 'В эпциклопедии нет такой записи'

@bot.inline_handler(func = lambda query: len(query.query)>0)
def qury_text(query):
    
    try:
        text = query.query
        m_res = getwiki(text)
        r_exp = types.InlineQueryResultArticle(id = '1', title='text', description=f'{m_res}', input_message_content=types.InputTextMessageContent(message_text=f'{m_res}'))
        bot.answer_inline_query(query.id, [r_exp,])
        
    except AttributeError as e:
        return 'Enter two digits'
    


bot.polling(none_stop = True, interval =0)
