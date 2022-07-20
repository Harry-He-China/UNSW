# 7 person 0, 1, 2, 3, 4, 5, 6
list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [4, 6], [5, 6]]
dict = {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
print(dict)
dict[0] = 1
print(dict)
# for i in range(len(out_boxes)):
#     for pair in list:
#         if i in pair:
#             grouped_label =