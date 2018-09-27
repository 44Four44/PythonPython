class Beans:
    def __init__(self, liste):
        '''
        Constructor to build a book object


        Parameters
        ----------

        liste : int list
        	The initial price of the book
        '''


        self.beancount = liste


b = [1, 3, 10, 2]

ethan = Beans(b)
print(ethan.beancount[2])