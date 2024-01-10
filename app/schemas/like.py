from pydantic import BaseModel 

class LikeBase(BaseModel):
    id: int | None = None
    recipe_id: int | None = None 
    user_id: int | None = None     

# class LikeOut(LikeBase):
#     count: int | None = None 

