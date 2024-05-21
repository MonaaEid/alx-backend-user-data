#!/usr/bin/env python3
""" module Auth"""
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """For now, this class is empty and inherits everything from Auth"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization
        header for Basic Authentication."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
