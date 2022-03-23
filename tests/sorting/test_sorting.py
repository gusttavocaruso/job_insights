import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    fake_jobs = [
        {'min_salary': 2, 'max_salary': 20, 'date_posted': '2011-01-01'},
        {'min_salary': 1, 'max_salary': 10, 'date_posted': '2010-01-01'},
        {'min_salary': 4, 'max_salary': 40, 'date_posted': '2013-01-01'},
        {'min_salary': 3, 'max_salary': 30, 'date_posted': '2012-01-01'},
    ]

    expected_min = [
        {'min_salary': 1, 'max_salary': 10, 'date_posted': '2010-01-01'},
        {'min_salary': 2, 'max_salary': 20, 'date_posted': '2011-01-01'},
        {'min_salary': 3, 'max_salary': 30, 'date_posted': '2012-01-01'},
        {'min_salary': 4, 'max_salary': 40, 'date_posted': '2013-01-01'},
    ]

    expected_max = [
        {'min_salary': 4, 'max_salary': 40, 'date_posted': '2013-01-01'},
        {'min_salary': 3, 'max_salary': 30, 'date_posted': '2012-01-01'},
        {'min_salary': 2, 'max_salary': 20, 'date_posted': '2011-01-01'},
        {'min_salary': 1, 'max_salary': 10, 'date_posted': '2010-01-01'},
    ]

    expected_date = [
        {'min_salary': 4, 'max_salary': 40, 'date_posted': '2013-01-01'},
        {'min_salary': 3, 'max_salary': 30, 'date_posted': '2012-01-01'},
        {'min_salary': 2, 'max_salary': 20, 'date_posted': '2011-01-01'},
        {'min_salary': 1, 'max_salary': 10, 'date_posted': '2010-01-01'},
    ]

    sort_by(fake_jobs, 'min_salary')
    assert fake_jobs == expected_min

    sort_by(fake_jobs, 'max_salary')
    assert fake_jobs == expected_max

    sort_by(fake_jobs, 'date_posted')
    assert fake_jobs == expected_date

    with pytest.raises(ValueError):
        sort_by(fake_jobs, 'wrong')
