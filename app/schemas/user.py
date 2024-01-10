from pydantic import BaseModel

class UserBase(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str
    recipes: list | None = None

class UserIn(UserBase):
    password: str

