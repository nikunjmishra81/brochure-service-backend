from filters.urls import initialize_filters_api_urls


def initialize_api_routes(api) -> None:
    """
        This method initialize the all the API URLs. 
        Parameters
        ----------
            api

        Returns
        -------
            None
    """
    initialize_filters_api_urls(api)
