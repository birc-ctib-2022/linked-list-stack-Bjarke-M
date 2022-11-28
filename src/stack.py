"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class EmptyStack(Exception):
    pass

@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.stack = []

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        self.stack.append(x)

    def top(self) -> T:
        """Return the top of the stack."""
        if self.is_empty():
            raise(EmptyStack)
        else:
            return self.stack[-1]


    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        if self.is_empty():
            raise(EmptyStack)
        else:
            self.stack.pop()

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        return len(self.stack)==0



is_stack = Stack()

is_stack.push(1)

is_stack.push(2)

is_stack.push(3)

is_stack.pop()

print(is_stack.top())