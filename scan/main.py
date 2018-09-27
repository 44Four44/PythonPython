# -----------------------------------------------------------------------------
# Name:        main (python.py)
# Purpose:     To analyze the statistics of the sentences in a text file
#
#
# Author:      Ethan Wang
# Created:     21-Sep-2018
# Updated:     24-Sep-2018
# ------

# Location of the text file
filename = '/Users/EthanWang/Python/scan/text.txt'
# Opens the file for reading
file = open(filename, 'r')
# Stores file into a string
contents = file.read()


class Sentence():
    """
    A sentence with the number of words in each word class

    Attributes
    ----------
    nouns : int
        Number of nouns in self
    verbs : int
        Number of verbs in self
    adjectives : int
        Number of adjectives in self
    adverbs : int
        Number of adverbs in self
    pronouns : int
        Number of pronouns in self
    prepositions : int
        Number of prepositions in self
    conjunctions : int
        Number of conjunctions in self
    determiners : int
        Number of determiners in self


    Methods
    -------
    # note, do not list private methods in this section.  Do not include this line
    printAuthor() -> None
    	Prints the name of the author to the console
    printPrice() -> None
    	Prints the price of the book to the console
    printTitle() -> None
    	Prints the name of the book to the console
    increasePrice(increase : float) -> None
    	Attempts to increase the price by a float value

    """


    def __init__(self, content):
        """
        Constructor to build a sentence object


        Parameters
        ----------
        content : str
            The sentence

        """

        self.content = content


print(contents.index('.'))

