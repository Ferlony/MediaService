from pydantic import BaseModel


class ParserModel(BaseModel):
    url: str
    parser_type: int
    action: int


class UserSchema(BaseModel):
    username: str
    password: str


class SyncSchema(BaseModel):
    sync_data: list
    # {
    #   sync_data:
    #   [
    #       {"key_data1": {"key1": "value1", "key2": "value2"}},
    #       {"key_data2": {"key1": "value1", "key2": "value2"}}
    #   ]
    # }
