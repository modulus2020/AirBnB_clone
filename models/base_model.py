#!/usr/bin/python3
"""Module that defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class for common attributes/methods."""

    def __init__(self):
        """Initialize a new Basemodel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute update_at."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing keys/value of __dict__."""
        mod_dict = self.__dict__.copy()
        mod_dict['__class__'] = self.__class__.__name__
        mod_dict['created_at'] = self.created_at.isoformat()
        mod_dict['updated_at'] = self.updated_at.isoformat()
        return mod_dict
