# New Dog Class Version 1.0

class Dog():
    
    def __init__(self,name,age):
    # _init_ method, is called each time an object is created from a class
    # here we are defining objects created from the class to expect two
    # input parameters / arguments (name and age) to be passed during instantiation
    # arguments / variables defined in this way are accessible to every method in the class
    # arguments / variables defined in this way are referred to as attributes
        self.name = name
        self.age = age
    
    # Here we can define a Classes 'Instance Method'
    def Sit(self):
        # A class method defining actions to take to make the Dog object 'Sit' are defined here
        print('\n\nthe dog named:' + ' ' + str(self.name) + ' , ' + 'which is'+' ' + str(self.age) + ' ' + 'years old' + ' ' + 'is now sitting')

    def Roll_Over(self):
        print('Dog is now rolling over and over and over')


    def get_humanAge(self):
        #calculate dog age in human years, convert the value to a string and assign it to the human_age variable
        human_age = str(self.age / 7)
        
        #return the human_age variable once the get_humanAge method has executed
        return human_age




 #   def output_human_age(self,Dog_Years_to_Human()):
 #       print('dog age in human terms is :' + ' ' + human_age)




#this code is control and call element

#here we are asking for user input from the terminal - this is to define a new name for our dog
newDogName = input('\n\nplease enter a name for our new dog:' )


newDogAge = int(input('\n\n\nplease enter how old the new dog is:' ))





# object called fido_the_dog is created / initialised from the Dog() class
fido_the_dog = Dog(newDogName,newDogAge)



# The Sit() method is called from the Dog() class against the instance of it called fido_the_dog
fido_the_dog.Sit()


print ('\n\n\ndog age in human terms is :' + ' ' + fido_the_dog.get_humanAge())





#fido_the_dog.output_human_age()

#print ('dog age in human terms is :' + ' ' + str(fido_the_dog.human_age))