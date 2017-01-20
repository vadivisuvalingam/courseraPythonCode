def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    bus_capacity = 50
    result = (n - (n % bus_capacity)) // bus_capacity 
    return result + 1


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    last_number = 0
    current_number = 0
    price_increase = 0
    price_decrease = 0
    for i in price_changes:
        current_number = i
        diff = current_number - last_number
        if diff > 0:
            price_increase = price_increase + diff
        else:
            price_decrease = price_decrease + diff
        last_number = i
    return (price_increase, price_decrease)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    for i in range(0, k):
        temp = L[i]
        L[i] = L[len(L) - k - 1 + i]
        L[len(L) - k - 1 + i] = temp            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
