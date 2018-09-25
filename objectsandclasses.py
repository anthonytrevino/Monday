class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends =[]
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1
        print("Hello {0}, I am {1}!".format  (other_person.name, self.name))

    def print_contact_info(self):
        print("My email: " + self.email + ", and my phone number: " + self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        len(self.friends)

 #jordan.friends.append(sonny)
# sonny.friends.append(jordan)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

sonny.print_contact_info()
jordan.print_contact_info()

jordan.add_friend(sonny)
sonny.add_friend(jordan)




# print(len(jordan.friends))
# print(len(sonny.friends))




# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print(self.make,self.model,self.year)
#
# car = Vehicle("Honda", "Accord", "2019")
# car.print_info()





# class Dog:
#
#     # Class Attribute
#     species = 'mammal'
#
#     # Initializer / Instance Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # Instantiate the Dog object
# philo = Dog("Philo", 5)
# mikey = Dog("Mikey", 6)
#
# # Access the instance attributes
# print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))
#
# # Is Philo a mammal?
# if philo.species == "mammal":
#     print("{0} is a {1}!".format(philo.name, philo.species))
#
