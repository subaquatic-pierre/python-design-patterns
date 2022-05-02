from structural.decorator import hello_world


def test_adds_text():
    """It adds DECORATED to end of text"""
    val = hello_world()

    assert val == "Hello, World! DECORATED"


def test_keepps_function_name():
    """Orginal function keeps its name"""
    assert hello_world.__name__ == "hello_world"


def test_doc_string():
    """It keeps original docstring"""
    assert hello_world.__doc__ == "Original Function!"
