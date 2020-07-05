import pytest

from apitalker.api import API, ApiResponse
# not in repo
from tests.auth import API_KEY


@pytest.fixture(
    params=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
    ids=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
)
def valid_resource(request):
    api = API(API_KEY)
    return api.query(request.param)


class TestWorkingApiCalls:
    def test_call_without_filters(self, valid_resource):
        assert isinstance(valid_resource, ApiResponse) is True
