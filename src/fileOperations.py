import re

# simple regex that match only the most basic python functions
function_start_regex = "(def.*:\n)"
function_end_regex = "(return.*\n)"


def find_next_function(data, start_index):
    """
    Searches for the next Python function in the given data string start_index 
    int and returns a tuple containing the function string,start position, 
    and end position.
    
    Args:
        data (str): The string to search for the next function.
        start_index (int): The index in the full string
    
    Returns:
        tuple: A tuple containing:
             (function string, start position, end position) 
        Returns -1 if no function was found.
    """
    function_start = re.search(function_start_regex, data)
    function_end = re.search(function_end_regex, data)

    if (function_start == None or function_end == None):
        return -1

    function_start = function_start.span()
    function_end = function_end.span()

    fn_str = data[function_start[0]:function_end[1]]

    return (fn_str, function_start[1] + start_index, function_end[1] + start_index)


def find_all_functions(file_name): 
    """
    Searches for all Python functions in the file with the given file name 
    and returns a list of tuples containing the function strings, start 
    positions, and end positions.
    
    Args:
        file_name (str): The name of the file to search for Python functions.
    
    Returns:
        list: A list of tuples containing the function strings, start positions, 
        and end positions. Returns an empty list if no functions were found.
    """
    functions_to_document = []
    
    # add error handling for file open
    with open(file_name, 'r') as file:
        data = file.read()

        start_index = 0

        while (True):
            next_function = find_next_function(data[start_index:], start_index)
            if (next_function == -1):
                break
            functions_to_document.append(next_function)
            start_index += next_function[2]

    return functions_to_document


def format_generated_documentation(documentation):
    """
    Extracts the documentation string enclosed in triple quotes from a given string.

    Args:
        documentation (str): A string containing the documentation to extract.

    Returns:
        str: The extracted documentation string, or an empty string if no documentation string is found.
    """
    documentation_start = re.search("[\"']{3}", documentation)

    # needs actual error handling 
    if (documentation_start == None):
        return ""

    documentation_start = documentation_start.span()

    documentation_end = re.search("[\"']{3}", documentation[documentation_start[1]:])

    if (documentation_end == None):
        return ""

    documentation_end = documentation_end.span()

    return "    "+documentation[documentation_start[0]:documentation_start[1]+documentation_end[1]].replace("\n", "\n    ")+"\n"


def insert_documentation(file_name, documentation_to_insert):
    with open(file_name, 'r') as file:
        data = file.read()

        for documentation in reversed(documentation_to_insert):
            data = data[:documentation[1]]+documentation[0]+data[documentation[1]:]

    with open(file_name, 'w') as file:
        file.write(data)
    
    return 1
