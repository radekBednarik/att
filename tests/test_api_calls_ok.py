# very basic unittests, just if methods are returning what they should if everything is ok

import pytest

from apitalker.api import API, ApiResponse

# not in repo
from tests.auth import API_KEY


@pytest.fixture(
    params=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
    ids=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
)
def valid_single_resource(request):
    api = API(API_KEY)
    return api.query(request.param)


@pytest.fixture(
    params=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
    ids=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
)
def valid_whole_resource(request):
    api = API(API_KEY)
    return api.get_all(request.param)


class TestWorkingApiCalls:
    def test_query(self, valid_single_resource):
        assert isinstance(valid_single_resource, ApiResponse) is True

    def test_get_all_data(self, valid_whole_resource):
        assert isinstance(valid_whole_resource, list) is True
        assert len(valid_whole_resource) > 0
        assert all([isinstance(item, dict) for item in valid_whole_resource]) is True
