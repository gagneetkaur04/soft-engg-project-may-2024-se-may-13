from app.models import ProgrammingAssignment, TestCase
from app import db

def insert_default_programming_assignments():
    assignment1 = ProgrammingAssignment(
        course_id='CS1002',
        title='Sort a List of Integers',
        description="Write a Python function that takes a list of integers as input and returns the sorted list in ascending order.\n \nInstructions:\n- Your function should work for lists of any length, including empty lists. \n- Make sure to name your function 'main' to allow test case execution.\n    \nExamples:\n- `main([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])` should return `[1, 1, 2, 3, 3, 4, 5, 5, 6, 9]`\n- `main([])` should return `[]`\n- `main([1])` should return `[1]`",
    )

    assignment2 = ProgrammingAssignment(
        course_id='CS1002',
        title='Calculate Factorial of a Number',
        description="Given a number n,  you need to return its factorial.\n\nTo obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely n! = n*(n-1)*(n-2) … 1.\n\nInstructions:\n- the factorial of 0 is 1, factorial(0) = 1.\n- factorial is only defined for positive numbers.\n- for negative inputs, you need to return -1 indicating the factorial does not exist.\n- Make sure to name your function 'main' to allow for test case evaluation.\n\nExamples:\n- `main(0)` should return `1`\n- `main(4)` should return `24`\n- `main(7)` should return `5040`\n",
    )

    assignment3 = ProgrammingAssignment(
        course_id='CS1002',
        title='Check if a Number is Prime',
        description="Write a Python function that takes a number as input and returns True if the number is prime, and False otherwise.\n\nInstructions:\n- The input number will be a positive integer.\n- Make sure to name your function 'main' to allow for test case execution.\n\nExamples:\n- `main(2)` should return `True`\n- `main(4)` should return `False`\n- `main(13)` should return `True`\n",
    )

    assignment4 = ProgrammingAssignment(
        course_id='CS1002',
        title='Largest Number in a List of Integers',
        description="Write a Python function that takes a list of integers as input and returns the largest number in the list.\n\nInstructions:\n- Your function should work for lists of any length, including empty lists.\n- Make sure to name your function 'main' to allow for test case execution.\n\nExamples:\n- `main([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])` should return `9`\n- `main([])` should return `None`\n- `main([1, 1, 1, 1, 1])` should return `1`\n- `main([5, 4, 3, 2, 1])` should return `5`\n",
    )

    db.session.add_all([assignment1, assignment2, assignment3, assignment4])
    db.session.commit()

    # Test Cases for Assignment 1
    test_case1 = TestCase(
        prog_assignment_id=assignment1.prog_assignment_id,
        input_data='[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]',
        expected_output='[1, 1, 2, 3, 3, 4, 5, 5, 6, 9]'
    )

    test_case2 = TestCase(
        prog_assignment_id=assignment1.prog_assignment_id,
        input_data='[]',
        expected_output='[]'
    )

    test_case3 = TestCase(
        prog_assignment_id=assignment1.prog_assignment_id,
        input_data='[1, 1, 1, 1, 1]',
        expected_output='[1, 1, 1, 1, 1]'
    )

    test_case4 = TestCase(
        prog_assignment_id=assignment1.prog_assignment_id,
        input_data='[5, 4, 3, 2, 1]',
        expected_output='[1, 2, 3, 4, 5]'
    )

    db.session.add_all([test_case1, test_case2, test_case3, test_case4])
    db.session.commit()

    # Test Cases for Assignment 2
    test_case1 = TestCase(
        prog_assignment_id=assignment2.prog_assignment_id,
        input_data='0',
        expected_output='1'
    )

    test_case2 = TestCase(
        prog_assignment_id=assignment2.prog_assignment_id,
        input_data='4',
        expected_output='24'
    )

    test_case3 = TestCase(
        prog_assignment_id=assignment2.prog_assignment_id,
        input_data='7',
        expected_output='5040'
    )

    test_case4 = TestCase(
        prog_assignment_id=assignment2.prog_assignment_id,
        input_data='-5',
        expected_output='-1'
    )

    db.session.add_all([test_case1, test_case2, test_case3, test_case4])
    db.session.commit()

    # Test Cases for Assignment 3
    test_case1 = TestCase(
        prog_assignment_id=assignment3.prog_assignment_id,
        input_data='2',
        expected_output='True'
    )

    test_case2 = TestCase(
        prog_assignment_id=assignment3.prog_assignment_id,
        input_data='4',
        expected_output='False'
    )

    test_case3 = TestCase(
        prog_assignment_id=assignment3.prog_assignment_id,
        input_data='13',
        expected_output='True'
    )

    test_case4 = TestCase(
        prog_assignment_id=assignment3.prog_assignment_id,
        input_data='1',
        expected_output='False'
    )

    db.session.add_all([test_case1, test_case2, test_case3, test_case4])
    db.session.commit()

    # Test Cases for Assignment 4
    test_case1 = TestCase(
        prog_assignment_id=assignment4.prog_assignment_id,
        input_data='[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]',
        expected_output='9'
    )

    test_case2 = TestCase(
        prog_assignment_id=assignment4.prog_assignment_id,
        input_data='[]',
        expected_output='None'
    )

    test_case3 = TestCase(
        prog_assignment_id=assignment4.prog_assignment_id,
        input_data='[1, 1, 1, 1, 1]',
        expected_output='1'
    )

    test_case4 = TestCase(
        prog_assignment_id=assignment4.prog_assignment_id,
        input_data='[5, 4, 3, 2, 1]',
        expected_output='5'
    )

    db.session.add_all([test_case1, test_case2, test_case3, test_case4])
    db.session.commit()

