def most_active(bio_data: list[tuple[str, int, int]]) -> tuple[int, int]:
    """
    Find window of time when most authors were active.
    Args:
        bio_data: list[tuple[str, int, int]]
    Returns:
        tuple[int, int]
    """

    start_year = 0
    end_year = 0
    active_period = False
    largest_concurrent_authors = 0

    current_data = 0
    past_data = 0
    for year in range(1900,2000):
        # reset active_authors for every itteration
        active_authors = 0
        for author in bio_data:
            # if the author is within the year add to the total active_authors
            if author[1] <= year <= author[2]:
                active_authors += 1
        # update current_data
        current_data = active_authors

        
        # set start_year if the value for current_data is greater than the value for past_data
        # and this year's active_authors is greater than the recorded largest_concurrent_authors
        if current_data > past_data and active_authors > largest_concurrent_authors:
            start_year = year
            largest_concurrent_authors = active_authors
            active_period = True
        # set end_year if the value for the current_data is less than the value for past_data
        # and we are in an active_period
        if current_data < past_data and active_period:
            end_year = year - 1
            active_period = False

        # update past_data for net itteration
        past_data = current_data
    # return the tuple
    return (start_year,end_year)

# Test the code
data = [
      ('Alice', 1901, 1950),
      ('Bob', 1920, 1960),
      ('Carol', 1908, 1945),
      ('Dave', 1951, 1960),
      ('Eve', 1955, 1985),
      ('Ivan', 1949, 1962),
   ] 

print(most_active(data))