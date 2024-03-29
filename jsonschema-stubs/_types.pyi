# Stubs for jsonschema._types (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def is_array(checker: Any, instance: Any): ...
def is_bool(checker: Any, instance: Any): ...
def is_integer(checker: Any, instance: Any): ...
def is_null(checker: Any, instance: Any): ...
def is_number(checker: Any, instance: Any): ...
def is_object(checker: Any, instance: Any): ...
def is_string(checker: Any, instance: Any): ...
def is_any(checker: Any, instance: Any): ...

class TypeChecker:
    def is_type(self, instance: Any, type: Any): ...
    def redefine(self, type: Any, fn: Any): ...
    def redefine_many(self, definitions: Any = ...): ...
    def remove(self, *types: Any): ...
    def __init__(self, type_checkers: Any) -> None: ...
    def __ne__(self, other: Any) -> None: ...
    def __eq__(self, other: Any) -> None: ...
    def __lt__(self, other: Any) -> None: ...
    def __le__(self, other: Any) -> None: ...
    def __gt__(self, other: Any) -> None: ...
    def __ge__(self, other: Any) -> None: ...

draft3_type_checker: Any
draft4_type_checker: Any
draft6_type_checker: Any
draft7_type_checker = draft6_type_checker
