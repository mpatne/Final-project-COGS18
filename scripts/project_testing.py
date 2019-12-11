from project_main import *

initial_input = "Hello, Grookey!"
def test_1(u_input):
    """Tests the parse_input function"""
    u_input = parse_input(u_input)
    print("Test 1:", u_input)
    return u_input

def test_2(u_input):
    """Tests the start_bot function"""
    print("Test 2: ")
    start_bot(u_input)
    return u_input

initial_input = test_1(initial_input)
test_2(initial_input)

input_loop()
