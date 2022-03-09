from sqlalchemy.orm.scoping import scoped_session


class BaseService:
    def __init__(self, session: scoped_session) -> object:
        self._db_session = session
