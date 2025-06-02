import time

a = 18
b = 25

def get_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

def test_nod(function):
    #-----Test 1-----
    if function(28, 35) == 7:
        print("Test 1 - ok.")
    else:
        print("Test 1 - fail.")

    # -----Test 2-----
    if function(1, 100) == 1:
        print("Test 2 - ok.")
    else:
        print("Test 2 - fail.")

    # -----Test 3-----
    st = time.time()
    res = function(2, 1000000000000000000000000000)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("Test 3 - ok.")
    else:
        print("Test 3 - fail.")

test_nod(get_nod)
