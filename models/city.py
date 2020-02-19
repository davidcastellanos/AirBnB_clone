#!/usr/bin/python3
"""
City module inherits from Base Model
"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """
    Class City
    """
    state_id = ""
    name = ""
