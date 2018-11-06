from shop import models


def get_daohang(request):
    type_list = models.Classify.objects.filter(Parentid=0)
    # 循环一级分类得到二级分类
    all_data = []
    for type_1 in type_list:
        type_list_2 = models.Classify.objects.filter(Parentid=type_1.id)
        two_data = []
        for type_2 in type_list_2:
            temp = {}
            temp['id'] = type_2.id
            temp['name'] = type_2.name
            type_list_3 = models.Classify.objects.filter(Parentid=type_2.id)
            temp['list'] = type_list_3
            two_data.append(temp)
        all_data.append(two_data)
    print(all_data)
    con = {
        'type_list': type_list,
        'all_data': all_data,
    }

    return (con)
