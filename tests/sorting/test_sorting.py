from src.sorting import sort_by


def test_sort_by_criteria():
    fake_criteria = 'min_salary'
    fake_jobs = [
        {'min_salary': 1, 'max_salary': 10},
        {'min_salary': 2, 'max_salary': 20},
        {'min_salary': 4, 'max_salary': 40},
        {'min_salary': 3, 'max_salary': 30},
    ]

    expected_jobs = [
        {'min_salary': 1, 'max_salary': 10},
        {'min_salary': 2, 'max_salary': 20},
        {'min_salary': 3, 'max_salary': 30},
        {'min_salary': 4, 'max_salary': 40},
    ]

    assert sort_by(fake_jobs, fake_criteria) == expected_jobs

    fake_criteria = 'wrong'
    assert sort_by(fake_jobs, fake_criteria) == ValueError
