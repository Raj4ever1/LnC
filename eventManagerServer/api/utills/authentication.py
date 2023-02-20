from .database import DatabaseQueryStringSelect, DatabaseQuery

def is_authenticated(request)->bool:
    valid_user = False
    db = DatabaseQuery()
    token = db.select(DatabaseQueryStringSelect.TOKEN_USING_USER, request.user)
    token = token[0]['key'] if len(token) == 1 else None
    if request.headers["Token"] == token:
        valid_user = True
    return valid_user