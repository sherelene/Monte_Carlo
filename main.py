# Author: Sherelene De Belen
# Assignment: Project 1 Task 2
# Completed (or last revision): 02/11/2022
# This project uses the Monte-Carlo method to calculate Pi. The goal is to achieve a result as accurate to Math.pi

import random
import math


def run_simulation(darts_thrown):
    hits = 0
    exact_pi = math.pi   # Accurate pi number

    for throws in range(darts_thrown):
        # generates random number between 0 and 1 for x and y coordinates
        x_throw = random.random()
        y_throw = random.random()

        # finding if darts are inside the circle
        if x_throw ** 2 + y_throw ** 2 <= 1:
            hits += 1

    # estimate value of pi
    pi = 4.0 * float(hits) / float(darts_thrown)

    # difference between pi estimate and pi
    pi_difference = abs(pi - exact_pi)

    print("Total number of Darts thrown = ", darts_thrown)
    print("Number of dart throws inside the circle = ", hits)
    print("Estimated value of Pi = ", '%.17f' % pi)

    if pi_difference > 0:  # to print + sign in difference
        print("Relative Difference = +", pi_difference, "\n")
    else:  # to print - sign in difference
        print("Relative Difference = -", pi_difference, "\n")

    return pi


if __name__ == '__main__':
    numOfThrowsList = [100, 1000, 10000, 100000, 100000000]

    for i in numOfThrowsList:
        pi_estimation = run_simulation(i)

