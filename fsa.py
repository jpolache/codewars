def flatten_and_sort(array):
    my_array = []
    [my_array.extend(x) for x in array]
    print(sorted(my_array))
    #return []

flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]) #[1, 2, 3, 4, 5, 6, 100]