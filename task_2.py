new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
changed_new_list = []
for element in new_list:
    if element.isdecimal():
        element = int(element)
        element_num = f'"{element:02d}"'
        changed_new_list.append(element_num)
    elif "+" in element:
        new_element = element[1:2]
        lost_element = element[0:1]
        final_element = '"' + lost_element + "0" + new_element + '"'
        changed_new_list.append(final_element)
    elif "-" in element:
        new_element = element[1:2]
        lost_element = element[0:1]
        final_element = '"' + lost_element + "0" + new_element + '"'
        changed_new_list.append(final_element)
    elif isinstance(element, str) is True:
        changed_new_list.append(element)
completed_list = " ".join(changed_new_list)
print(completed_list)