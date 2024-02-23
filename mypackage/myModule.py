def top_n(items, n):
    """Returns the top n items in an array in descending order.

    Args:
        items (array): list or array-like object
        n (int): number of items to return

    Return:
        array: top n items in desc order

    Egs:
        >>> top_n([6,3,8,1,5], 3)
            [8,6,5]
    """
    for i in range(n):  # keep sorting untill we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j]  # swap the two
    
    # get last 2 items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]