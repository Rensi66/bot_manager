from pydantic import BaseModel, Field, ConfigDict


class CreateUser(BaseModel):
    user_name: str = Field(min_length=4)
    user_password: str = Field(min_length=8)

    model_config = ConfigDict(from_attributes=True)