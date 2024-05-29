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
