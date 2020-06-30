class User():  # the parentheses in the class defination is empty cause we're creating the class from scratch
    """Created a user class"""
    def __init__(self, first_name, last_name,
                 nationality, sex, birth_date):     # varius attributes
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.sex = sex
        self.birthdate = birth_date

    def describe_user(self):
        full_name = self.first_name+" "+self.last_name
        print("User's full name: "+ full_name.title())
        print(self.first_name.title() + " is "+ self.nationality.title())
        print(self.first_name.title() + " is "+ self.sex)
        print(self.first_name.title() + "'s birth date is: "+ str(self.birthdate))

    def greet_user(self):
        print("Congratulations!! "+self.first_name.title()+ ". You have started your journey as Pythonastas.")

my_self = User('elias', 'islam', 'bangladeshi', 'male', 'Nov 16th, 1997') #declaring my_self as the first instance of user class
my_self.describe_user()      #calling the describe_user method with the dot notation
my_self.greet_user()         #calling the greet_user method with the dot notation

