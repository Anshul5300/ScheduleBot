class Reminder:

    def __init__(self, description, time):
        """
        Function:
            __init__
        Description:
            Creates a new Event object instance
        Input:
            self - The current Event object instance
            description - description - text field that contains notes about an reminder
            time - int object representing the time from now
        Output:
            - A new Reminder object instance
        """
        self.description = description
        self.time = time

    def __str__(self):
        """
        Function:
            __str__
        Description:
            Converts a Reminder object into a string
        Input:
            self - The current Reminder object instance
        Output:
            A formatted string that represents all the information about an Reminder instance
        """
        output = (
            self.description
            + " "
            + str(self.time)
            
        )
        return output

    def __lt__(self, other):
        """
        Function:
            __lt__
        Description:
            Finds whether the current reminder starts before another
        Input:
            self - The current Reminder object instance
            other - The Reminder object we are comparing self to
        Output:
            True - self starts before other
            False - self starts after other
        """
        return self.time < other.time

    def __le__(self, other):
        """
        Function:
            __le__
        Description:
            Finds whether the current reminder starts before or at the same time as another
        Input:
            self - The current Reminder object instance
            other - The Reminder object we are comparing self to
        Output:
            True - self starts before or at the same time as other
            False - self comes after other
        """
        return self.time <= other.time

    def __gt__(self, other):
        """
        Function:
            __gt__
        Description:
            Finds whether the current Reminder starts after another
        Input:
            self - The current Reminder object instance
            other - The Reminder object we are comparing self to
        Output:
            True - self starts after other
            False - self comes before other
        """
        return self.time > other.time

    def __ge__(self, other):
        """
        Function:
            __ge__
        Description:
            Finds whether the current reminder starts after or at the same time as another
        Input:
            self - The current Reminder object instance
            other - The Reminder object we are comparing self to
        Output:
            True - self starts after or at the same time as other
            False - self comes before other
        """
        return self.time >= other.time


    def to_list(self):
        """
        Function:
            to_list
        Description:
            Converts an Reminder object into a list
        Input:
            self - The current Reminder object instance
        Output:
            array - A list with each index being an attribute of the self Reminder object
        """
        array = [self.description, str(self.time)]
        return array