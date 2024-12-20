#!/usr/bin/env python3
"""DB module for user management"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
import bcrypt


class DB:
    """DB class for user database operations"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        # Optional: Comment out these lines to retain data across runs
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

        Args:
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
        """Find a user by arbitrary keyword arguments."""
        if not kwargs:
            raise InvalidRequestError("No filter arguments provided")
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the given filter")
        except Exception as e:
            raise InvalidRequestError(f"Invalid arguments provided: {e}")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes in the database.

        Args:
            user_id (int): The ID of the user to update.
            kwargs: Arbitrary keyword arguments corresponding
            to user attributes.

        Raises:
            ValueError: If an invalid attribute is passed in kwargs.
        """
        # Step 1: Find the user by ID using find_user_by
        user = self.find_user_by(id=user_id)

        # Step 2: Update user's attributes
        for key, value in kwargs.items():
            # Validate if the key is a valid attribute of the User model
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        # Step 3: Commit the changes to the database
        self._session.commit()
