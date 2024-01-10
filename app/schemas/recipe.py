from pydantic import BaseModel


class RecipeBase(BaseModel):
    id: int | None = None
    title: str
    user_info: dict | None = None
    description: str
    ingredients: str
    instructions: str
    cook_time: str
    difficulty: str
    image: str
    category: str
    comments: list | None = None
    likes: int | None = None