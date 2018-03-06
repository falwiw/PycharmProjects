#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Xs (object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def sg(self):
        if self.age < 25:
            print("年轻")
        return


if __name__ == '__main__':
    xs = Xs("kevin", 24, 150)
    print(xs.sg())



