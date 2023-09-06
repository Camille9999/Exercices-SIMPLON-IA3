import streamlit as st
import os

def main():
    st.title("Function Testing Exercise")

    # Display exercise statement
    exercise_statement = """
    In this little assignment you need to create a function "maxmin" that, given a string of space separated numbers, returns the highest and lowest number.

    Examples\n
        maxmin("1 2 3 4 5")  # return "5 1"
        maxmin("1 2 -3 4 5") # return "5 -3"
        maxmin("1 9 3 4 -5") # return "9 -5"

    Notes\n
    All numbers are valid Int32, no need to validate them.\n
    There will always be at least one number in the input string.\n
    Output string must be two numbers separated by a single space, and highest number is first.
    """
    st.markdown(exercise_statement)

    # Text editor for input function
    input_function = st.text_area("Enter your function here:", height=200)

    # Button to run tests
    if st.button("Run Tests"):
        # Save the input function to exercice.py
        with open("exercice.py", "w") as f:
            f.write(input_function)

        # Run tests using pytest and capture output
        result = os.system("pytest tests.py > results.txt")

        # Display test results
        st.write("Tests completed. Check results.txt for details.")
        if result == 0:
            st.success("All tests passed!")
        else:
            st.error("Some tests failed. Check results.txt for details.")

if __name__ == "__main__":
    main()
