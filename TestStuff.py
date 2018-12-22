
class testClass2:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        #self.addResult = addResult

    @classmethod
    def getUserInput2(cls):
        print('program now running get user input....')
        return cls(
            int(input('please enter number 1 :')), 
            int(input('please enter numner 2 :')),
        )


    @classmethod
    def addUserInput(self,number1, number2):
        print('program now adding nnumbers up')
        print(number1 + number2)
        print('x+y')



runInputProgram = testClass2.getUserInput2()



runCalculationAdd = testClass2.addUserInput(runInputProgram.number1,runInputProgram.number2)

