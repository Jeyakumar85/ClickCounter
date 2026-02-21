from typing import Callable

def greet():
    return "hello"

def shout(f: Callable[[], str]) -> str:
    return f() + "!!!!"

print(shout(greet))