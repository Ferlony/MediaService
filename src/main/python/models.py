from pydantic import BaseModel


class ParserModel(BaseModel):
    url: str
    parser_type: int
    action: int


class UserSchema(BaseModel):
    username: str
    password: str
