def merge_two_lists(list1, list2):
    merged_list = []
    longest_list_length = len(list1) if len(list1) > len(list2) else len(list2)
    first = list1[0] if list1[0] <= list2[0] else list2[0]
    print(first)
    print(longest_list_length)

    for i in range(longest_list_length):
        if first == list[i]:
            merged_list.append(first)
        if first == list2[i]:
            merged_list.append(list2[i])
        

    # for i in range(len(list1)):
    #     for j in range(len(list2)):
    #         print(list1[i], list2[j])
    #         if list1[i] == list2[j]:
    #             merged_list.append(list1[i])
    #             merged_list.append(list2[j])
    #         elif list1[i] < list2[j]:
    #             merged_list.append(list1[i])
    #         else:
    #             merged_list.append(list2[j])
    #         print(merged_list)
    return merged_list


llist1 = [1, 2, 3, 4]
llist2 = [1, 3, 4]

mmerged_list = merge_two_lists(llist1, llist2)
print(mmerged_list)

