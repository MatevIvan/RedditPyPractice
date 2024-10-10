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

    currentData = 0
    pastData = 0
    for i in range(1900,2000):
        # reset activeAuthors for every itteration
        activeAuthors = 0
        for j in range(len(bio_data)):
            # if the author is within the year (i) add to the total activeAuthors
            if i >= bio_data[j][1] and i <= bio_data[j][2]:
                activeAuthors += 1
        # update currentData
        currentData = activeAuthors

        
        # set startYear if the value for currentData is greater than the value for pastData
        # and this year's activeAuthors is greater than the recorded largestConcurrentAuthors
        if currentData > pastData and activeAuthors > largestConcurrentAuthors:
            startYear = i
            largestConcurrentAuthors = activeAuthors
            activePeriod = True
        # set endYear if the value for the currentData is less than the value for pastData
        # and we are in an activePeriod
        if currentData < pastData and activePeriod:
            endYear = i - 1
            activePeriod = False

        # update pastData for net itteration
        pastData = currentData
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