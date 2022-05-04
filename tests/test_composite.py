from structural.composite import Composite, Child
from unittest.mock import patch


def setup_menu():
    top_menu = Composite("Top Menu")
    sub1 = Composite("Sub 1")
    sub2 = Composite("Sub 2")
    child1 = Child("Child 1")
    child2 = Child("Child 2")
    child3 = Child("Child 3")

    sub1.append_child(child1)
    sub1.append_child(child2)
    sub2.append_child(child3)

    top_menu.append_child(sub1)
    top_menu.append_child(sub2)

    return top_menu


@patch("builtins.print")
def test_all_children_called(mock_print):
    """It calls all children components in the tree"""
    menu = setup_menu()

    menu.component_function()

    assert mock_print.call_count == 6


@patch("builtins.print")
def test_append_child(mock_print):
    """It adds child to tree"""
    menu = setup_menu()
    child4 = Child("Child 4")
    menu.append_child(child4)

    menu.component_function()

    assert mock_print.call_count == 7


@patch("builtins.print")
def test_remove_child(mock_print):
    """It removes child from tree"""
    menu = setup_menu()
    child4 = Child("Child 4")
    menu.append_child(child4)

    menu.component_function()
    mock_print.call_count = 0

    menu.remove_child(child4)

    menu.component_function()

    assert mock_print.call_count == 6
