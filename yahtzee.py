import numpy as np

roll = np.random.randint(1, 6, 6)
print(roll)


def re_order():
    # build function that allows user to reorder roll from lowest to highest
    pass


def reroll():


    # reroll needs to be set up such that after you change a number,
    # it cannot be changed again
    # because if the first number changed in roll is randomly changed to the next number in reroll
    # it will get rerolled again

    # SOLUTION: change all matching numbers to 0, then iterate through roll and change all 0s


    reroll = list(input('which would you like to reroll: '))
    reroll = list(map(int, reroll))
    for a in reroll:
        for i in roll:
            if a == i:
                # identify indecies where a = i
                index = np.where(roll == a)
                roll[index[0][0]] = 0
                # print(roll)
                break

    for a in range(len(roll)):
        if roll[a] == 0:
            roll[a] = np.random.randint(1, 6)
    print(roll)


for i in range(3):
    answer = input('Would you like to reroll? (y/n)')
    if answer == 'y':
        reroll()
    if answer == 'n':
        print('Your final roll: ', roll)
        break
    i += 1
