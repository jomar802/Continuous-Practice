

def matchingStrings(strings, queries):

    # param
    # strings: list of elements
    # queries: list of queries looking for elements
    # Count how many instances of elements in queries appear in strings


    count_of_elements = []

    for q in range(0,len(queries)):
        count = 0

        for element in range(0,len(strings)):

            if queries[q] == strings[element]:
                count = count + 1
            
            if element == len(strings)-1:
                count_of_elements.append(count)

    return count_of_elements


strings = ['ab','ab','abc']
queries = ['ab','abc','bc']

matchingStrings(strings,queries)





