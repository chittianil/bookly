# from pydantic_settings import BaseSettings, SettingsConfigDict



# class Settings(BaseSettings):
#     DATABASE_URL: str 

#     model_config = SettingsConfigDict(
#         env_file=".env", 
#         extra="ignore"
#     )

# # add this line    
# Config = Settings()
# print(Config.DATABASE_URL)




import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Ensure .env is loaded first
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str ="postgresql+asyncpg://neondb_owner:npg_aowrcYPmN9E7@ep-shy-thunder-a8ifgqle-pooler.eastus2.azure.neon.tech/neondb"

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )

# Provide a default or raise an error if not found
Config = Settings(_env_file='.env')