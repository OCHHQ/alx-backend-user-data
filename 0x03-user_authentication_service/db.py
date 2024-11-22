#!/usr/bin/env python3
"""DB module for user management"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
import bcrypt


class DB:
    """DB class for user database operations"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database

        Args:main.p
            email (str): User's email
            hashed_password (str): Hashed password for the user

        Returns:
            User: The newly created user object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.

        Args:
            kwargs: Arbitrary keyword arguments to filter users.

        Returns:
            User: The first user matching the filter.

        Raises:
            NoResultFound: If no user matches the filter.
            InvalidRequestError: If query arguments are invalid.
        """
        if not kwargs:
            raise InvalidRequestError("No query arguments provided")

        query = self._session.query(User).filter_by(**kwargs)
        user = query.first()

        if user is None:
            raise NoResultFound("No user found with the given filter")

        return user
