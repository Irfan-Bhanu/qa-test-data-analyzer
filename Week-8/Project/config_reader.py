#in this file  we read config.ini


import configparser
import os

config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, "config", "config.ini")

#print("Config path:", config_path)

config.read(config_path)

#print("Sections:", config.sections())
#print("Defaults:", config.defaults()) #read is a method inside Configparser class

def get_base_url():
    return config['DEFAULT']['base_url']
def get_browser():
    return config['DEFAULT']['browser']

#print("Config sections:", config.sections())
#print("Config defaults:", config.defaults())