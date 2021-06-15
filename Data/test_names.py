from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
  assert make_full_name('Erick', 'Saavedra') == 'Saavedra; Erick'
  assert make_full_name('Joshua', 'Ellinger') == 'Ellinger; Joshua'


def test_extract_family_name():
  assert extract_family_name('Saavedra; Erick') == 'Saavedra'
  assert extract_family_name('Ellinger; Joshua') == 'Ellinger'

def test_extract_given_name():
  assert extract_given_name('Saavedra; Erick') == 'Erick'
  assert extract_given_name('Ellinger; Joshua') == 'Joshua'

pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])