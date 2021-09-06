from fastapi import APIRouter

from app.api.routes import authentication, comments, profiles, tags, users, words, project1_words, project1_server, project1_files
from app.api.routes.articles import api as articles

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
router.include_router(articles.router, tags=["articles"])
router.include_router(
    comments.router,
    tags=["comments"],
    prefix="/articles/{slug}/comments",
)
router.include_router(tags.router, tags=["tags"], prefix="/tags")
router.include_router(words.router, tags=["words"], prefix="/words")
router.include_router(project1_words.router, tags=["project1_words"], prefix="/project1_words")
router.include_router(project1_server.router, tags=["project1_server"], prefix="/project1_server")
router.include_router(project1_files.router, tags=["project1_files"], prefix="/project1_files")
