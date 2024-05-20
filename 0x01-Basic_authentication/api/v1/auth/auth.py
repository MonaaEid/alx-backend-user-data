#!/usr/bin/env python3
""" module Auth"""
from flask import Flask, jsonify, request
from typing import List, TypeVar


class Auth:
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Ensure path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'

        # Normalize excluded paths to ensure they end with a slash
        excluded_paths = [p if p.endswith('/') else p + '/' for p in excluded_paths]

        if path in excluded_paths:
            return False

        return True


    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
