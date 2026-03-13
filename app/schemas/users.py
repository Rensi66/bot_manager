from pydantic import BaseModel, Field, ConfigDict


class CreateUser(BaseModel):
    user_name: str = Field(min_length=4)
    user_password: str = Field(min_length=8)

    model_config = ConfigDict(from_attributes=True)


class UserOut(BaseModel):
    user_id: int
    user_name: str

    model_config = ConfigDict(from_attributes=True)