#!/usr/bin/env python3
"""Auth module"""

from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
import bcrypt


def _hash_password(password: str) -> str:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class
    """

    def __init__(self):
        """Initialize a new Auth instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user
