#!/usr/bin/python3

import uuid
import datetime

"""
A class that defines all common attributes/methods for other classes.
"""


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes.

    Attributes:
        id: unique id for each instance of this object.
        created_at: time of creation.
        updated_at: last time the instance was modified.

    Methods:
        save(self): updates the updated_at variable.
        to_dict(self): returns a dictionary containing all keys/values needed.
    """

    def __init__(self):
        """
        initializes the private attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        prints:[<class name>] (<self.id>) <self.__dict__> when object is called
        """
        temp = self.__dict__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, temp)

    def save(self):
        """
        updates the public instance attribute updated_at = current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ and more.
        """
        temp = self.__dict__
        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = temp['updated_at'].isoformat()
        temp['created_at'] = temp['created_at'].isoformat()
        return temp