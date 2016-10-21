# game_of_chance.py : Solve the Yahtzee problem!
# Prateek Srivastava, October 2016

from sys import argv

#solver function
def solve(a):
    expected_value = 0
    ind = [0]

    # if 1 die is rolled
    e = float(sum([score([i, a[1], a[2]]) for i in range(1, 7)])) / 6
    (expected_value, ind) = (e, [1]) if e > expected_value else (expected_value, ind)
    e = float(sum([score([a[0], i, a[2]]) for i in range(1, 7)])) / 6
    (expected_value, ind) = (e, [2]) if e > expected_value else (expected_value, ind)
    e = float(sum([score([a[0], a[1], i]) for i in range(1, 7)])) / 6
    (expected_value, ind) = (e, [3]) if e > expected_value else (expected_value, ind)

    # if 2 dice are rolled
    e = float(sum([score([i, j, a[2]]) for i in range(1, 7) for j in range(1, 7)])) / 36
    (expected_value, ind) = (e, [1, 2]) if e > expected_value else (expected_value, ind)

    e = float(sum([score([a[0], i, j]) for i in range(1, 7) for j in range(1, 7)])) / 36
    (expected_value, ind) = (e, [2, 3]) if e > expected_value else (expected_value, ind)

    e = float(sum([score([i, a[1], j]) for i in range(1, 7) for j in range(1, 7)])) / 36
    (expected_value, ind) = (e, [1, 3]) if e > expected_value else (expected_value, ind)

    # if 3 dice are rolled
    e = float(sum([score([i, j, k]) for i in range(1, 7) for j in range(1, 7) for k \
                   in range(1, 7)])) / 216
    (expected_value, ind) = (e, [1, 2, 3]) if e > expected_value else (expected_value, ind)

    return expected_value, ind

#Calculate the score
def score(a):
    return 25 if a[0]==a[1] and a[0]==a[2] else sum(a)

# main()
a=[int(argv[x]) for x in range(1,len(argv))]
if len(a)==0:
    print "please input the initial dice values"
else:
    print "Dice Values :",a
    if (a[0]==a[1] and a[0]==a[2]):
        print "No need to roll the dice"
    else:
        expected_value, ind = solve(a)
        print "roll the following dice :",
        for i in ind:
            print "  ",i,
