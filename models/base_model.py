#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for common attributes/methods."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Basemodel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update the public instance attribute update_at."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing keys/value of __dict__."""
        mod_dict = self.__dict__.copy()
        mod_dict['__class__'] = self.__class__.__name__
        mod_dict['created_at'] = self.created_at.isoformat()
        mod_dict['updated_at'] = self.updated_at.isoformat()
        return mod_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance"""
        clname = self.__class__.name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
