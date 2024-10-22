from time import time

def test(inputs, func):
    """
    Tests whether the given function works correctly via printing
    the output of the function given the arguments.
    
    Parameters:
    -----------
    inputs: a list of inputs/arguments. e.g. [[*args1], [*args2]]
    func: function
    """
    start = time()
    for args in inputs:
        output = ""
        for arg in args:
            output += str(arg) + " "
        print(output + ": " + str(func(*args)))
        
    print("Time elapsed: %.5f seconds" % (time()-start))