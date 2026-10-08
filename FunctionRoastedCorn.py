def longest_word(words):
    longest = " "
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)
    
the_list = ["welcome","out","weather","mobile","breakfast","journey"] 
result_word, result_length = longest_word(the_list) 


def odd_index(word):
    result = ""
    for character in range(len(word)):
        if character % 2 == 1:
            result += word[character]
    return result


def minimum_numbers(numbers):
    smallest = numbers[0]
    for the_number in numbers:
        if the_number < smallest:
            smallest = the_number
    return smallest
                
def maximum_numbers(numbers):
    largest = numbers[0]
    for the_number in numbers:
        if the_number > largest:
            largest = the_number
    return largest
    def repeated(word, number):
    if type(number) == float:
        return word
        
    result = ""
    for index in range(number):
        result += word
    return result

def square(numbers):
    result = []
    for the_numbers in numbers:
        result.append(the_numbers * the_numbers)
    return result
    
def sum_of_square(numbers):
    total = 0
    for the_numbers in numbers:
        total += (the_numbers * the_numbers)
    return total
