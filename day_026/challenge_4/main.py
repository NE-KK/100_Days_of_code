# 100 Days of code by Angela Yu
# Day 26 - challenge 4 - Dictionary Comprehensions word length count

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {k:len(k) for k in sentence.split(" ")}
print(result)