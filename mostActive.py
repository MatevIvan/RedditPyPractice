def most_active(bio_data):
    """
    Find window of time when most authors were active.

    One really direct approach is to go through every year (from 1900 to 1999) and see how many active people there were, 
    then find the largest number and see which consecutive years had that number
    """
    """
    Input: List of Tuples
    Output: Tuple
    """

    startYear = 0
    endYear = 0
    activePeriod = False
    largestConcurrentAuthors = 0

    # This list will hold the 
    data = []
    for i in range(1900,2000):
        # reset activeAuthors for every itteration
        activeAuthors = 0
        # k variable is to help index the data list
        k = i - 1900
        for j in range(len(bio_data)):
            # if the author is within the year (i) add to the total activeAuthors
            if i >= bio_data[j][1] and i <= bio_data[j][2]:
                activeAuthors += 1
        # append data list after going through bio_data list
        data.append(activeAuthors)

        # k > 0 avoids index out of range errors 
        if k > 0:
            # set the start year if the value for current year is greater than the value for last year
            # and this year's activeAuthors is greater than the recorded largestConcurrentAuthors
            if data[k] > data[k-1] and activeAuthors > largestConcurrentAuthors:
                startYear = i
                largestConcurrentAuthors = activeAuthors
                activePeriod = True
            # set the end year if the value for the current year is less than the value for the previous year
            # and we are in an activePeriod
            if data[k] < data[k-1] and activePeriod:
                endYear = i - 1
                activePeriod = False
    # return the tuple
    return (startYear,endYear)

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