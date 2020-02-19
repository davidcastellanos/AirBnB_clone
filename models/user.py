#!/usr/bin/python3
"""
User module inherits from Base Model
"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    Class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
