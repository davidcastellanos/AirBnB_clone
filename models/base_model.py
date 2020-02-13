#!/usr/bin/python3
"""
Base module
"""
import uuid
from datetime import datetime, date, time


class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now(tz=None).isoformat(sep='T')
    updated_at = datetime.now(tz=None).isoformat(sep='T')

    def __str__(self):
        """
        Print [<class name>] (<self.id>) <self.__dict__>
        """
        return "[BaseModel] " + "(" + str(self.id) + ") "\
            + str(self.__dict__)

    def save(self):
        """
        Update date-time update_at public attribute
        """
        self.updated_at = datetime.now(tz=None).isoformat(sep='T')

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values __dict__ of instance
        """
        return self.__dict__
