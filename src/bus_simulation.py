import random

journey_time = [20,25,30,35,40,45]

probabilities = [0.05, 0.10, 0.20, 0.30, 0.20, 0.15]

random_journey = random.choices(journey_time, weights=probabilities)[0]

print(random_journey) 