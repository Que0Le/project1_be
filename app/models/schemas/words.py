from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from app.models.domain.rwmodel import RWModel
from app.models.domain.words import Word
# from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema
from typing import List

# class UserInLogin(RWSchema):
#     email: EmailStr
#     password: str


class WordShort(RWModel):
    word: str
    type: str

class WordShortOutCreate(WordShort):
    id: int
    created_at: datetime

class WordShortOutUpdate(WordShort):
    id: int
    updated_at: datetime

# class ListOfWordsInResponse(RWSchema):
#     words: List[WordOutWithIdDate]

class WordInUpdate(BaseModel):
    word: Optional[str] = None
    type: Optional[str] = None
    fullword: Optional[str] = None
    content: Optional[str] = None
    updated_at: datetime

class WordOutWithIdDate(RWSchema):
    id: int
    word: str
    type: Optional[str] = ""
    fullword: Optional[str] = ""
    content: str
    created_at: datetime
    updated_at: datetime

class ListOfWordOutWithIdDate(RWSchema):
    words: List[WordOutWithIdDate]