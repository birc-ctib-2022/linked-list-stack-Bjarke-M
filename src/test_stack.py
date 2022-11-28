"""Testing our stack implementation."""
from stack import EmptyStack, Stack
import pytest
def test_me() -> None:
    """You bet"""
    assert 40 + 2 == 42


def test_push() -> None:
    is_stack = Stack()
    is_stack.push(1)
    assert is_stack.is_empty() == False


def test_top() -> None:
    is_stack = Stack()
    is_stack.push(1)
    assert is_stack.top()==1


def test_pop() -> None:
    is_stack = Stack()
    is_stack.push(1)
    is_stack.pop()
    assert is_stack.is_empty()==True

def test_exception() -> None:
    is_stack = Stack()
    with pytest.raises(EmptyStack):
        is_stack.pop()
        is_stack.top()
    
