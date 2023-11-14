def num_of_wc_runs(n,m): 
    # Initialize a 2d table with 0s
    # T[i][j] is the min number of tests for i bricks and j force settings
    S = [[0] * (n + 1) for i in range(m + 1)]

    # Base case: if there's 1 brick, test all the force settings 
    if m == 1:
        return n
    
    # Base case: if there are 0 bricks, no tests need to be done
    if n == 0:
        return 0

    # Iterate through each brick
    for i in range(1, m + 1):
        # Iterate through the number of times that the machine may run
        for j in range(1, n + 1):
            S[i][j] = float('inf')
            # Iterate over each potential force settings for the brick
            for k in range(1, j + 1):
                # Use the recursion formula
                S[i][j] = min(S[i][j], max(S[i-1][k-1], S[i][j-k]) + 1)
    return S[m][n]
#--------------------------
def next_setting(n, m):

    # Initialize table T[i][j] for the min number of tests for i bricks and j force settings
    S = [[0] * (n + 1) for i in range(m + 1)]
    
    # Base case: if there are 0 bricks, no tests need to be done
    if n == 0:
        return 0
    
    # Initialize a table to store the optimal choices for the next setting for i bricks and j force settings
    next_k_val = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            S[i][j] = float('inf')
            # Iterate over potential force settings for the first brick
            for k in range(1, j + 1):
                # If at the current value, the current k value results in a SMALLER min number of tests 
                # Update next_k_val with this optimal value of k
                if ((min(S[i][j], max(S[i-1][k-1], S[i][j-k]) + 1)) < S[i][j]):
                    S[i][j] = min(T[i][j], max(S[i-1][k-1], S[i][j-k]) + 1)
                    next_k_val[i][j] = k
    return next_k_val[m][n]

