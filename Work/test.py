
us = [('united', 154), ('american', 91), ('world', 88), ('war', 59), ('country', 50), ('million', 38), ('america', 36), ('federal', 36), ('new', 35), ('population', 34), ('government', 27), ('north', 22), ('native', 22), ('among', 22), ('national', 21), ('century', 21), ('military', 21), ('one', 21), ('many', 21), ('led', 20)]
ca = [('canada', 248), ('canadian', 102), ('percent', 81), ('world', 45), ('country', 41), ('government', 41), ('united', 33), ('quebec', 32), ('federal', 30), ('french', 28), ('north', 27), ('act', 26), ('population', 25), ('war', 24), ('european', 23), ('american', 22), ('one', 22), ('official', 22), ('national', 21), ('new', 18)]

k = 20


def comparison(a,b,k):
    """returns the common words in the k most frequent words of each list of words"""
    common = []
    common_count = 0

    for n in range(k):
        word = a[n][0]

        for item in b:
            if word == item[0]:
                common.append(word)
                common_count +=1

    perc = common_count/k
    response = ( 
        f"""Matching Words are {common}, 
        {common_count} out of the {k} most frequent words match. ({perc:.2}%""")
            
    return response


print(comparison(us,ca,k))