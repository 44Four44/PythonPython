# List of different praises
praises = ["Wow! You are a natural!", "Your IQ is above 100!", "Immaculate!", "Egregious!", "Delicious!",
           "Albert Einstein would be jealous!", "You have a big brain!", "You would even pass Dunne's class!"]

# List of difficulties
difficulties = ['easy', 'medium', 'hard']

# List of problem types
problem_types = ['addition', 'subtraction', 'multiplication', 'division']

# Current difficulty level
difficulty = difficulties[0]

# Current problem type
problem_type = problem_types[0]

# List of accounts
accounts = []

# Currently active acccount
active = 0

# Data path file name
file_path = '/Users/EthanWang/Python/Khan Academy/data.txt'

class Account:
    """
    An account that stores the user's progress

    Attributes
    ----------
    answered : int list
        The total number of completed problems for each problem type
    attempts : int list
        The total number of attempts for each problem type

    Methods
    -------
    addAnswered(type : str) -> None
        Increases the number of answered problems for a specific problem type by one
    addAttempts(type : str) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """

    def __init__(self, index, name, answered, attempts):
        """
        Constructor to build a Khan Academy account

        Parameters
        ----------
        name : str
            Name of the account
        index : int
            Position of data in the data text file (for distinguishing between multiple accounts)
        answered : int list
            An integer list of the total amount of answered problems for each problem type (index)
        attempts : int list
            An integer list of the total amount of answered problems for each problem type (index)

	    Returns
        -------
        None

        """
        self.index = index
        self.name = name
        self.answered = answered
        self.attempts = attempts

    def addAnswered(self, type):
        """
        Increases the number of answered problems for a specific problem type by one and updates it on the data file

        Parameters
        ----------
        type : int
            The problem type that was answered as an index of 'problem_types'

        Returns
        -------
        None

        """

        # Opens and updates the text file to update numbers
        with open(file_path, 'r') as file:
            data = file.readlines()

        # Total answered problems
        number1 = int(data[self.index + 6]) + 1
        self.answered[4] = number1

        number2 = int(data[self.index + 2 + type]) + 1
        self.answered[type] = number2

        data[self.index + 6] = str(number1) + "\n"
        data[self.index + 2 + type] = str(number2) + "\n"

        # Writes everything back
        with open(file_path, 'w') as file:
            file.writelines(data)

    def addAttempts(self, type):
        """
        Increases the number of attempted problems for a specific problem type by one and updates it on the data file


        Parameters
        ----------
        type : int
            The problem type that was answered as an index of 'problem_types'

        Returns
        -------
        None

        """

        # Opens and updates the text file to update numbers
        with open(file_path, 'r') as file:
            data = file.readlines()

        # Total attempted problems
        number1 = int(data[self.index + 11]) + 1
        self.attempts[4] = number1

        number2 = int(data[self.index + 7 + type]) + 1
        self.attempts[type] = number2

        data[self.index + 11] = str(number1) + "\n"
        data[self.index + 7 + type] = str(number2) + "\n"

        # Writes everything back
        with open(file_path, 'w') as file:
            file.writelines(data)

    def reset(self):
        """
        Resets the user's stats

        Parameters
        ----------
        None

        Returns
        -------
        None
        
        """

        # Opens and updates the text file to update numbers
        with open(file_path, 'r') as file:
            data = file.readlines()

        # Set values to 0
        for i in range (2, 12):
            data[self.index + i] = '0\n'
        self.answered = ['0', '0', '0', '0', '0']
        self.attempts = ['0', '0', '0', '0', '0']

        # Writes everything back
        with open(file_path, 'w') as file:
            file.writelines(data)



