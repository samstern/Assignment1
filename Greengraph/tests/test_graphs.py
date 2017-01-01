from ..greengraph import Greengraph
from nose.tools import assert_equal
from mock import Mock
import yaml
import os

def test_graph_construct():
    #test whether the domain is correct
    #test whether the start and end strings passed as the correc parameters
    with open(os.path.join(os.path.dirname(__file__),'fixtures','location_pairs.yaml')) as location_pairs:
        pairs=yaml.load(location_pairs)
        for pair in pairs:
            temp_graph=Greengraph(**pair)
            assert_equal(temp_graph.geocoder.domain, 'maps.google.co.uk')
            assert_equal(temp_graph.start, pair['start'])
            assert_equal(temp_graph.end, pair['end'])

def test_geolocate():
    pass

def test_location_sequence():
    pass
def test_green_between():
    pass