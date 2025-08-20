def count_of_words(text):
    split_text = text.split()
    total_words = len(split_text)
    return f"Found {total_words} total words"

def count_of_characters(text):
    new_dict = {}
    text = text.lower()
    split_text = text.split()
    for i in split_text:
        split_word = list(i)
        for x in split_word:
            if x not in new_dict:
                new_dict[x] = 1
            else:
                new_dict[x] += 1
    return new_dict
    
def report_of_dictionary(dictionary):
    print_array = []
    for i in dictionary:
        if i.isalpha():
            print_array.append({"key":i, "value": dictionary[i]})
        else:
            pass
    print_array.sort(reverse=True, key = sort_on)
    return print_array

def sort_on(items):
    return items["value"]
