from numb3rs import validate

def test_ip():
    assert validate('10.10.10.2') == 'Valid IPv4'

def test_invalid():
    assert validate('not ip') == 'Invalid IPv4'
    assert validate('257.2.2.2') == 'Invalid IPv4'