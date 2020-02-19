#!/usr/bin/python3
"""
Base module
"""
import models
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        self.updated_at = datetime.strptime(datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f')
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values __dict__ of instance
        """
        pdp = self.__dict__.copy()
        pdp['__class__'] = self.__class__.__name__
        pdp['created_at'] = self.created_at.isoformat()
        pdp['updated_at'] = self.updated_at.isoformat()
        return pdp
