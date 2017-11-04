import uuid


class Recipe(object):
    """A class representing a ACME recipe"""
    DIFFICULTIES = [1, 2, 3]

    def __init__(self, id=None, name=None, prep_time=None, difficulty=None,
                 vegetarian=False):
        """
            Args:
                id: (obj): A UUID v4 object or string
                name: (str): Recipe name
                prep_time: (int): Preparation time in minutes
                difficulty: (int): Preparation difficulty, either 1, 2 or 3
                vegetarian: (bool): Whether a recipe is vegetarian or not
        """
        self.id = id
        self.name = name
        self.prep_time = prep_time
        self.difficulty = difficulty
        self.vegetarian = vegetarian

    @property
    def id(self):
        """Returns the id of the recipe"""
        return self._id

    @id.setter
    def id(self, value):
        """
        Validates and sets the id of the recipe or creates a new one if value
        is empty
        """
        if value is None:
            self._id = uuid.uuid4()
        elif isinstance(value, uuid.UUID):
            if value.version is 4:
                self._id = value
            else:
                raise ValueError({"id": "ID must be a UUID v4"})
        else:
            self._id = uuid.UUID(value)

    @property
    def name(self):
        """Returns the name of the recipe"""
        return self._name

    @name.setter
    def name(self, value):
        """Validates and sets the name of the recipe"""
        if value is None or isinstance(value, str):
            self._name = value
        else:
            raise ValueError({"name": "Name must be a string"})

    @property
    def prep_time(self):
        """Returns the prep time of the recipe in miutes"""
        return self._prep_time

    @prep_time.setter
    def prep_time(self, value):
        if value is None or (isinstance(value, int) and value > 0):
            self._prep_time = value
        else:
            raise ValueError(
                    {"prep_time": "Prep time must be a positive integer"})

    @property
    def difficulty(self):
        """Returns the difficulty of the recipe"""
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        """Validates and sets difficulty of the recipe"""
        if value is None or value in Recipe.DIFFICULTIES:
            self._difficulty = value
        else:
            msg = "Difficulty must be one of {}".format(Recipe.DIFFICULTIES)
            raise ValueError({"difficulty": msg})

    @property
    def vegetarian(self):
        """Returns the vegetarian flag of the recipe"""
        return self._vegetarian

    @vegetarian.setter
    def vegetarian(self, value):
        """Validates and sets the vegetarian flag of the recipe"""
        if isinstance(value, bool):
            self._vegetarian = value
        else:
            raise ValueError({"vegetarian": "Vegetarian must be a boolean"})
