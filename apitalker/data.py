from typing import Any, List

from pandas import DataFrame
from pandas.io.json import _json_normalize


class Data:
    """Class for handling data returned by using `apitalker.api.API.get_data()` method.
    """

    def __init__(self, data: List[Any]) -> None:
        """Initializes instance of the class.

        Args:
            data (List[Any]): data retrieved from Apitalks API data resource.
        
        Attributes:
            as_list (List[Any]): original data retrieved from Api resource
            as_dataframe (pandas.Dataframe): data as pandas' DataFrame object, converted using `pandas._json_normalize()`
        """
        self.as_list: List[Any] = data
        self.as_dataframe: DataFrame = self.to_dataframe()

    def to_dataframe(self) -> DataFrame:
        """Converts `apitalker.data.Data.as_list` attribute value to DataFrame and
        returns.

        Returns:
            DataFrame: converted API data to pandas DataFrame
        """
        return _json_normalize(self.as_list)