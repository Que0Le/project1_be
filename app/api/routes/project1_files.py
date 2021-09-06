from typing import Optional
from typing import List

from fastapi import FastAPI, File, UploadFile, Form
from fastapi import APIRouter, Body, Depends
from starlette import status

from app.api.dependencies.database import get_repository
# from app.db.repositories.comments import CommentsRepository
# from app.db.repositories.words import WordsRepository
from app.db.repositories.project1_words import Project1WordsRepository
# from app.models.domain.articles import Article
# from app.models.domain.comments import Comment
# from app.models.domain.users import User
from app.models.domain.words import Word
# from app.models.schemas.comments import (
#     CommentInCreate,
#     CommentInResponse,
#     ListOfCommentsInResponse,
# )
from app.models.schemas.words import (
    WordInUpdate,
    WordShort,
    WordShortOutCreate,
    ListOfWordOutWithIdDate,
    WordOutWithIdDate,
    WordShortOutUpdate
)
from app.services.image_helpers import process_bitmap_from_file

router = APIRouter()

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

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=WordShortOutCreate,
    name="project1_files:create-new-file",
)
async def create_new_file(
    words_repo: Project1WordsRepository = Depends(get_repository(Project1WordsRepository)),
    file: UploadFile = File(...),
    word: str = Form(...),
    type: str = Form(...),
    fullword: str = Form(...),
    content: str = Form(...),
) -> WordShortOutCreate:
    contents = await file.read()
    process_bitmap_from_file(file=contents, output=fullword + ".bmp")
    word_row_created = await words_repo.create_new_dictword(
        word=word,
        type=type,
        fullword=fullword + ".bmp",
        content=content,
    )
    return word_row_created

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

