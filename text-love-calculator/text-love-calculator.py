# Love calculator game as shown in:
# https://www.youtube.com/watch?v=oFsLVG7EAZ4

def unique_counts(name1, name2):
    '''Takes in two names and returns counts for each unique letter'''

    # make everything lower case to not double count
    name1_lc = name1.lower()
    name2_lc = name2.lower()
    temp_str = name1_lc + 'loves' + name2_lc

    unique_letters = []
    unique_letter_counts = []
    for letter in temp_str:
        # if letter not in unique letter list, add it
        if letter not in unique_letters:
            unique_letters.append(letter)
        
            # go thru whole string counting occurences of letter
            letter_count = 0
            for x in temp_str:
                if letter == x:
                    letter_count += 1
            unique_letter_counts.append(letter_count)
        
    return unique_letter_counts

def calc_love_percentage(list_of_counts):
    '''Recursive function to calculate love percentage'''

    # Exit case
    if len(list_of_counts) == 2:
        return str(list_of_counts[0]) + str(list_of_counts[1])

    # Add terms outside to inside 
    new_counts = []
    midpoint = len(list_of_counts) // 2
    for term in range(midpoint):
        temp_count = list_of_counts[term] + list_of_counts[len(list_of_counts)-1-term]
        new_counts.append(temp_count)

    # Drop the middle term if len is odd
    if len(list_of_counts) % 2 > 0:
        middle_term = (len(list_of_counts) // 2)
        new_counts.append(list_of_counts[middle_term])
    
    # Recurse.
    percentage = calc_love_percentage(new_counts)
    return percentage

def main():
    # start the game, ask for your name and crush's name
    print("*" * 40)
    print("Welcome to the Love Calculator!")
    print("*" * 40)
    name1 = input('First, what is your first name?: ')
    name2 = input("What is your crush's first name? ")
    
    # get counts of all unique letters in name1 + 'loves' + name2
    count_list = unique_counts(name1, name2)

    # calculate love percentage
    lp = calc_love_percentage(count_list)

    print(f"The love compatibility between {name1} and {name2} is: {lp}%!")

if __name__=='__main__':
    main()