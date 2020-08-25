class Parent:

    def m1(self):

        print("inside parent1")

class child:

    def m2(self):

        print("inside child")

class Subchild(child,Parent):

    def m3(self):

        print("inside subchild")

s=Subchild()

s.m2()
s.m1()