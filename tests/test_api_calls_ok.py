# very basic unittests, just if methods are returning what they should if everything is ok

import pytest

from pandas.core.frame import DataFrame

from apitalker.api import API, ApiResponse
from apitalker.data import Data

# not in repo
from tests.auth import API_KEY


@pytest.fixture(
    params=["/coi/rizikove-weby", "/cnb.cz/smenarny"],
    ids=["/coi/rizikove-weby", "/cnb.cz/smenarny"],
)
def valid_resource(request):
    return request.param


class TestWorkingApiCalls:
    api = API(API_KEY)

    def test_query(self, valid_resource):
        r = self.api.query(valid_resource)

        assert isinstance(r, ApiResponse) is True

    def test_get_data_no_params(self, valid_resource):
        data, error = self.api.get_data(valid_resource, sleep=0.1)

        assert error is None
        assert isinstance(data, Data) is True
        assert isinstance(data.as_dataframe, DataFrame) is True
        assert len(data.as_list) > 0
        assert all([isinstance(item, dict) for item in data.as_list]) is True

    def test_get_data_params_set_01(self, valid_resource):
        data, error = self.api.get_data(
            valid_resource, limit=10, skip=30, order='"id ASC"', sleep=0.1,
        )

        assert error is None
        assert isinstance(data, Data) is True
        assert isinstance(data.as_dataframe, DataFrame) is True
        assert len(data.as_list) > 0
        assert all([isinstance(item, dict) for item in data.as_list]) is True
