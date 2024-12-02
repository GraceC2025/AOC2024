# write a function for each day's puzzle
def day01():
    print('Day 01')
    
    # set up empty lists
    left = []
    right = []
    
    # read TXT file
    file = open('input.txt', 'r')
    split = [line.strip() for line in file]
    for line in split:
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])
    
    # pair smallest number on left with smallest number on right
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    
    # iterate from smallest to largest
    for (l, r) in zip(sorted_left, sorted_right):
        print(l, r)
    

def main():
    # update this function call for each puzzle 
    day01()

if __name__ == "__main__":
    main() 
