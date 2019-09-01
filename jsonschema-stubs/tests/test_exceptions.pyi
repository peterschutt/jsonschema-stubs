# Stubs for jsonschema.tests.test_exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from unittest import TestCase

class TestBestMatch(TestCase):
    def best_match(self, errors: Any): ...
    def test_shallower_errors_are_better_matches(self) -> None: ...
    def test_oneOf_and_anyOf_are_weak_matches(self) -> None: ...
    def test_if_the_most_relevant_error_is_anyOf_it_is_traversed(self) -> None: ...
    def test_if_the_most_relevant_error_is_oneOf_it_is_traversed(self) -> None: ...
    def test_if_the_most_relevant_error_is_allOf_it_is_traversed(self) -> None: ...
    def test_nested_context_for_oneOf(self) -> None: ...
    def test_one_error(self) -> None: ...
    def test_no_errors(self) -> None: ...

class TestByRelevance(TestCase):
    def test_short_paths_are_better_matches(self) -> None: ...
    def test_global_errors_are_even_better_matches(self) -> None: ...
    def test_weak_validators_are_lower_priority(self) -> None: ...
    def test_strong_validators_are_higher_priority(self) -> None: ...

class TestErrorTree(TestCase):
    def test_it_knows_how_many_total_errors_it_contains(self) -> None: ...
    def test_it_contains_an_item_if_the_item_had_an_error(self) -> None: ...
    def test_it_does_not_contain_an_item_if_the_item_had_no_error(self) -> None: ...
    def test_validators_that_failed_appear_in_errors_dict(self) -> None: ...
    def test_it_creates_a_child_tree_for_each_nested_path(self) -> None: ...
    def test_children_have_their_errors_dicts_built(self) -> None: ...
    def test_multiple_errors_with_instance(self) -> None: ...
    def test_it_does_not_contain_subtrees_that_are_not_in_the_instance(self) -> None: ...
    def test_if_its_in_the_tree_anyhow_it_does_not_raise_an_error(self) -> None: ...

class TestErrorInitReprStr(TestCase):
    def make_error(self, **kwargs: Any): ...
    def assertShows(self, expected: Any, **kwargs: Any) -> None: ...
    def test_it_calls_super_and_sets_args(self) -> None: ...
    def test_repr(self) -> None: ...
    def test_unset_error(self) -> None: ...
    def test_empty_paths(self) -> None: ...
    def test_one_item_paths(self) -> None: ...
    def test_multiple_item_paths(self) -> None: ...
    def test_uses_pprint(self) -> None: ...
    def test_str_works_with_instances_having_overriden_eq_operator(self) -> None: ...

class TestHashable(TestCase):
    def test_hashable(self) -> None: ...