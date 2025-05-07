def get_number_of_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_count_of_characters(text):
    dict_char = {}
    count = 1
    lower_case = text.lower()
    for char in lower_case:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = count
    return dict_char

def sorting_key(dict):
    return dict["num"]

def sort_on(dict_of_count):
    new_list = []
    for key in dict_of_count:
        inner_dict = {}
        inner_dict["char"] = key
        inner_dict["num"] = dict_of_count[key]
        
        new_list.append(inner_dict)
    new_list.sort(reverse=True, key=sorting_key)

     
        
    return new_list


