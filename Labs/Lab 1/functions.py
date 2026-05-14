# This is a landing page for some helper functions that we will clal in the notebook. 

def myCoolFunction(input:bool):
    """This is a text print based on user input.
    Inputs:
    - input: a boolean value that determines the output message
    Outputs:
    - None: this function onlu prints a message based on the input value.
    """
    if input:
        print("This is a cool function!")
    else:
        print("This function could use some work.")