import os,sys
debug=False
if not debug:
    print("INFO: Debug mode is disabled")
else:
    print("INFO: Debug mode is enabled")
if not os.path.exists("solution.py"):
    print("ERROR: You do NOT have solution.py in this directory.")
    sys.exit(1)
else:
    try:
        if debug:
            from key import *
            print("INFO: Successfully imported key.py")
        else:
            from solution import *
            print("INFO: Successfully imported solution.py")
        print()
    except:
        print("ERROR: Failed to import solution.py")
        sys.exit(1)
# return True if passed. False otherwise
def check_basic_write_file():
    if os.path.exists("your_output_file/basic_write_empty.txt"):
        os.remove("your_output_file/basic_write_empty.txt")
    if simple_write_file("your_output_file/basic_write_empty_test.txt","")=="not_implemented_yet":
        print("INFO: simple_write_file() is failed because it is not implemented.")
        if os.path.exists("your_output_file/basic_write_empty_test.txt"):
            os.remove("your_output_file/basic_write_empty_test.txt")
        return False
    else:
        print("INFO: Testing simple_write_file() with empty string")
        simple_write_file("your_output_file/basic_write_empty.txt","")
        if os.path.exists("your_output_file/basic_write_empty.txt"):
            print("INFO: File exists")
            print("INFO: Checking content...")
            with open("your_output_file/basic_write_empty.txt", "r") as of:
                if of.read()=="":
                    print("INFO: simple_write_file() PASS w/ empty string. Congratulations!")
                    os.remove("your_output_file/basic_write_empty.txt")
                    os.remove("your_output_file/basic_write_empty_test.txt")
                    return True
                else:
                    print("INFO: simple_write_file() failed due to non-empty file")
                    return False
        else:
            print("INFO: Failed due to file does not exist")
            return False
def check_basic_write_file_str():
    if os.path.exists("your_output_file/basic_write_str.txt"):
        os.remove("your_output_file/basic_write_str.txt")
    if simple_write_file("your_output_file/basic_write_str_test.txt","-1")=="not_implemented_yet":
        print("INFO: simple_write_file() is failed because it is not implemented.")
        if os.path.exists("your_output_file/basic_write_str_test.txt"):
            os.remove("your_output_file/basic_write_str_test.txt")
        return False
    else:
        print("INFO: Testing simple_write_file() with a string")
        simple_write_file("your_output_file/basic_write_str.txt","--")
        if os.path.exists("your_output_file/basic_write_str.txt"):
            print("INFO: File exists")
            print("INFO: Checking content...")
            with open("your_output_file/basic_write_str.txt", "r") as of:
                if of.read()=="--":
                    print("INFO: simple_write_file() PASS w/ a string. Congratulations!")
                    os.remove("your_output_file/basic_write_str.txt")
                    os.remove("your_output_file/basic_write_str_test.txt")
                    return True
                else:
                    print("INFO: simple_write_file() failed due to incorrect content in that file")
                    return False
        else:
            print("INFO: Failed due to file does not exist")
            return False
def check_int_write_file():
    if os.path.exists("your_output_file/basic_write_int.txt"):
        os.remove("your_output_file/basic_write_int.txt")
    if simple_write_file("your_output_file/basic_write_int_test.txt","")=="not_implemented_yet":
        print("INFO: simple_write_file() is failed because it is not implemented.")
        if os.path.exists("your_output_file/basic_write_int_test.txt"):
            os.remove("your_output_file/basic_write_int_test.txt")
        return False
    else:
        print("INFO: Testing simple_write_file() with an integer")
        try:
            simple_write_file("your_output_file/basic_write_int.txt",100)
        except:
            print("INFO: simple_write_file() is failed due to type error")
            os.remove("your_output_file/basic_write_int.txt")
            os.remove("your_output_file/basic_write_int_test.txt")
            return False
        if os.path.exists("your_output_file/basic_write_int.txt"):
            print("INFO: File exists")
            print("INFO: Checking content...")
            with open("your_output_file/basic_write_int.txt", "r") as of:
                if of.read()=="100":
                    print("INFO: simple_write_file() PASS w/ an integer. Congratulations!")
                    os.remove("your_output_file/basic_write_int.txt")
                    os.remove("your_output_file/basic_write_int_test.txt")
                    return True
                else:
                    print("INFO: simple_write_file() failed due to non-empty file")
                    os.remove("your_output_file/basic_write_int_test.txt")
                    os.remove("your_output_file/basic_write_int.txt")
                    return False
        else:
            print("INFO: Failed due to file does not exist")
            return False
def check_float_write_file():
    if os.path.exists("your_output_file/basic_write_float.txt"):
        os.remove("your_output_file/basic_write_float.txt")
    if simple_write_file("your_output_file/basic_write_float_test.txt",3.3)=="not_implemented_yet":
        print("INFO: simple_write_file() is failed because it is not implemented.")
        if os.path.exists("your_output_file/basic_write_float_test.txt"):
            os.remove("your_output_file/basic_write_float_test.txt")
        return False
    else:
        print("INFO: Testing simple_write_file() with a float number")
        try:
            simple_write_file("your_output_file/basic_write_float.txt",2.2)
        except:
            print("INFO: simple_write_file() is failed due to type error")
            os.remove("your_output_file/basic_write_float.txt")
            os.remove("your_output_file/basic_write_float_test.txt")
            return False
        if os.path.exists("your_output_file/basic_write_float.txt"):
            print("INFO: File exists")
            print("INFO: Checking content...")
            with open("your_output_file/basic_write_float.txt", "r") as of:
                if of.read()=="2.2":
                    print("INFO: simple_write_file() PASS w/ a float. Congratulations!")
                    os.remove("your_output_file/basic_write_float.txt")
                    os.remove("your_output_file/basic_write_float_test.txt")
                    return True
                else:
                    print("INFO: simple_write_file() failed due to incorrect file")
                    os.remove("your_output_file/basic_write_float_test.txt")
                    os.remove("your_output_file/basic_write_float.txt")
                    return False
        else:
            print("INFO: Failed due to file does not exist")
            return False
def check_reverse_a_list():
    test=[]
    original=[]
    for x in range(1,12):
        test.append(x)
        original.append(x)
    #print("original",original,original.reverse())
    reverse_a_list(test)
    original.reverse()
    if original == test:
        print("INFO: List is correctly reversed. Congratulations! You passed this test.")
        return True
    else:
        print("INFO: List did NOT reversed properly")
        return False

def basic_write_file_all():
    case1=check_basic_write_file()
    print()
    case2=check_basic_write_file_str()
    print()
    case3=check_int_write_file()
    print()
    case4=check_float_write_file()
    if case1 and case2 and case3 and case4:
        print()
        print("INFO: You passed all sub tests of simple_write_file()")
        print()
def driver():
    basic_write_file_all()
    print()
    check_reverse_a_list()
driver()