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
import numpy as np


#@patch.object(Greengraph, 'location_sequence')
#@patch.object(Map, 'count_green')
def test_map_constructor():
    mock_image= open(os.path.join(os.path.dirname(__file__),'fixtures','NY_2.png'),'rb') #as mock_imgfile:
    with patch.object(requests,'get',return_value=Mock(content=mock_image.read())) as mock_get:
        with patch.object(image,'imread') as mock_img:
            #default
            Map(40.7127837, -74.0059413) # New York
            #Longon Map(51.5073509,-0.1277583)
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
                #changing parameters
            Map(41.8781136, -87.6297982,satellite=False,zoom=15,size=(500,350),sensor=True) # New York
            mock_get.assert_called_with(
                "http://maps.googleapis.com/maps/api/staticmap?",
                params={
                    'sensor':'true',
                    'zoom':15,
                    'size':'500x350',
                    'center':'41.8781136,-87.6297982',
                    'style':'feature:all|element:labels|visibility:off',
                    #'maptype': 'satellite'
                    }
                )

def test_green():
    mock_image= open(os.path.join(os.path.dirname(__file__),'fixtures','NY_2.png'),'rb')
    fixture_green = np.load(os.path.join(os.path.dirname(__file__),'fixtures','ny_green.npy'))
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        testMap = Map(41.8781136, -87.6297982) # New York
        assert_equal(fixture_green.shape,testMap.green(threshold).shape)
        assert (testMap.green(threshold) == fixture_green).all() == True
        assert (testMap.green(1.5) == fixture_green).all() == False

def test_count_green():
    mock_image= open(os.path.join(os.path.dirname(__file__),'fixtures','NY_2.png'),'rb')
    fixture_green = np.load(os.path.join(os.path.dirname(__file__),'fixtures','ny_green.npy'))
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        testMap = Map(41.8781136, -87.6297982) # New York
        count_from_fixture=np.sum(fixture_green)
        assert (testMap.count_green() == count_from_fixture)
        assert (testMap.count_green(1.5) != count_from_fixture)