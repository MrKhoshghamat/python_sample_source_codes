def get_statement():
    """
    This function gets a statement from user input
    :return: statement
    """
    statement = input("Please Enter a statement that you wanna "
                      "repeat : ")
    return statement


def get_counter():
    """
    This function gets counter from user input
    :return: counter
    """
    try:
        counter = int(input("please Enter a counter for repetition loop : "))
        return counter
    except ValueError:
        print("It's Invalid. Please Enter a valid integer number for "
              "counter")


def statement_repetition_process(statement, counter):
    """
    This function process the result for statement repetition
    :param statement: statement
    :param counter: counter
    :return: result
    """
    result = statement * counter
    return result


def statement_repetition():
    """
    This function print the result of statement repetition
    """
    statement_rep = get_statement()
    statement_counter = get_counter()
    statement_repetition_result = \
        statement_repetition_process(statement_rep,
                                     statement_counter)

    print(f"\nStatement is : {statement_rep}\n"
          f"Statement Counter is : {statement_counter}\n"
          f"Statement Repetition is about : {statement_repetition_result}")


if __name__ == "__main__":
    statement_repetition()
