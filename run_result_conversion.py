import json
import csv

f = open('./hyperplan-fetch/results/thin_vert_place/iteration/1/results.json')
g = open('./hyperplan-fetch/results/thin_vert_place/iteration/1/configs.json')
file = open('./hyperplan-fetch/results/thin_vert_place/iteration/1/results.csv', 'w', newline='')
writer = csv.writer(file)
datas = f.readlines()
writer.writerow(['id','budget','loss','planner','model_based'])
datag = g.readlines()
dic = {}
for line in datag:
    line = json.loads(line)
    dic[str(line[0])] = line
# print(dic)

for data in datas:
    # datag = json.loads(g.readline())
    lis =  json.loads(data)
    try:
        if str(lis[0]) in dic:
            if True: #lis[3]['loss'] != 0:
                datag = dic[str(lis[0])]
                n = '(' + str(lis[0][0]) + ', ' + str(lis[0][1]) + ', '+ str(lis[0][2]) + ')'
                temp = [n, lis[1], lis[3]['loss'], datag[1]['planner'], int(datag[2]['model_based_pick'])]
                print(temp)
                writer.writerow(temp)
                pass
        # else:
        #     print(f"Error at {lis[0]}")
    except:
        print(f"Error at {lis[0]}")
f.close()
g.close()
file.close()