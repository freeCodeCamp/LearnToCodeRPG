from datetime import date, timedelta

import pytest

from supermemo2 import SMTwo, year_mon_day, mon_day_year, day_mon_year


@pytest.mark.parametrize(
    "quality, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, 1.7000000000000002, 1, 0, date.today() + timedelta(days=1)),
        (1, 1.96, 1, 0, date.today() + timedelta(days=1)),
        (2, 2.1799999999999997, 1, 0, date.today() + timedelta(days=1)),
        (3, 2.36, 1, 1, date.today() + timedelta(days=1)),
        (4, 2.5, 1, 1, date.today() + timedelta(days=1)),
        (5, 2.6, 1, 1, date.today() + timedelta(days=1)),
    ],
)
def test_first_review(
    quality,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):

    reviewed = SMTwo.first_review(quality)

    assert reviewed.easiness == expected_easiness
    assert reviewed.interval == expected_interval
    assert reviewed.repetitions == expected_repetitions
    assert reviewed.review_date == expected_review_date


@pytest.mark.parametrize(
    "quality, review_date, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, date.today(), 1.7000000000000002, 1, 0, date.today() + timedelta(days=1)),
        (1, date.today(), 1.96, 1, 0, date.today() + timedelta(days=1)),
        (2, date.today(), 2.1799999999999997, 1, 0, date.today() + timedelta(days=1)),
        (3, date.today(), 2.36, 1, 1, date.today() + timedelta(days=1)),
        (4, date.today(), 2.5, 1, 1, date.today() + timedelta(days=1)),
        (5, date.today(), 2.6, 1, 1, date.today() + timedelta(days=1)),
    ],
)
def test_first_review_given_date(
    quality,
    review_date,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    reviewed = SMTwo.first_review(quality, review_date)

    assert reviewed.easiness == expected_easiness
    assert reviewed.interval == expected_interval
    assert reviewed.repetitions == expected_repetitions
    assert reviewed.review_date == expected_review_date


@pytest.mark.parametrize(
    "str_date, date_fmt",
    [
        ("2021-12-01", None),
        ("2021-12-01", year_mon_day),
        ("12-01-2021", mon_day_year),
        ("01-12-2021", day_mon_year),
    ],
)
def test_first_review_given_date_in_str(str_date, date_fmt):
    reviewed = SMTwo.first_review(3, str_date, date_fmt)

    assert reviewed.easiness == 2.36
    assert reviewed.interval == 1
    assert reviewed.repetitions == 1
    assert reviewed.review_date == date(2021, 12, 1) + timedelta(days=1)


@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, 2.3, 12, 3, 1.5, 1, 0, date.today() + timedelta(days=1)),
        (1, 2.3, 12, 3, 1.7599999999999998, 1, 0, date.today() + timedelta(days=1)),
        (2, 2.3, 12, 3, 1.9799999999999998, 1, 0, date.today() + timedelta(days=1)),
        (3, 2.3, 12, 3, 2.1599999999999997, 28, 4, date.today() + timedelta(days=28)),
        (4, 2.3, 12, 3, 2.3, 28, 4, date.today() + timedelta(days=28)),
        (5, 2.3, 12, 3, 2.4, 28, 4, date.today() + timedelta(days=28)),
    ],
)
def test_review(
    quality,
    easiness,
    interval,
    repetitions,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    sm = SMTwo(easiness, interval, repetitions)
    reviewed = sm.review(quality)

    assert reviewed.easiness == expected_easiness
    assert reviewed.interval == expected_interval
    assert reviewed.repetitions == expected_repetitions
    assert reviewed.review_date == expected_review_date


@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, review_date, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (
            0,
            2.3,
            12,
            3,
            date.today(),
            1.5,
            1,
            0,
            date.today() + timedelta(days=1),
        ),
        (
            1,
            2.3,
            12,
            3,
            date.today(),
            1.7599999999999998,
            1,
            0,
            date.today() + timedelta(days=1),
        ),
        (
            2,
            2.3,
            12,
            3,
            date.today(),
            1.9799999999999998,
            1,
            0,
            date.today() + timedelta(days=1),
        ),
        (
            3,
            2.3,
            12,
            3,
            date.today(),
            2.1599999999999997,
            28,
            4,
            date.today() + timedelta(days=28),
        ),
        (
            4,
            2.3,
            12,
            3,
            date.today(),
            2.3,
            28,
            4,
            date.today() + timedelta(days=28),
        ),
        (5, 2.3, 12, 3, date.today(), 2.4, 28, 4, date.today() + timedelta(days=28)),
        # test case for when easiness drops lower than 1.3
        (0, 1.3, 12, 3, date.today(), 1.3, 1, 0, date.today() + timedelta(days=1)),
        # test case for for repetitions equals to 2
        (4, 2.5, 1, 1, date.today(), 2.5, 6, 2, date.today() + timedelta(days=6)),
    ],
)
def test_review_given_date(
    quality,
    easiness,
    interval,
    repetitions,
    review_date,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    sm = SMTwo(easiness, interval, repetitions)
    reviewed = sm.review(quality, review_date)

    assert reviewed.easiness == expected_easiness
    assert reviewed.interval == expected_interval
    assert reviewed.repetitions == expected_repetitions
    assert reviewed.review_date == expected_review_date
