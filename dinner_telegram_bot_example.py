import requests
import json
import random
import os

# 設定Telegram Bot的API令牌
TOKEN = 'Your token'

# 設定Telegram Bot的基本API URL
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
dinner_options = ["鍋去啃", "麥當勞", "火鍋", "牛肉麵", "牛排店", "拉麵", "丼飯", "學餐"]
# 定義一個函數來處理收到的消息
def handle_message(update):
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    if text == '/start':
        send_message(chat_id, '歡迎使用我的Telegram機器人！')
    elif text == '/help':
        send_message(chat_id, '這是一個簡單的Telegram機器人示例。')
    elif text == '/dinner':
        dinner_choice = random.choice(dinner_options)
        send_message(chat_id, f'今天的晚餐是：{dinner_choice}')
    else:
        send_message(chat_id, '我不明白你在說什麼。')
# 定義一個函數來發送消息
def send_message(chat_id, text):
    url = BASE_URL + '/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    return response

# 主循環，不斷地檢查新消息
def main():
    offset = None
    while True:
        url = BASE_URL + '/getUpdates'
        params = {'offset': offset, 'timeout': 30}
        response = requests.get(url, params=params)
        updates = json.loads(response.text)

        for update in updates['result']:
            handle_message(update)
            offset = update['update_id'] + 1

if __name__ == '__main__':
    main()
