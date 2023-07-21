from filters.views import (
    FilteredBrochureDataAPIView,
)
from filters.constants import *


def initialize_filters_api_urls(api) -> None:
    """
        This method initialize the filters API URLs. 
        Parameters
        ----------
            api

        Returns
        -------
            None
    """

    api.add_resource(FilteredBrochureDataAPIView, FILTER_BROCHURE_DATA_API_URL)
