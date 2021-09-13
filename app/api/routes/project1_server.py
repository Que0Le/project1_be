from app import main
from typing import Optional

from fastapi import APIRouter, Body, Depends
from starlette import status

from app.api.dependencies.database import get_repository
from app.db.repositories.project1_words import Project1WordsRepository
from app.models.domain.words import Word
from app.services.image_helpers import (
    create_bitmap_from_word,
    create_bitmap_from_calendar
)
from app.services.calendar_helpers import (
    get_calendar_for_this_week
)
from fastapi.responses import StreamingResponse 

from app.core.config import settings
import datetime as dt

from app.models.schemas.words import (
    WordOutWithIdDate,
    WordShortOutUpdate
)
from app.resources import strings 
import io
import datetime as dt

router = APIRouter()

def iterfile(path: str):  
    with open(path, mode="rb") as file_like:  
        yield from file_like  

@router.get(
    "/next",
    response_model=WordOutWithIdDate,
    name="project1_server:get-next-word",
)
async def project1_get_next(
    words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
) -> WordOutWithIdDate:
    if settings.o365_account:
        all_events = get_calendar_for_this_week(settings.o365_account.schedule())
        return StreamingResponse(
            io.BytesIO(create_bitmap_from_calendar(all_events, output="__buffer")), 
            media_type="image/jpeg"
        )
    else:
        dictword = await words_repo.get_1_random_dictword()
        return dictword

@router.get(
    "/next_bitmap",
    name="project1_server:get-next-bitmap",
)
async def project1_get_next(
    words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
) -> io.BytesIO:
    #TODO: next_engine will decide which content will be served at this moment
    if (dt.datetime.now().minute % 2 == 0) and settings.o365_account:
        all_events = get_calendar_for_this_week(settings.o365_account.schedule())
        return StreamingResponse(
            io.BytesIO(create_bitmap_from_calendar(all_events, output="__buffer")), 
            media_type="image/jpeg"
        )
    else:
        dictword = await words_repo.get_1_random_dictword()
        if dictword.type==strings.TYPE_STATIC_FILE:
            path = strings.PATH_STATIC_FOLDER + dictword.fullword
            return StreamingResponse(iterfile(path), media_type="image/jpeg")
        else:
            return StreamingResponse(
                io.BytesIO(create_bitmap_from_word(dictword, output="__buffer")), 
                media_type="image/jpeg"
            )

# @router.get(
#     "/next_bitmap_from_file",
#     name="project1_server:get-next-bitmap-from-file",
# )
# def project1_get_next_from_file(
# ) -> WordOutWithIdDate:
#     return StreamingResponse(
#         iterfile(strings.PATH_STATIC_FOLDER + "ausserhalb_1bit.bmp"), 
#         media_type="image/jpeg"
#     )






# @router.get(
#     "/",
#     response_model=ListOfWordOutWithIdDate,
#     name="project1_words:get-words-by-path-query",
# )
# async def get_words_by_path_query(
#     word: str,
#     words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
# ) -> ListOfWordOutWithIdDate:
#     # test  = await words_repo.get_all_dictwords(word=word)
#     words = await words_repo.get_dictwords_by_word(word=word)
#     return ListOfWordOutWithIdDate(words=words)

# @router.get(
#     "/{word_id}",
#     response_model=WordOutWithIdDate,
#     name="project1_words:get-word-by-id-by-query",
# )
# async def get_word_by_id_path_query(
#     word_id: int,
#     words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
# ) -> WordOutWithIdDate:
#     print("here")
#     dictword = await words_repo.get_dictword_by_id(id=word_id)
#     return dictword

# @router.post(
#     "/",
#     status_code=status.HTTP_201_CREATED,
#     response_model=WordShortOutCreate,
#     name="project1_words:create-new-dictword",
# )
# async def create_new_word(
#     word_create: Word,
#     words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
#     # user: User = Depends(get_current_user_authorizer()),
# ) -> WordShortOutCreate:
#     word_row_created = await words_repo.create_new_dictword(
#         word=word_create.word,
#         type=word_create.type,
#         fullword=word_create.fullword,
#         content=word_create.content,
#     )
#     return word_row_created

# @router.put(
#     "/{word_id}",
#     status_code=status.HTTP_201_CREATED,
#     response_model=WordShortOutUpdate,
#     name="project1_words:update-existing-dictword-by-id",
# )
# async def update_dictword_by_id(
#     word_id: int,
#     word_update: Word,
#     words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
#     # user: User = Depends(get_current_user_authorizer()),
# ) -> WordOutWithIdDate:
#     word_row_updated = await words_repo.update_dictword_row_by_id(
#         id=word_id,
#         dictword=word_update
#     )
#     return word_row_updated

# @router.delete(
#     "/{word_id}",
#     status_code=status.HTTP_200_OK,
#     name="project1_words:delete-dictword-from-db",
# )
# async def delete_dictword_from_db(
#     word_id: int,
#     words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
# ) -> int:
#     r = await words_repo.delete_dictword(id=word_id)
#     return {"id": r}

