import json

# 创建 json 文件
my_dict = {
    'name':'罗浩',
    'age':40,
    'friends':['好命', '年田'],
    'cars':[
        {'brand':'AWM', 'max_speed':240},
        {'brand':'Audi', 'max_speed':240},
        {'brand':'Benz', 'max_speed':124}
    ]
}

with open('data.json', 'w') as file:
    json.dump(my_dict, file)

# 读取 json 文件
with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)