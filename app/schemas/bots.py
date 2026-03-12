from pydantic import BaseModel, ConfigDict

class AddBot(BaseModel):
    bot_token: str 

    model_config = ConfigDict(from_attributes=True)