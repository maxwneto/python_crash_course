from person import person

person1 = person('Max', "14/12/1980", 'male', 'black', 'maxforexample@gmail.com')

person1.sleep()
person1.wakeup()
person1.walk()
person1.sit()
person1.talk()
person1.eat()

print("\n")

person2 = person('Heitor', "16/02/2016", 'male', 'black', 'heitorforexample@gmail.com')
                 
person3 = person('Sara', "14/03/1979", 'female', 'black', 'saraforexample@gmail.com')
                 
people = {person1, person2, person3}


for p1 in people:
    print(p1)
    print("\n")

