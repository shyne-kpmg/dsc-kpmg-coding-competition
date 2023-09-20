# Question 0: Sample Question

Given a string, return the string in reverse order.

For example:  

    Given an input of "Hello world", your function should return "dlrow olleH".

# Question 1: Checksum

A spreadsheet consists of rows of apparently-random numbers. You have been tasked with calculating the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example:

    Given the following spreadsheet:  
    [  
    [5, 1, 9, 5],  
    [7, 5, 3   ],  
    [2, 4, 6, 8],  
    ]

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

    Therefore, the spreadsheet's checksum is 8 + 4 + 6 = 18.

# Question 2: Digitsum

Given an integer number, return the sum of its digits.

For example:  

    1234 produces a sum of 10 (1+2+3+4)
    1111 produces a sum of 4 (1+1+1+1)

# Question 3: Santa

Santa needs to deliver a present to a child, but he's having trouble finding the right floor in a tall apartment building. Fortunately, he has a set of instructions to follow, which consist of a series of opening and closing parentheses. An opening parenthesis, '(', indicates that Santa should go up one floor, while a closing parenthesis, ')', indicates that he should go down one floor. Santa needs to starts on the ground floor (floor 0), and follow the instructions one character at a time.

Given a string of parentheses indicating the direction to move, write a function that calculates the floor that Santa ends up on.

For example:
    
    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

# Question 4: Bargain Packs

A manufacturing company has recently stopped producing several of its products. The company wants to sell the remaining inventory of these products in bargain packs, where all packs have the same composition. 

Given a list of product quantities, find the size of the smallest bundle that can be created. You can assume it will always be possible to find a bundle size where there are no leftover items.

For example:

    The company has:
    - 1000 units of Product A
    - 2000 Units of Product B
    - 3500 units of Product C

    The smallest pack size that can be created is 13, containing:
    - 2 units of Product A
    - 4 units of Product B
    - 7 units of Product C

# Question 5: Box Packing

Products can be shipped in multiple configurations (single units, cartons, pallets, etc). Sometimes all we know is the configuration sizes and number of units that need to be shipped but need to determine how these products will be packed in order to calculate realistic shipping and handling fees. The below question is used in practice as part of a cost / benefit analysis to determine whether it is profitable to consolidate product orders.

Given a set of integers `box_sizes` and an integer `units`, return the least number of boxes needed to hold all the units. 
No `units` can be left over and no boxes can be partially filled. 
If there is no combination of box sizes from `box_sizes` that holds all `units` return -1.

Hint: Time complexity `O(units * len(box_sizes)`

For example:

    Given:
    - box_sizes: (2, 5)
    - units: 12
    The solution is 3 (2 boxes of size 5, 1 box of size 2)

    Given:
    - box_sizes: (2, 5)
    - units: 3
    The solution is -1 

# Question 6: Column Names

You are working on a data science project that involves combining data from a variety of sources. Unfortunately, each source uses a different naming convention for their columns. Some use snake case, some use camel case, and some use spaced case. You need to standardise all column names to spaced case.

Write a function that can convert a list of of column names in camel case to spaced case.

For example:

    Given [firstName, lastName, addressLineOne, suburb]:

    Your function should return [First Name, Last Name, Address Line One, Suburb].

# Question 7: Keyword Extraction

You are working on a document retrieval engine that allows users to search for documents based on keywords. You need to write a function that can extract the three most common words from a document represented as a string, so that they can be used as keywords for searching.

The three most common words must be returned in lowercase in the correct order. You can assume that there will be no ties among the top three words and that the only punctation used will be commas and fullstops.

For example:

    Document: "Python is a high level, interpreted programming language that is widely used, including in web development, scientific computing, data analysis, artificial intelligence, and other applications. Python is designed to be an easily readable language. It is also known for having many third party libraries created by the Python community.

    Keywords: 'is', 'python', 'language'

# Question 8: Clustering

A clustering algorithm has been used to group points in a dataset based on their x and y attributes. You have been provided with the centerpoint of each cluster in the format $[({x_0}, {y_0}), ({x_1}, {y_1}), ..., ({x_n}, {y_n})]$ and asked to find which cluster a new point belongs to by finding the closest centrepoint using Euclidean distance. You can assume there will be a single closest centrepoint.

For example:
    
    Given the cluster centres [(-1, 3), (2, 4), (-5, 3)]:
    
    A new point (3, 4) would belong to cluster 1 with centrepoint (2, 4).

# Question 9: Decision Trees

You are writing a decision tree algorithm from scratch for a classification problem.

Given a list of possible splits at a decision tree node, write a function to choose the best split based on Gini impurity. You can assume the two classes are called A and B.

The Gini impurity of a node can be calculated as:

$$Gini(D) = 1 - \sum_{i=1}^k p_i^2$$

where $k$ is the class index and $p_i$ is the proportion of records in that class.

The gini impurity of a split can be calculated as:

$$Gini_{split}(D) = \frac {n_1}{n} Gini(D_1) + \frac {n_2}{n} Gini(D_2)$$

For example:

    Given two potential splits:
    [[AAAAAABB, BB], [AAAAAB, ABBB]]

    Which minimises the Gini impurity?

    The Gini impurity of the potential nodes are:
    - AAAAAABB = 0.375
    - BB = 0.0
    - AAAAAB = 0.278
    - ABBB = 0.375

    This means the impurity of the splits are:
    - split 0 = 8/10 * 0.375 + 2/10 * 0 = 0.300
    - split 1 = 6/10 * 0.278 + 4/10 * 0.375 = 0.317

    Therefore, split 0 is the best split.

 # Question 10: Linear Regression

You have a dataset of x-coordinates and y-coordinates and need to make a prediction for a new x-value. Using linear regression, the gradient (m) and slope (c) of the line of best fit can be calulated as below.

$$\hat{x} = \frac {\sum\limits_{i=1}^n x_i}{n} $$

$$\hat{y} = \frac {\sum\limits\_{i=1}^n y_i}{n} $$

$$m = \frac {\sum\limits_{i=1}^n (x_i - \hat{x}) (y_i - \hat{y})}{\sum\limits_{i=1}^n (x_i - \hat{x})^2} $$

$$c = \hat{y} - m\hat{x} $$

What is the predicted y-value for a new x-value?

For example:

    Given x-coordinates of [1, 2, 3, 4, 5], y-coordinates of [1, 1.5, 3, 4.5, 5] and a new x-value of 6:
    
    We can calculate that the average x-value is 3 and the average y-value is 3. 

    We can then calculate that m is 1.1 and c is -0.3.
    
    For an x-value of 6, we then predict a y-value of 6.3 (y = mx+c = 1.1*6-0.3 = 6.3).

# Question 11: Wordle 1

You have been tasked with building a Wordle game. In Wordle, the player has to guess a five-letter word chosen by the computer. The computer provides feedback to the player by coloring the letters of the guessed word in the following way:
- A green letter represents a letter that is in the same position in the target word and the guessed word.
- A yellow letter represents a letter that is present in the target word, but in a different position in the guessed word.
- A red letter represents a letter that is not present in the target word.

You need to build a function that takes a target word and a guessed word as input and returns the feedback as a string, where G represents a green letter, Y represents a yellow letter, and R represents a red letter.

For example:

    Given a target word of HOUSE and a guessed word of HONEY, the feedback would be GGRYR.

# Question 12: Wordle 2

You now want to build a Wordle bot to play your Wordle game.

Given a list of allowed words, a list of previous guesses, and the feedback for those previous guesses, your bot needs to be able to determine which words are still valid solutions.

For example:

    Given:
    Allowed words = [BREAD, PEACH, CHART, LEAKS, IDEAS, MEANT]
    Guesses = [BREAD, LEAKS]
    Feedback = [RRYYR, RGGRR]

    CHART and IDEAS are no longer valid solutions as we know E is the second letter and A is the third letter.

    Therefore, the remaining solutions are PEACH and MEANT.

# Question 13: Scheduling

Your calender has been overbooked and you want to remove the minimum number of meetings needed so no meetings overlap.

Given a list of meeting intervals, return the minimum number of meetings you need to remove to make the rest of the meetings non-overlapping.

Hint: You should always schedule the meeting with the earliest deadline next.

For example:

    Given the list of meetings [[9, 10], [10, 11], [10, 12], [11, 12]]:

    The meeting [10, 12] can be removed so no meetings overlap.

    Therefore, only one meeting needs to be removed.

# Question 14: Shortest Path

You are planning a road trip and want to find the shortest route. You have a map that shows the major cities along the way and the distances between them.

Given a graph represented as an adjacency matrix, find the shortest distance between the first and last cities. Each row of the adjacency matrix contains the distances to the other cities starting from the city with that index. You can assume there will always be a feasible path between the first and last city and that a large number will be used for distances between cities that there is not a road between.

Each number in the adjacency matrix contains the distance starting from the row index city and ending at the column index city.

For example:

    The matrix below represents a graph where:
    -  you can travel from city 0 to city 1 (with distance 3) or 2 (with distance 4)
    -  you can travel from city 1 to city 3 (with distance 8) or city 2 to city 3 (with distance 5)

    
    [  
    [inf, 3, 4, inf], 
    [inf, inf, inf, 8], 
    [inf, inf, inf, 5], 
    [inf, inf, inf, inf]  
    ]

    Starting at city 0 and ending at city 3, the shortest distance is 9.
    This uses a path travelling from city 0 to city 2 (with a distance of 4), then city 2 to city 3 (with a distance of 5).
