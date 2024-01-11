#!/usr/bin/python3
"""define user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """represent user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
