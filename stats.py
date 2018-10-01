"""
Collect statistics after simulation
"""


def yearly_collection_stats(collection, years, status):
    """
    :param collection: list
        population result after simulation
    :param years: list
        years to collect the statistics for
    :param status: list
        list of health status to collect the statistics for
    :return: dict
        [st] is the key; the item is another dict
        with year as the key
        each value is the total population for that status for
        every year in the list
    """
    stat = dict()
    for st in status:
        stat[st] = dict()

    for st in status:
        year_states = dict()
        for year in years:
            year_states[year] = 0

        for year in years:

            for col in collection:
                if col.get_health_status(year) == st:
                    year_states[year] += 1

        stat[st] = year_states

    return stat


def accumulate_collection_stats(collections, years, status):
    """
    :param collection: list
        population result after running simulation for multiple times
    :param years: list
        years to collect the statistics for
    :param status: list
        list of health status to collect the statistics for
    :return: dict
        [st] is the key; the item is another dict
        with year as the key
        each value is the total population for that status for
        every year in the list
    """

    collective_stats = dict()

    for st in status:
        year_states = dict()
        for year in years:
            year_states[year] = [0]
        collective_stats[st] = year_states

    for collection in collections:

        run_stat = yearly_collection_stats(collection, years, status)

        for st in status:
            year_states = run_stat[st]
            for year in years:
                collective_stats[st][year].append(year_states[year])

    return collective_stats

