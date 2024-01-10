from pydantic import BaseModel

#return Schema 
class CommentBase(BaseModel):
    id: int | None = None
    recipe_info: dict | None = None
    user_info: dict | None = None
    comment: str

# Create Schema
class CommentIn(CommentBase):
    id: int | None = None
    recipe_id: int 
    user_id: int 
    content: str
    

