import requests
from .models import TeleSetting


def sendTelegram(tg_name, tg_phone, tg_address, tg_executor):
    settings = TeleSetting.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.find('{', a+1)
    d = text.find('}', b+1)
    e = text.find('{', c+1)
    f = text.find('}', d+1)
    g = text.find('{', e+1)

    part_1 = text[0:a]
    part_2 = text[b+1:c]
    part_3 = text[d+1:e]
    part_4 = text[f+1:g]

    text_slise = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_address + part_4 + tg_executor

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise
         })
