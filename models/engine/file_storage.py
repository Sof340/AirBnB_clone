#!/usr/bin/python3

import json
import os
"""
A class that serializes and deserializes data to json.
"""


class FileStorage():
    """
    A class that serializes/deserializes instances to/from a JSON file.

    Attribues:
        __file_path: private attribute {string} holds the path of json file.
        __objects: dictionary - empty but will store all objects.

    Methods:
        all(self): returns the dictionary __objects.
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path).
        reload(self): deserializes the JSON file to __objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path).
        """
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(self.__objects, file)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def reload(self):
        """
        deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    self.__objects[key] = value

        except (FileNotFoundError, TypeError):
            pass
