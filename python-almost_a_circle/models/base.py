#!/usr/bin/python3
"""Module containing the Base class."""
import csv
import json


class Base:
    """Base class for managing id attribute across models."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes set using dictionary."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = None
            if dummy:
                dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return list of instances loaded from JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV representation of list_objs to file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of instances loaded from CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = []
                reader = csv.DictReader(f, fieldnames=fieldnames)
                for row in reader:
                    d = {k: int(v) for k, v in row.items()}
                    list_dicts.append(d)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle graphic module."""
        import turtle

        t = turtle.Turtle()
        t.screen.bgcolor("#1e1e2e")
        t.pensize(3)
        t.speed(1)

        if list_rectangles:
            t.color("#89b4fa")
            for rect in list_rectangles:
                t.penup()
                t.goto(rect.x, rect.y)
                t.pendown()
                for _ in range(2):
                    t.forward(rect.width)
                    t.left(90)
                    t.forward(rect.height)
                    t.left(90)

        if list_squares:
            t.color("#a6e3a1")
            for sq in list_squares:
                t.penup()
                t.goto(sq.x, sq.y)
                t.pendown()
                for _ in range(4):
                    t.forward(sq.size)
                    t.left(90)

        t.hideturtle()
        turtle.exitonclick()
