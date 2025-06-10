import pytest

from pylix.errors.decorator import TODO, to_test

def test_todo():
    @TODO
    def something():
        return "something"

    with pytest.warns(UserWarning, match="something - TODO: implementation pending."):
        assert something() == "something"

    @TODO("testo")
    def something_else():
        return "something_else"

    with pytest.warns(UserWarning, match="something_else - TODO: testo."):
        assert something_else() == "something_else"

def test_to_test():
    @to_test
    def something():
        return "something"

    with pytest.warns(UserWarning, match="something - to_test: testing pending."):
        assert something() == "something"

    @to_test("testo")
    def something_else():
        return "something_else"

    with pytest.warns(UserWarning, match="something_else - to_test: testo."):
        assert something_else() == "something_else"
