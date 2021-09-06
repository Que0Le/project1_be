from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB
from app.models.domain.words import Word

from app.models.schemas.words import (
    WordInUpdate,
    WordShort,
    WordShortOutCreate,
    ListOfWordOutWithIdDate,
    WordOutWithIdDate
)
from typing import List

class WordsRepository(BaseRepository):

    async def get_all_dictwords(self, *, word: str) -> List[str]:
        dictword_rows = await queries.get_all_dictwords(self.connection)
        for row in dictword_rows:
            print(row)
        return [row for row in dictword_rows]

    async def get_dictwords_by_word(self, *, word: str) -> List[WordOutWithIdDate]:
        word_rows = await queries.get_dictwords_by_word(
            self.connection,
            word=word,
        )
        if word_rows:
            l = [
                (WordOutWithIdDate (
                    id=word_row["id"],
                    word=word_row["word"],
                    type=word_row["type"],
                    fullword=word_row["fullword"],
                    content=word_row["content"],
                    created_at=word_row["created_at"],
                    updated_at=word_row["updated_at"],
                ))
                for word_row in word_rows
            ]
            # print(l)
            return l

        raise EntityDoesNotExist(
            "Word {0} does not exist".format(word),
        )

    async def get_dictword_by_id(self, *, id: int) -> WordOutWithIdDate:
        word_row = await queries.get_dictword_by_id(
            self.connection,
            id=id,
        )
        if word_row:
            return WordOutWithIdDate(**word_row)

        raise EntityDoesNotExist(
            "Word with id={0} does not exist".format(id),
        )

    async def create_new_dictword(
        self,
        *,
        word: str,
        type: str,
        fullword: str,
        content: str,
    ) -> WordShortOutCreate:
        w = Word(word=word, type=type, fullword=fullword, content=content)
        async with self.connection.transaction():
            word_row = await queries.create_new_dictword(
                self.connection,
                word=w.word,
                type=w.type,
                fullword=w.fullword,
                content=w.content,
            )
        return WordShortOutCreate(**word_row)


    async def update_dictword_row_by_id(  # noqa: WPS211
        self,
        *,
        id: int,
        dictword: Word
    ) -> WordOutWithIdDate:
        word_in_db = await self.get_dictword_by_id(id=id)

        dictword.word = dictword.word or word_in_db.word
        dictword.type = dictword.type or word_in_db.type
        dictword.fullword = dictword.fullword or word_in_db.fullword
        dictword.content = dictword.content or word_in_db.content

        async with self.connection.transaction():
            word_updated = await queries.update_dictword_row_by_id(
                self.connection,
                id=id,
                new_word=dictword.word,
                new_type=dictword.type,
                new_fullword=dictword.fullword,
                new_content=dictword.content,
            )

        return word_updated

    async def delete_dictword(self, *, id: int) -> str:
        r = await queries.delete_dictword_by_id(
            self.connection,
            id=id,
        )
        if r:
            if int(r["id"]):
                return int(r["id"])
        raise EntityDoesNotExist(
            "Word with id={0} does not exist".format(id),
        )
