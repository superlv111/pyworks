import pygame


# help(pygame.key)


# a = {'key':'value'}
# b = list(a.values())

# print(b)
# print(isinstance(b, list))

class A():

    def __init__(self):
        self.a = 1

    def print(self):
        print(self.a)


a = A()

a.print = 1
print(dir(a))

b = [0,1]

print("anything")

print("nothing")