examples = {
    "0": {
        "1": (
            #input
            "Hello world",
            #output
            "dlrow olleH"
        ),
    },
    "1": {
        "1": (
                #input
                [
                [5, 1, 9, 5],
                [7, 5, 3   ],
                [2, 4, 6, 8],
                ],
                #output
                18
        ),
    },
    "2": {
        "1": (
                #input
                1234,
                #output
                10
        ),
    },
    "3": {
        "1": (
                #input
                "))(((((",
                #output
                3
        ),
    },
    "4": {
        "1": (
                #input
                [1000, 2000, 3500],
                #output
                13
        ),
    },
    "5": {
        "1": (
            # input
            (
                (2, 5), # box_sizes
                12      # units
            ),
            # output
            3
        ),
    },
    "6": {
        "1": (
            # input
            ["firstName", "lastName", "addressLineOne", "suburb"],
            # output
            ["First Name", "Last Name", "Address Line One", "Suburb"]
        ),
    },
    "7": {
        "1": (
            # input
            "Python is a high level, interpreted programming language that is widely used, including in web development, scientific computing, data analysis, artificial intelligence, and other applications. Python is designed to be an easily readable language. It is also known for having many third party libraries created by the Python community.",
            # output
            ["is", "python", "language"]
        ),
    },
    "8": {
        "1": (
            # input
            (
                [(-1, 3), (2, 4), (-5, 3)], 
                (3, 4)
            ),
            # output
            1
        ),
    },
    "9": {
        "1": (
                #input
                [["AAAAAABB", "BB"], ["AAAAAB", "ABBB"]],
                #output
                0
        ),
    },
    "10": {
        "1": (
            # input
            (
                [1, 2, 3, 4, 5],
                [1, 1.5, 3, 4.5, 5],
                6
            ),
            # output
            6.3
        ),
    },
    "11": {
        "1": (
            # input
            (
                "HOUSE",
                "HONEY"
            ),
            # output
            "GGRYR"
        ),
    },
    "12": {
        "1": (
            # input
            (
                ["BREAD", "PEACH", "CHART", "LEAKS", "IDEAS", "MEANT"],
                ["BREAD", "LEAKS"],
                ["RRYYR", "RGGRR"]
            ),
            # output
            ["PEACH", "MEANT"]
        ),
    },
    "13": {
        "1": (
                #input
                [[9, 10], [10, 11], [10, 12], [11, 12]],
                #output
                1
        ),
    },
    "14": {
        "1": (
            # input
            [[9999, 3, 4, 9999], 
            [9999, 9999, 9999, 8], 
            [9999, 9999, 9999, 5], 
            [9999, 9999, 9999, 9999]],
            # output
            9
        ),
    },
}