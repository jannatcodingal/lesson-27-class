class Dog:
    # Class variable
    species = "Canis familiaris"
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
dog1 = Dog("ben", "Golden Retriever")
dog2 = Dog("danny", "German Shepherd")
dog1.display_info()
dog2.display_info()