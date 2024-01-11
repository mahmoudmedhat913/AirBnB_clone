#!/usr/bin/python3
"""define review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent review"""

    place_id = ""
    user_id = ""
    text = ""
