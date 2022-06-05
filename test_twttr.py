from twittr import shorten

def test_me():
    assert shorten('Craig Loo') == 'Crg L'
    assert shorten('good') == 'gd'
    assert shorten('abc') == 'abc'

