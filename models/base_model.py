#!/usr/bin/python3
"""Module that defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for common attributes/methods."""

    def __init__(self):
        """Initialize a new Basemodel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
