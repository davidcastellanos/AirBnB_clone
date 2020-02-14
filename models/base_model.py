#!/usr/bin/python3
"""
Base module
"""
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.now().isoformat()
                if key == 'updated_at':
                    value = datetime.now().isoformat()

    def __str__(self):
        """
        Print [<class name>] (<self.id>) <self.__dict__>
        """
        return "[" + self.__class__.__name__ + "]"\
            + "(" + str(self.id) + ") "\
            + str(self.__dict__)

    def save(self):
        """
        Update date-time update_at public attribute
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values __dict__ of instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
