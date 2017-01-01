from ..greengraph import Greengraph
import geopy
from nose.tools import assert_equal, assert_almost_equal
import numpy.testing as np_test
from mock import Mock, patch
import yaml
import os

def test_graph_construct():
    #test whether the domain is correct
    #test whether the start and end strings passed as the correc parameters
    with open(os.path.join(os.path.dirname(__file__),'fixtures','location_pairs.yaml')) as location_pairs:
        pairs=yaml.load(location_pairs)
        for pair in pairs:
            temp_graph = Greengraph(**pair)
            assert_equal(temp_graph.geocoder.domain, 'maps.google.co.uk')
            assert_equal(temp_graph.start, pair['start'])
            assert_equal(temp_graph.end, pair['end'])

def test_geolocate():
    #test whether how geolocate is calling geopy
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mockgeocode:
        with open(os.path.join(os.path.dirname(__file__),'fixtures','location_pairs.yaml')) as location_pairs:
            pairs=yaml.load(location_pairs)
            for pair in pairs:
                testGreengraph = Greengraph(**pair)
                testGreengraph.geolocate(pair['start'])
                mockgeocode.assert_called_with(pair['start'], exactly_one=False)
                testGreengraph.geolocate(pair['end'])
                mockgeocode.assert_called_with(pair['end'], exactly_one=False)


def test_location_sequence():
    sequence=Greengraph.location_sequence(Greengraph("New York","Chicago"), (0,0),(20,20),5)
    np_test.assert_equal(sequence[0],(0,0))
    np_test.assert_equal(sequence[1],(5.0,5.0))
    np_test.assert_equal(sequence[2],(10.0,10.0))
    np_test.assert_equal(sequence[-1],(20.0,20.0))



def test_green_between():
    pass