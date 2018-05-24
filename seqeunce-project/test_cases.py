from sequence_object import sequence

def test_initialize_no_error(input1,input2,func,expected):
    output = None
    try:
        output = func(input1, input2)
    except TypeError:
        print("TEST FAILURE expected: " + str(expected) + " input1: " + str(input1) + " input2: " + str(input2) + " function: " + str(func) + " output: " + str(output))
        return
        
def test_initialize_error(input1,input2,func,expected):
    try:
        output = func(input1, input2)
    except TypeError:
        return
    else:
        print("TEST FAILURE expected: " + "Failure" + " output: " + str(output) + " input1: " + str(input1) + " input2: " + str(input2) + " function: " + str(func))

def Test(input1,input2,func,expected):
    """Given two inputs for creating the sequence object, a function, and an expected result,
    returns nothing if the results match, otherwise returns a sting of what failed"""
    test_case = sequence(input1, input2)
    output = func(test_case)

    if output != expected:
        print("TEST FAILURE expected: " + str(expected) + " output: " + str(output) + "input: sequence " + str(input1) + " type " + str(input2) + " function: " + str(func))

def test_error(input1,input2,func,expected):
    """Given two inputs for creating the sequence object, a function, and an expected result,
    returns nothing if the proper error is raised, otherwise returns a string of what failed"""
    test_case = sequence(input1, input2)
    try:
        output = func(test_case)
    except AttributeError:
        return
    if output != expected:
        print("TEST FAILURE expected: " + str(expected) + " output: " + str(output) + " input: sequence " + str(input1) + " type " + str(input2) + " function: " + str(func))


#Use multiple test cases for each function

#test suite for creating sequence object and is_DNA function
test_initialize_no_error("ATGCATGCATGCATGCATGC", "DNA", sequence,None)
test_initialize_error("aguaguaguaguaguaguug", "DNA", sequence, None)
test_initialize_no_error("", "DNA", sequence,None)

#test suite for creating sequence object and is_RNA function
test_initialize_no_error("AUGUGUAUGUCGU", "RNA", sequence,None)
test_initialize_error("atatatatatatat", "RNA", sequence, None)
test_initialize_no_error("", "RNA", sequence,None)

#test suite for creating sequence object and is_PROTEIN function
test_initialize_no_error("AYTAYTAYA", "PROTEIN", sequence,None)
test_initialize_error("atatatatatatatuz", "PROTEIN", sequence, None)
test_initialize_no_error("", "PROTEIN", sequence,None)

#test suite for translate function
    #test normal functionality
Test("AUGAGGGGGGGGUAA","RNA",sequence.translate,"met-arg-gly-gly")
#RNA after Stop codon
Test("AUGAGGGGGGGGUAAGGG","RNA",sequence.translate,"met-arg-gly-gly")
#No start Codon (should produce an error)
test_error("AGGGGGGGGUAAGGG", "RNA",sequence.translate,None)
#No Stop Codon
Test("AUGAGGGGGGGGUACCC", "RNA",sequence.translate, "met-arg-gly-gly-tyr")
#DNA input
Test("TACCCCCCC","DNA",sequence.translate, "met-gly-gly")