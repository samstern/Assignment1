from ..greengraph import Greengraph
from ..map import Map
import geopy
from nose.tools import assert_equal, assert_almost_equal
import numpy.testing as np_test
from mock import Mock, patch
import requests
from matplotlib import image
import yaml
import os

#@patch.object(Greengraph, 'location_sequence')
#@patch.object(Map, 'count_green')
def test_map_constructor():
    with patch.object(requests,'get') as mock_get:
        with patch.object(image,'imread') as mock_img:
            #default
            Map(40.7127837, -74.0059413) # New York
            mock_get.assert_called_with(
            "http://maps.googleapis.com/maps/api/staticmap?",
            params={
                'sensor':'false',
                'zoom':10,
                'size':'400x400',
                'center':'40.7127837,-74.0059413',
                'style':'feature:all|element:labels|visibility:off',
                'maptype': 'satellite'
                }
            )