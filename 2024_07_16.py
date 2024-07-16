# import timeit
#
# setup = '''
# from math import sqrt
# def func():
#     return [sqrt(x) for x in range(100)]
# '''
#
# stmt = 'func()'
#
# print(timeit.timeit(stmt=stmt, setup=setup, number=100000))

# todo
#   task 1
#   napíš funkciu, ktorá vráti súťet arr na základe indexov v liste queries.
#   result = [15, 16, 31, 5]

arr = [2, 8, 5, 0, 3, 3, 10]

queries = [
    (0, 2),
    (3, 6),
    (0, 6),
    (2, 2)
    ]

def renge_sum(arr, queries):
    results = []
    for start_index, end_index in queries:
        results.append(sum(arr[start_index:end_index+1]))
    return results

result = renge_sum(arr, queries)
print(result)