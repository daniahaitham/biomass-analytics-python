"""Small container class used by the genetic-algorithm notebook to return its results
(same attribute names as the EvoloPy framework's `solution` class)."""


class solution:
    def __init__(self):
        self.bestIndividual = []
        self.bestScore = 0
        self.convergence = []
        self.executionTime = 0
