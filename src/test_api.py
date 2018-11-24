import pytest
import api as service


@pytest.fixture
def api():
    return service.api


def test_monday(api):
    r = api.requests.get("/v1/monday/")
    assert r.json() == {'day_of_week': "Monday"}
