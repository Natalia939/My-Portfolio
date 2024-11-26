from seasons import calculate_minutes, convert_to_words
# Imports the date class, which is required to mock today's date during testing.
from datetime import date
from unittest.mock import patch


def test_calculate_minutes():
    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2000, 1, 1)
        mock_date.fromisoformat.side_effect = date.fromisoformat
        # Test with valid dates
        assert calculate_minutes("1999-01-01") == 525600
        assert calculate_minutes("1998-06-20") == 806400
        # Test with invalid date
        assert calculate_minutes("invalid-date") is None


def test_convert_to_words():
    # Test conversion of minutes to words
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(0) == "Zero"
    assert convert_to_words(806400) == "Eight hundred six thousand, four hundred"
