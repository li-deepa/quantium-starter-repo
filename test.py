import time
from new_pinkmorsels_visualize import dash_app

def test_header_exists(dash_duo):
    time.sleep(3)
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header",timeout=60)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    # dash_duo.wait_for_element("#visualization", )


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    # dash_duo.wait_for_element("#region_picker", )