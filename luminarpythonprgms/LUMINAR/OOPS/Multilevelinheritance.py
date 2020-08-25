class Parent:

    def m1(self):

        print("inside parent1")

class child(Parent):

    def m2(self):

        print("inside child")

class Subchild(child):

    def m3(self):

        print("inside subchild")

ch=child()

ch.m2()
ch.m1()

su=Subchild()
su.m3()
su.m2()
su.m1()


pa=Parent()
pa.m1()