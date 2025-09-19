def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list2 = list_to_add_elements.copy()
    list2.append('Yellow')
    list2.insert(0,'Pink')
    return list2

def is_empty(list_to_check):
    return len(list_to_check) == 0

print(is_empty([]))
print(is_empty([1,2,3]))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >=3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False



def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0]= list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1]= list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2]= list_of_lists_to_modify[2][len(list_of_lists_to_modify[2])-2:len(list_of_lists_to_modify[2])]
    return list_of_lists_to_modify
