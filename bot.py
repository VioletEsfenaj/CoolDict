from telethon import TelegramClient, events
from config import * 
from PyMultiDictionary import MultiDictionary, DICT_WORDNET, DICT_EDUCALINGO
import json

bot = TelegramClient('session', API_ID, API_HASH)
dictionary = MultiDictionary()


async def start(event):
    await event.respond(f"Cool you know how to start a bot?, now send the word.")
    
    raise events.StopPropagation

async def word_handler(event, _dictionary=DICT_EDUCALINGO):
    try:
        if len(event.raw_text.split(' ')) > 1:
            await sentence_handler(event)
            return 
        
        word = event.raw_text
        result = dictionary.meaning('en', word.lower(), dictionary=_dictionary)
        logging.info(json.dumps(result))
        
        if len(result) < 2 or not result[0]:
            raise ValueError
        
        tldr = f"__TL;DR:__ {result[1].replace(f'The first definition of {word.lower()} in the dictionary is ', '').replace(f'{word.lower()} in the dictionary is', '')}"
        
        meaning = None
        if len(result) > 2:
            meaning = '\n\n'.join(result[2:])
            meaning = '\n\n▪️'.join(meaning.split('\u25aa'))
            
        text = f"**{word.lower().capitalize()}**\n\n{tldr}\n\n\n{meaning}" if meaning else f"**{word.lower().capitalize()}**\n\n{tldr}"
        await event.respond(text)
    except Exception as e:
        await event.respond(f"Dunno, usethefuckinggoogle.com")
        logging.error(e, exc_info=True)   
    finally:
        raise events.StopPropagation
    
async def sentence_handler(event):
    await event.respond(f"bruh, is that a word to you? read the fucking description:\n\n__No bullshit just send the word to get the meaning without having to open google__")
    
        
async def main(): 
    bot.add_event_handler(start, events.NewMessage(pattern=r'^/start$'))
    bot.add_event_handler(word_handler, events.NewMessage(pattern=r'\w+'))
    
        
bot.start(bot_token=BOT_TOKEN)
bot.loop.create_task(main())
bot.loop.run_forever()