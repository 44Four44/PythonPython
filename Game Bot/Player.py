import pygame

pygame.init()

# size of the square tiles that make up the map
tile_size = 40

screen = pygame.display.set_mode((tile_size * 20, tile_size * 15))
pygame.display.set_caption("mmmmmmmmmmmm")

# true if the game is running
run = True

class Player:
    """
    The player that moves to complete levels

    Attributes
    ----------
    x : float
        The x coordinate of the player
    y : float
        The y coordinate of the player
    speed : float
        The speed of the player
    size : int
        The side length of the square player
    color : int list
        The color of the player in RGB


    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """

    def __init__(self, x, y, speed, size, color):
        """
        Constructor to build a player

        Parameters
        ----------
        x : float
            The x coordinate of the player
        y : float
            The y coordinate of the player
        speed : flot
            The speed of the player
        size : int
            The side length of the square player
        color : int list
            The color of the player in RGB

	    Returns
        -------
        None

        """
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color


    def display(self):
        """
        Draw the player

        Parameters
        ----------
        None

        Return
        ------
        None

        """

        pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2]),
                        (self.x, self.y, self.size, self.size))

    def move(self, keys):
        """
        Checks for player movement, then updates position

        Parameters
        ----------
        keys : pygame keys

        Return
        ------
        None

        """

        # checks for which keys are pressed and moves the player
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed