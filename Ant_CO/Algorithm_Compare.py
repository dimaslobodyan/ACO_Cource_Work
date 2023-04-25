# import matplotlib.pyplot as plt

# with open("rez6_100.txt", "r") as file:
# # with open("rez3_ant_30_iteration_45.txt", "r") as file:
#     contents = file.readlines()
#     contents.append("----------\n")
#     indices = [i for i, x in enumerate(contents) if x == "----------\n"]
#     indices.pop(0)
#
# TheNearestNeighbour_Time=[]
# TheNearestLineTargetsWithX_Time=[]
# TheNearestLineTargetsWithMatrix_Time=[]
# AntColony_Time=[]
#
# TheNearestNeighbour_Target=[]
# TheNearestLineTargetsWithX_Target=[]
# TheNearestLineTargetsWithMatrix_Target=[]
# AntColony_Target=[]
# for index in indices:
#     TheNearestNeighbour_Time.append(float(contents[index-11].replace(',','.')))
#     TheNearestLineTargetsWithX_Time.append(float(contents[index-8].replace(',','.')))
#     TheNearestLineTargetsWithMatrix_Time.append(float(contents[index-5].replace(',','.')))
#     AntColony_Time.append(float(contents[index-2]))
#
#     TheNearestNeighbour_Target.append(int(contents[index-10]))
#     TheNearestLineTargetsWithX_Target.append(int(contents[index-7]))
#     TheNearestLineTargetsWithMatrix_Target.append(int(contents[index-4]))
#     AntColony_Target.append(int(contents[index-1]))
#
# # NN=0
# # NLTWX=0
# # NLTWM=0
# # AC=0
# rez=[0,0,0,0]
# target_rez=[0,0,0,0]
# for i in range(len(TheNearestNeighbour_Time)):
#     target=[TheNearestNeighbour_Target[i],TheNearestLineTargetsWithX_Target[i],TheNearestLineTargetsWithMatrix_Target[i],AntColony_Target[i]]
#     time=[TheNearestNeighbour_Time[i], TheNearestLineTargetsWithX_Time[i],TheNearestLineTargetsWithMatrix_Time[i],AntColony_Time[i]]
#     # target = [TheNearestNeighbour_Target[i], TheNearestLineTargetsWithX_Target[i],
#     #           TheNearestLineTargetsWithMatrix_Target[i]]
#     # time = [TheNearestNeighbour_Time[i], TheNearestLineTargetsWithX_Time[i], TheNearestLineTargetsWithMatrix_Time[i]]
#     max_target=max(target)
#     indices = [i for i, x in enumerate(target) if x == max_target]
#     if len(indices)>1:
#         sub_time=[]
#         for index in indices:
#             sub_time.append(time[index])
#             target_rez[index]+=1
#         min_time=min(sub_time)
#         # indices_subtime = [i for i, x in enumerate(sub_time) if x == min_time]
#         # if len(indices_subtime)>1:
#         #     indices_time_rez=[i for i, x in enumerate(time) if x == min_time]
#         #     for index in indices_time_rez:
#         #         rez[index]+=1
#         # else:
#         #     rez[indices_subtime[0]] += 1
#
#         indices_time_rez=[i for i, x in enumerate(time) if x == min_time]
#         for index in indices_time_rez:
#             rez[index]+=1
#     else:
#         target_rez[indices[0]] += 1
#         rez[indices[0]] += 1
#
# print("Count time when better than others: time_considering/only_targets\n")
# print('TheNearestNeighbour: ',rez[0],'/',target_rez[0])
# print('TheNearestLineTargetsWithX: ',rez[1],'/',target_rez[1])
# print('TheNearestLineTargetsWithMatrix: ',rez[2],'/',target_rez[2])
# print('AntColony: ',rez[3],'/',target_rez[3])
#
# plt.subplot(1,2,1)
# plt.title("Route time")
# plt.plot(TheNearestNeighbour_Time, label='NN')
# plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithX_Time, label='NLTWX')
# plt.legend(loc="upper left")
# # plt.plot(TheNearestLineTargetsWithMatrix_Time, label='NLTWM')
# # plt.legend(loc="upper left")
# plt.plot(AntColony_Time, label='AC')
# plt.legend(loc="upper left")
#
# plt.subplot(1, 2, 2)
# plt.title("Research targets")
# plt.plot(TheNearestNeighbour_Target, label='NN')
# plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithX_Target, label='NLTWX')
# plt.legend(loc="upper left")
# # plt.plot(TheNearestLineTargetsWithMatrix_Target, label='NLTWM')
# # plt.legend(loc="upper left")
# plt.plot(AntColony_Target, label='AC')
# plt.legend(loc="upper left")
# plt.show()


import matplotlib.pyplot as plt

with open("Alltxt2.txt", "r") as file:
    contents = file.readlines()
    # contents.append("----------\n")
    indices = [i for i, x in enumerate(contents) if x == "----------\n"]
    # indices.pop(0)

TheNearestNeighbour_Time=[]
TheNearestLineTargetsWithX_Time=[]
TheNearestLineTargetsWithMatrix_Time=[]
AntColony_Time=[]
AntColony_Serhii_Time=[]

TheNearestNeighbour_Target=[]
TheNearestLineTargetsWithX_Target=[]
TheNearestLineTargetsWithMatrix_Target=[]
AntColony_Target=[]
AntColony_Serhii_Target=[]

for index in indices:
    TheNearestNeighbour_Time.append(float(contents[index-14].replace(',','.')))
    TheNearestLineTargetsWithX_Time.append(float(contents[index-11].replace(',','.')))
    TheNearestLineTargetsWithMatrix_Time.append(float(contents[index-8].replace(',','.')))
    AntColony_Time.append(float(contents[index-5]))
    AntColony_Serhii_Time.append(float(contents[index - 2].replace(',','.')))

    TheNearestNeighbour_Target.append(int(contents[index-13]))
    TheNearestLineTargetsWithX_Target.append(int(contents[index-10]))
    TheNearestLineTargetsWithMatrix_Target.append(int(contents[index-7]))
    AntColony_Target.append(int(contents[index-4]))
    AntColony_Serhii_Target.append(int(contents[index - 1]))

rez=[0,0,0,0,0]
target_rez=[0,0,0,0,0]
for i in range(len(TheNearestNeighbour_Time)):
    target=[TheNearestNeighbour_Target[i],TheNearestLineTargetsWithX_Target[i],TheNearestLineTargetsWithMatrix_Target[i],AntColony_Target[i],AntColony_Serhii_Target[i]]
    time=[TheNearestNeighbour_Time[i], TheNearestLineTargetsWithX_Time[i],TheNearestLineTargetsWithMatrix_Time[i],AntColony_Time[i],AntColony_Serhii_Time[i]]
    # target = [TheNearestNeighbour_Target[i], TheNearestLineTargetsWithX_Target[i],
    #           TheNearestLineTargetsWithMatrix_Target[i]]
    # time = [TheNearestNeighbour_Time[i], TheNearestLineTargetsWithX_Time[i], TheNearestLineTargetsWithMatrix_Time[i]]
    max_target=max(target)
    indices = [i for i, x in enumerate(target) if x == max_target]
    if len(indices)>1:
        sub_time=[]
        for index in indices:
            sub_time.append(time[index])
            target_rez[index]+=1
        min_time=min(sub_time)
        indices_time_rez=[i for i, x in enumerate(time) if x == min_time]
        for index in indices_time_rez:
            rez[index]+=1
    else:
        target_rez[indices[0]] += 1
        rez[indices[0]] += 1

print("Count time when better than others: time_considering/only_targets\n")
print('TheNearestNeighbour: ',rez[0],'/',target_rez[0])
print('TheNearestLineTargetsWithX: ',rez[1],'/',target_rez[1])
print('TheNearestLineTargetsWithMatrix: ',rez[2],'/',target_rez[2])
print('AntColony: ',rez[3],'/',target_rez[3])
print('AntColony_Serhii: ',rez[4],'/',target_rez[4])

plt.subplot(1,2,1)
plt.title("Route time")
plt.plot(TheNearestNeighbour_Time, label='NN')
plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithX_Time, label='NLTWX')
# plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithMatrix_Time, label='NLTWM')
# plt.legend(loc="upper left")
plt.plot(AntColony_Time, label='AC')
plt.legend(loc="upper left")
# plt.plot(AntColony_Serhii_Time, label='AC_S')
# plt.legend(loc="upper left")

plt.subplot(1, 2, 2)
plt.title("Research targets")
plt.plot(TheNearestNeighbour_Target, label='NN')
plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithX_Target, label='NLTWX')
# plt.legend(loc="upper left")
# plt.plot(TheNearestLineTargetsWithMatrix_Target, label='NLTWM')
# plt.legend(loc="upper left")
plt.plot(AntColony_Target, label='AC')
plt.legend(loc="upper left")
# plt.plot(AntColony_Serhii_Target, label='AC_S')
# plt.legend(loc="upper left")
plt.show()
