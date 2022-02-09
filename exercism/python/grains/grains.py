def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    else:
        return 1 << number - 1


def total(squares=64):
    ### ITERATION 1 ###
    # each_square_grains = [2 ** (x - 1) for x in range(1, squares + 1)]
    # return sum(each_square_grains)
    # TEST:
    # 128 squares took: 0.0 seconds
    # 256 squares took: 0.0 seconds
    # 512 squares took: 0.0009968280792236328 seconds
    # 1024 squares took: 0.0010132789611816406 seconds
    # 65536 squares took: 6.098200559616089 seconds
    # 131072 squares took: 26.521271228790283 seconds
    # 262144 squares took: 116.17688250541687 seconds

    ### ITERATION 3 ###
    # trying to improve performance
    # sum_of_grains = 1
    # last_square = 1
    # if 1 == squares:
    #     return 1
    #
    # for x in range(2, squares + 1):
    #     sum_of_grains += last_square * 2
    #     last_square *= 2
    # return sum_of_grains
    # TEST:
    # 128 squares took: 0.0 seconds
    # 256 squares took: 0.0 seconds
    # 512 squares took: 0.0 seconds
    # 1024 squares took: 0.0 seconds
    # 65536 squares took: 0.32781171798706055 seconds
    # 131072 squares took: 1.0811586380004883 seconds
    # 262144 squares took: 3.7573440074920654 seconds

    ### ITERATION 4 ###
    # bit shift - results seem comparable to normal multiplying
    # sum_of_grains = 1
    # last_square = 1
    # if 1 == squares:
    #     return 1
    #
    # for x in range(2, squares + 1):
    #     sum_of_grains += last_square << 1
    #     last_square = last_square << 1
    # return sum_of_grains
    # TEST:
    # 128 squares took: 0.0 seconds
    # 256 squares took: 0.0 seconds
    # 512 squares took: 0.0 seconds
    # 1024 squares took: 0.0 seconds
    # 65536 squares took: 0.2917296886444092 seconds
    # 131072 squares took: 0.9778952598571777 seconds
    # 262144 squares took: 3.41083025932312 seconds

    ### ITERATION 5 ###
    # smarter bit shift - results seem comparable to normal multiplying
    # ok - we have winner xD
    return (1 << squares) - 1
    # TEST:
    # 128 squares took: 0.0 seconds
    # 256 squares took: 0.0 seconds
    # 512 squares took: 0.0 seconds
    # 1024 squares took: 0.0 seconds
    # 65536 squares took: 0.0 seconds
    # 131072 squares took: 0.0 seconds
    # 262144 squares took: 0.0 seconds
