#!/usr/bin/env python3
""" module Auth"""
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """For now, this class is empty and inherits everything from Auth"""
    pass
