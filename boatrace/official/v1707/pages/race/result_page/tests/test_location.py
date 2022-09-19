from datetime import date

from boatrace.models import StadiumTelCode
from boatrace.official.v1707.pages.race.result_page.location import (
    create_race_result_page_url,
)


def test_create_race_result_page_url():
    assert (
        create_race_result_page_url(
            race_holding_date=date(2022, 9, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=12,
        )
        == "https://boatrace.jp/owpc/pc/race/raceresult?rno=12&jcd=04&hd=20220919"
    )
