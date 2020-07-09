import pytest

from apitalker.api import API, ApiError
from apitalker.data import Data

# not in repo
from tests.auth import API_KEY


@pytest.fixture(
    params=["/czso.cz/lide-domy-byt", "/cnb.cz/smenarn"],
    ids=["/czso.cz/lide-domy-byty", "/cnb.cz/smenarny"],
)
def invalid_resource(request):
    return request.param


class TestNotWorkingApiCalls:
    api = API(API_KEY)

    def test_query(self, invalid_resource):
        r = self.api.query(invalid_resource)

        assert isinstance(r, ApiError) is True

    def test_get_data(self, invalid_resource):
        data, error = self.api.get_data(invalid_resource)

        assert isinstance(error, ApiError) is True
        assert isinstance(data, Data) is True
        assert len(data.as_list) == 0
