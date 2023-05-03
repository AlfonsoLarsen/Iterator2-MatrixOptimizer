import random
import logging
import tabulate 
import math 

from tabulate import tabulate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Matrix:
    def __init__(self, size=5, range_min=1, range_max=50):
        self.size = size
        self.range_min = range_min
        self.range_max = range_max
        self.matrix = []
        self.create_matrix()

    def create_matrix(self):
        for i in range(self.size):
            row = random.sample(range(self.range_min, self.range_max+1), self.size)
            self.matrix.append(row)

    def evaluate(self, matrix):
        columns = []
        for j in range(self.size):
            product = 1
            for i in range(self.size):
                product *= matrix[i][j]
            columns.append(product)
        return sum(columns)

    def shuffle_row(self, row):
        a, b = random.sample(range(self.size), 2)
        row[a], row[b] = row[b], row[a]

    def optimize(self):
        best_score = -1
        best_matrix = self.matrix
        for i in range(100000):
            if i==0:
               print("  Original Matrix") 
               print(tabulate(self.matrix, tablefmt="fancy_grid"))
            new_matrix = [row.copy() for row in best_matrix]
            row_index = random.randrange(self.size)
            self.shuffle_row(new_matrix[row_index])
            score = self.evaluate(new_matrix)
            if score > best_score:
                best_score = score
                best_matrix = new_matrix
                sym_space= " "* (12-int(math.log(score,10)))
                logging.info(f"New best score: {score}" + sym_space   +  f"Iteration: {i}")

        return best_matrix


matrix = Matrix()
best_matrix = matrix.optimize()
print("  Best Matrix ") 
print(tabulate(best_matrix, tablefmt="fancy_grid"))
