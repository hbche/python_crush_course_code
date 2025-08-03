from city_functions import get_city_country_population

def test_city_country():
    """能正确处理像 Santiago, Chile 这种场景吗"""

    city_country = get_city_country_population('santiago', 'chile', 5_000_000)
    assert city_country == 'Santiago, Chile-population=5000000'