import time
import matplotlib.pyplot as plt
import pandas as pd
from ACO_TPS_Class import *
from Input_Target import *
import numpy as np
from scipy import spatial

# # вычисление длины пути
# def cal_total_distance(routine):
#     num_points, = routine.shape
#     return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points-1)])

# вычисление длины пути
def cal_total_distance(routine,num_points):
    num_points=num_points
    s=sum([distance_matrix[routine[i], routine[i + 1]] for i in range(num_points)])
    return s

def cal_distance(i,j):
    return distance_matrix[i, j]

def main(size_pop=40, max_iter=20, check=0):
    # создание объекта алгоритма муравьиной колонии
    aca = ACO_TSP(points_coordinate, func=cal_total_distance, func_dis=cal_distance, n_dim=num_points, distance=distance,
                  size_pop=size_pop,  # количество муравьёв
                  max_iter=max_iter, distance_matrix=distance_matrix)
    best_x, best_y, best_len= aca.run()

    time_exec=abs(time.time() - start_time)
    print("time of execution(",check,"): %s seconds" % time_exec)  # вычисление времени выполнения

    # # Вывод результатов на экран
    # fig, ax = plt.subplots(1, 2)
    # best_points_ = np.concatenate([best_x, [best_x[0]]])
    # best_points_coordinate = points_coordinate[best_points_, :]
    # for index in range(0, len(best_points_)):
    #     ax[0].annotate(best_points_[index], (best_points_coordinate[index, 0], best_points_coordinate[index, 1]))
    # ax[0].plot(best_points_coordinate[:, 0],
    #            best_points_coordinate[:, 1], 'o-r')
    # pd.DataFrame(aca.y_best_history).cummin().plot(ax=ax[1])
    # # изменение размера графиков
    # plt.rcParams['figure.figsize'] = [20, 10]
    # plt.show()

    #===================== Вывод результатов на экран ===================
    best_points_=[]
    for i in range(len(best_x)):
        if i!=0 and best_x[i]==0:
            continue
        best_points_.append(best_x[i])
    best_points_coordinate = points_coordinate[best_points_, :]
    for index in range(num_points):
        plt.annotate(index, (points_coordinate[index, 0], points_coordinate[index, 1]))
        plt.plot(points_coordinate[index, 0], points_coordinate[index, 1], 'o-r')
    plt.plot(best_points_coordinate[:, 0],
               best_points_coordinate[:, 1], 'o-r')
    # изменение размера графиков
    # plt.rcParams['figure.figsize'] = [20, 10]
    plt.annotate("flight length: %.4f km" % best_y, (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
    plt.annotate("time of execution: %.4f seconds" % time_exec, (0, 0), (150, -20), xycoords='axes fraction', textcoords='offset points', va='top')
    plt.show()

    return best_len, best_y, best_len

if __name__ == "__main__":

    # #читання з файлу
    # with open("write.txt", "r") as file:
    #     contents = file.readlines()
    #     indices = [i for i, x in enumerate(contents) if x == "----------\n"]
    #     # indices.pop(-1)
    #
    # time_to_fly = float(contents[3])
    # speed = 10
    # start = np.asfarray(contents[1].split(' '))
    # points_coordinate = np.array([start])
    # end = np.array([np.asfarray(contents[2].split(' '))])
    # num_points = int(np.asfarray(contents[0].split(' '))[0])
    # for i in range(num_points):
    #     points_coordinate = np.append(points_coordinate, np.array([np.asfarray(contents[4 + i].split(' '))]),
    #                                   axis=0)
    # points_coordinate = np.append(points_coordinate, end, axis=0)
    # num_points += 2
    # distance = time_to_fly * speed
    # # print("Координаты вершин:\n", points_coordinate, "\n")
    # # вычисление матрицы расстояний между вершин
    # distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
    #
    # start_time = time.time()  # сохранение времени начала выполнения
    # x, y, target = main(30, 15, i+1)  # выполнение кода
    # print("length: ", y, "target:", target, "\n")
    #
    # f = open("write_2.txt", "w")
    # f.writelines("----------\n")
    # f.writelines(contents[:indices[0]])
    # f.writelines(['AntColony\n', str(y/speed*60)+'\n', str(target-2)+'\n'])
    #
    #
    # for index in indices:
    #     time_to_fly = float(contents[index+4])
    #     speed = 10
    #     start = np.asfarray(contents[index+2].split(' '))
    #
    #     points_coordinate = np.array([start])
    #
    #     end = np.array([np.asfarray(contents[index+3].split(' '))])
    #
    #     num_points = int(np.asfarray(contents[index+1].split(' '))[0])
    #     for i in range(num_points):
    #         points_coordinate = np.append(points_coordinate, np.array([np.asfarray(contents[index + 5 + i].split(' '))]),
    #                                       axis=0)
    #     points_coordinate = np.append(points_coordinate, end, axis=0)
    #     num_points += 2
    #
    #     distance = time_to_fly * speed
    #
    #     # print("Координаты вершин:\n", points_coordinate, "\n")
    #
    #     # вычисление матрицы расстояний между вершин
    #     distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
    #
    #     start_time = time.time()  # сохранение времени начала выполнения
    #     x, y, target = main(30, 15, i+1)  # выполнение кода
    #     print("length: ", y, "target:", target, "\n")
    #
    #     f.writelines(contents[indices[indices.index(index)]:indices[indices.index(index)+1]])
    #     f.writelines(['AntColony\n', str(y / speed * 60) + '\n', str(target-2) + '\n'])
    # f.writelines("----------\n")
    # f.close()


    for i in range(1):
        start_time = time.time()  # сохранение времени начала выполнения
        x,y,length=main(25,15,i)  # выполнение кода
        print("length: ",y,"target:", length, "\n")


    # #=================== визначення опт критеріїв ітерацій і мурах =====================
    # x_len=[]
    # y_len=[]
    # for i in range(1,31):
    #     start_time = time.time()  # сохранение времени начала выполнения
    #     x, y ,l= main(i,15,i) # выполнение кода
    #     x_len.append(x)
    #     y_len.append(y)
    #
    # plt.subplot(1,2,1)
    # plt.plot(x_len)
    # plt.subplot(1, 2, 2)
    # plt.plot(y_len)
    # plt.show()


