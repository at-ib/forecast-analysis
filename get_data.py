from get_metoffice_forecast import get_metoffice_weston
from scrape_bay_cafe import scrape_bay_cafe_weston
from scrape_xc import scrape_xc_weston


def get_data_weston():
    scrape_bay_cafe_weston()
    scrape_xc_weston()
    get_metoffice_weston()


if __name__ == "__main__":
    get_data_weston()