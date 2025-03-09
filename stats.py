
def word_count(input_string):
    return len(input_string.split())

def character_count(input_string):
    characters_with_count = dict()
    for c in input_string:
        lc = c.lower()
        if lc in characters_with_count:
            characters_with_count[lc] += 1
        else:
            characters_with_count[lc] = 1
    return characters_with_count

def sort_on(dict):
    return dict["num"]

def char_count_report(data):
    data_list = list()
    for char, num in data.items():
        if char.isalpha(): 
            data_list.append({"char": char, "num": num})
    
    data_list.sort(reverse=True, key=sort_on)

    return data_list
