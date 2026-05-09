#from os import getenv
from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    urlDB: str
    model_config = SettingsConfigDict(env_file=".env")
    

setting = Setting()