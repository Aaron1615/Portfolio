from sequence_object import sequence

def test_initialize_no_error(input1,input2,func,expected):
    try:
        output = func(input1, input2)
    except TypeError:
        print("TEST FAILURE expected: " + str(expected) + " input1: " + str(input1) + " input2: " + str(input2) + " function: " + str(func))
        return
        
def test_initialize_error(input1,input2,func,expected):
    try:
        output = func(input1, input2)
    except TypeError:
        return
    else:
        print("TEST FAILURE expected: " + "Failure" + " output: " + str(output) + " input1: " + str(input1) + " input2: " + str(input2) + " function: " + str(func))

def Test(input,func,expected):
    """Given a function, an input, and an expected result, returns True
    if the results match, otherwise returns False"""
    output = input.func()
    if output != expected:
        print("TEST FAILURE expected: " + str(expected) + " output: " + str(output) + "input: sequence " + str(input.seq) + " type " + str(input.seq_type) + " function: " + str(func))
def test_error(input,func,expected):
    try:
        output = input.func(input.seq)
    except TypeError:
        return
    if output != expected:
        print("TEST FAILURE expected: " + str(expected) + " output: " + str(output) + "input: sequence " + str(input.seq) + " type " + str(input.seq_type) + " function: " + str(func))


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
