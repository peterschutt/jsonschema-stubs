# Stubs for jsonschema.tests.test_types (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from unittest import TestCase

def equals_2(checker: Any, instance: Any): ...
def is_namedtuple(instance: Any): ...
def is_object_or_named_tuple(checker: Any, instance: Any): ...
def coerce_named_tuple(fn: Any): ...

required: Any
properties: Any

class TestTypeChecker(TestCase):
    def test_is_type(self) -> None: ...
    def test_is_unknown_type(self) -> None: ...
    def test_checks_can_be_added_at_init(self) -> None: ...
    def test_redefine_existing_type(self) -> None: ...
    def test_remove(self) -> None: ...
    def test_remove_unknown_type(self) -> None: ...
    def test_redefine_many(self) -> None: ...
    def test_remove_multiple(self) -> None: ...
    def test_type_check_can_raise_key_error(self) -> None: ...

class TestCustomTypes(TestCase):
    def test_simple_type_can_be_extended(self): ...
    def test_object_can_be_extended(self) -> None: ...
    def test_object_extensions_require_custom_validators(self) -> None: ...
    def test_object_extensions_can_handle_custom_validators(self) -> None: ...
