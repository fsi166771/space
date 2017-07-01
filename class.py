class Animal(object):
    def run(self):
        print 'Animal is running..'
class Dog(Animal):
    def run(self):
        print 'dog is running..'
    def eat(self):
        print 'Eating meat..'
class Cat(Animal):
    def run(self):
        print 'Cat is running..'
    def eat(self):
        print 'cat eating meat..'
def run_twice(animal):
    animal.run()
    animal.run()


dog=Dog()
dog.run()
dog.eat()
cat=Cat()
cat.run()
cat.eat()
run_twice(cat)
