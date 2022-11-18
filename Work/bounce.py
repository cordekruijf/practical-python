# bounce.py
#
# Exercise 1.5

height = 100
bounce = 1

while bounce <= 10:
    height = height * 0.6
    print(round(height, 4))
    bounce += 1
