"""
bot_setup.py — запускается ОДИН РАЗ для настройки бота.
После этого бот не нужен: Mini App работает полностью самостоятельно.

Установка: pip install requests
Запуск:    python bot_setup.py
"""

import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"       # из @BotFather
MINI_APP_URL = "https://YOUR_USERNAME.github.io/tg-tasks/"  # GitHub Pages URL

BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"


def set_menu_button():
    """Кнопка 'Tasks' откроет Mini App прямо в Telegram."""
    r = requests.post(f"{BASE}/setChatMenuButton", json={
        "menu_button": {
            "type": "web_app",
            "text": "Tasks",
            "web_app": {"url": MINI_APP_URL}
        }
    })
    print("Menu button:", r.json())


def set_commands():
    r = requests.post(f"{BASE}/setMyCommands", json={
        "commands": [{"command": "start", "description": "Open task tracker"}]
    })
    print("Commands:", r.json())


def get_my_id():
    """Отправь боту /start и запусти это — покажет твой chat_id."""
    r = requests.get(f"{BASE}/getUpdates")
    updates = r.json().get("result", [])
    if updates:
        msg = updates[-1].get("message", {})
        print("Your chat_id:", msg.get("chat", {}).get("id"))
        print("Username:", msg.get("chat", {}).get("username"))
    else:
        print("No updates. Send /start to the bot first, then re-run.")


if __name__ == "__main__":
    print("=== Telegram Task Tracker — One-time Setup ===\n")
    set_menu_button()
    set_commands()
    print("\nNow send /start to your bot, then run get_my_id():")
    get_my_id()
    print("\nDone. Bot setup complete. You won't need to run it again.")
