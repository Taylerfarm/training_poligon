import pyrogram
from pyrogram import Client
import time
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
api_id = cfg.get("tg_keys", "api_id")
api_hash = cfg.get("tg_keys", "api_hash")
client = Client("Garage", api_id=api_id, api_hash=api_hash)
group_info = client.get_chat("-4025370246")
input()
print(type(group_info))


if __name__ == '__main__':
    client.run()
