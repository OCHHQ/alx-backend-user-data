#!/usr/bin/env python3
"""
SQLAlchemy User model for authentication service
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    User model for the authentication service database

    Attributes:
        __tablename__: Name of the database table
        id: Primary key (integer)
        email: User's email (non-nullable string)
        hashed_password: Hashed password (non-nullable string)
        session_id: User session ID (nullable string)
        reset_token: Password reset token (nullable string)
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
