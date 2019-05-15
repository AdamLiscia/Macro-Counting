from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class Food(Base):
    def __init__(self, name, calories, protein, fat, carb, fiber, serving):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.fiber = fiber
        self.serving = serving
