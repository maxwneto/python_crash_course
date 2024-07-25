class person:

    #methods
    def __init__(self, name, birth_date, gender, color, email):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.color = color      
        self.email = email

    def __str__(self):
        return (f'Name: {self.name} \nBirthday: {self.birth_date}, \nGender: {self.gender}, '
                f'\nEthnicity: {self.color}, \nE-mail: {self.email}')
    
    def sleep(self):
        print("Sleeping")
    
    def wakeup(self):
        print("Waking Up")
    
    def eat(self):
        print("Eating")
    
    def walk(self):
        print("Walking")
    
    def sit(self):
        print("Sitting")
    
    def study(self):
        print("Studying")
    
    def talk(self):
        print("Talking")
    
    def greet_person(self):
        return f"Hello, {self.name}!"