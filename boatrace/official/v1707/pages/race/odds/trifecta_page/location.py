import urllib.parse
from datetime import date

from boatrace.models import StadiumTelCode
from boatrace.official.v1707 import BASE_URL
from boatrace.official.v1707.utils import (
    format_date_for_query_string,
    format_stadium_tel_code_for_query_string,
)


def create_odds_page_url(
    race_holding_date: date, stadium_tel_code: StadiumTelCode, race_number: int
):
    return f"{BASE_URL}/owpc/pc/race/odds3t?{urllib.parse.urlencode({'rno': race_number, 'jcd': format_stadium_tel_code_for_query_string(stadium_tel_code), 'hd': format_date_for_query_string(race_holding_date)})}"
