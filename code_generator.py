from typing import List, Union

from CodeBuilder import CodeBuilder, CodeTemplate

def generate_function(name: str, arguments: str, body: Union[str, CodeBuilder]) -> str:
    """
    Generate a Python function definition with support for complex bodies.

    Args:
        name (str): The name of the function.
        arguments (str): The arguments of the function.
        body (Union[str, CodeBuilder]): The body of the function.
            It can be either a string or a CodeBuilder object.

    Returns:
        str: The generated Python function definition.
    """
    builder = CodeBuilder()
    builder.add_line(f"def {name}({arguments}):")
    if isinstance(body, str):
        builder.indent()
        builder.add_line(body)
        builder.dedent()
    elif isinstance(body, CodeBuilder):
        builder.indent()
        builder.add_code(body)
        builder.dedent()
    else:
        raise TypeError("Body for function should be string or CodeBuilder")
    return builder.get_code()

def generate_class(name: str, attributes: List[str], methods: List[CodeBuilder]) -> str:
    """
    Generate a Python class definition with attributes and methods.

    Args:
        name (str): The name of the class.
        attributes (List[str]): The attributes of the class.
        methods (List[CodeBuilder]): The methods of the class as CodeBuilder objects.

    Returns:
        str: The generated Python class definition.
    """
    builder = CodeBuilder()
    builder.add_line(f"class {name}:")
    builder.indent()
    for attribute in attributes:
        builder.add_line(f"    {attribute}")
    for method in methods:
        builder.add_code(method)
    builder.dedent()
    return builder.get_code()
    
