# 列表推导式
# a = [0] * 3
# for i in range(3):
#     a[i] = [0] * 3
# b = [[0]*3 for i range(3)] 

word = ['Great','FishC','Brilliant','Fantastic']
word_select = [i for i in word if i[0]=='F']
print(word_select)

# 列表推导式的嵌套