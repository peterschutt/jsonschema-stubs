# Stubs for jsonschema.tests.test_cli (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from unittest import TestCase

def fake_validator(*errors: Any): ...

class TestParser(TestCase):
    FakeValidator: Any = ...
    instance_file: str = ...
    schema_file: str = ...
    def setUp(self) -> None: ...
    def fake_open(self, path: Any): ...
    def test_find_validator_by_fully_qualified_object_name(self) -> None: ...
    def test_find_validator_in_jsonschema(self) -> None: ...

class TestCLI(TestCase):
    def test_draft3_schema_draft4_validator(self) -> None: ...
    def test_successful_validation(self) -> None: ...
    def test_unsuccessful_validation(self) -> None: ...
    def test_unsuccessful_validation_multiple_instances(self) -> None: ...
    def test_version(self) -> None: ...
