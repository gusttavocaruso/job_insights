from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_job_type = set()

    for job in jobs:
        if job['job_type'] != '':
            unique_job_type.add(job['job_type'])

    return list(unique_job_type)


def filter_by_job_type(jobs, job_type):
    job_filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            job_filtered.append(job)

    return job_filtered


def get_unique_industries(path):
    jobs = read(path)
    unique_industry_type = set()

    for job in jobs:
        if job['industry'] != '':
            unique_industry_type.add(job['industry'])

    return list(unique_industry_type)


def filter_by_industry(jobs, industry):
    ind_filtered = []
    for job in jobs:
        if job['industry'] == industry:
            ind_filtered.append(job)

    return ind_filtered


def get_max_salary(path):
    jobs = read(path)
    max_salaries = set()

    for job in jobs:
        max_cash = job['max_salary']

        if max_cash != '' and max_cash != 'invalid':
            max_salaries.add(int(max_cash))

    return max(max_salaries)


def get_min_salary(path):
    jobs = read(path)
    min_salaries = set()

    for job in jobs:
        min_cash = job['min_salary']

        if min_cash != '' and min_cash != 'invalid':
            min_salaries.add(int(min_cash))

    return min(min_salaries)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError

    min_cash = job['min_salary']
    max_cash = job['max_salary']

    if (type(min_cash) is not int) or (type(max_cash) is not int):
        raise ValueError
    elif (type(salary) is not int) or (min_cash > max_cash):
        raise ValueError
    elif min_cash <= salary <= max_cash:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
