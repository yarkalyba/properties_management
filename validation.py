def get_valid_input(input_string, valid_options):
    """
    function is used for input validation
    :param input_string: str(string for user)
    :param valid_options: tuple(options that could be chousen
    :return: str(the result of an input)
    """

    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response
