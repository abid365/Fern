from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get('/users')
async def get_all_users():
    return [
        {"username": 'Jango', "age": 90},
        {"username": 'rambo', "age": 50}
    ]


@router.get('/users/me')
async def get_my_info():
    return {
        "name": 'Ak47',
        "city": "Russia",
        "gun": True,

    }


@router.get('/users/{username}')
async def get_user(username: str, query: str):
    return {
        "username": username,
        "query": query
    }
