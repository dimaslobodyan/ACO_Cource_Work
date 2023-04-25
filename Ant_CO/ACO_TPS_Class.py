import numpy as np
import matplotlib.pyplot as plt

class ACO_TSP:  # класс алгоритма муравьиной колонии для решения задачи коммивояжёра
    def __init__(self, points, func, func_dis, n_dim, distance, size_pop=10, max_iter=20, distance_matrix=None, alpha=1, beta=1, rho=0.1):
        self.func = func
        self.points = points
        self.func_dis = func_dis
        self.n_dim = n_dim  # количество городов
        self.size_pop = size_pop  # количество муравьёв
        self.max_iter = max_iter  # количество итераций
        self.alpha = alpha  # коэффициент важности феромонов в выборе пути
        self.beta = beta  # коэффициент значимости расстояния
        self.rho = rho  # скорость испарения феромонов
        self.distance=distance #шлях який може пролетіти БПЛА


        self.prob_matrix_distance = 1 / (distance_matrix + 1e-10 * np.eye(n_dim, n_dim))

        # Матрица феромонов, обновляющаяся каждую итерацию
        self.Tau = np.ones((n_dim, n_dim))
        # Путь каждого муравья в определённом поколении
        self.Table = np.zeros((size_pop, n_dim)).astype(int)
        self.y = None  # Общее расстояние пути муравья в определённом поколении
        self.generation_best_X, self.generation_best_Y, self.generation_best_N= [], [], [] # фиксирование лучших поколений
        self.x_best_history, self.y_best_history = self.generation_best_X, self.generation_best_Y
        self.best_x, self.best_y = None, None

    def run(self, max_iter=None):
        self.max_iter = max_iter or self.max_iter
        y_best_iter = 2 * self.distance
        unvis_best_iter = self.n_dim
        best_gen=0

        # for index in range(self.n_dim):
        #     plt.annotate(index, (self.points[index, 0], self.points[index, 1]))
        #     plt.plot(self.points[index, 0], self.points[index, 1], 'o-r')
        # plt.show()

        for i in range(self.max_iter):
            self.Table = np.zeros((self.size_pop, self.n_dim)).astype(int)
            # вероятность перехода без нормализации
            number_of_unvisited_target = np.zeros((self.size_pop, 1)).astype(int)
            prob_matrix = (self.Tau ** self.alpha) * (self.prob_matrix_distance) ** self.beta
            for j in range(self.size_pop):  # для каждого муравья
                # точка начала пути (она может быть случайной, это не имеет значения)
                self.Table[j, 0] = 0
                taboo_set_dist=[]
                kk=0
                for k in range(self.n_dim - 2):  # каждая вершина, которую проходят муравьи
                    # точка, которая была пройдена и не может быть пройдена повторно
                    taboo_set = set(self.Table[j, :kk + 1])
                    # список разрешённых вершин, из которых будет происходить выбор
                    allow_list = list(set(range(self.n_dim-1)) - taboo_set-set(taboo_set_dist))
                    prob = prob_matrix[self.Table[j, kk], allow_list]
                    prob = prob / prob.sum() # нормализация вероятности
                    # next_point = np.random.choice(allow_list, size=1, p=prob)[0]

                    next_point = np.random.choice(allow_list, size=1, p=prob)[0]
                    self.Table[j, kk + 1] = next_point
                    y = np.array([self.func(self.Table[j], kk+1)])

                    if (y[0]+self.func_dis(next_point,self.n_dim - 1))>self.distance: #перевірка чи долетимо до кінця
                        taboo_set_dist.append(next_point)
                        self.Table[j, kk + 1] = 0
                        number_of_unvisited_target[j]+=1
                        continue
                    kk+=1



                self.Table[j, self.n_dim - 1 - number_of_unvisited_target[j]] = self.n_dim - 1


            # рассчёт расстояния
            y = np.array([])
            kt=0
            for ii in self.Table:
                y=np.append(y,self.func(ii,int(self.n_dim - 1 - number_of_unvisited_target[kt][0])))
                kt+=1

            # фиксация лучшего решения
            # index_best = number_of_unvisited_target.argmin()
            min_number_of_unvisited_target = min(number_of_unvisited_target)
            indices = [i for i, x in enumerate(number_of_unvisited_target) if x == min_number_of_unvisited_target]
            if len(indices) > 1:
                sub_y = []
                for index in indices:
                    sub_y.append(y[index])
                index_best = indices[sub_y.index(min(sub_y))]
            else:
                index_best = indices[0]
            x_best, y_best, unvis_best= self.Table[index_best, :].copy(), y[index_best].copy(), number_of_unvisited_target[index_best][0]
            self.generation_best_X.append(x_best)
            self.generation_best_Y.append(y_best)
            self.generation_best_N.append(unvis_best)



            if unvis_best<unvis_best_iter:
                unvis_best_iter=unvis_best
                y_best_iter=y_best
                best_gen=i
            elif unvis_best==unvis_best_iter and y_best<y_best_iter:
                y_best_iter=y_best
                best_gen=i

            # # =========================== результат на кожній ітерації =====================================
            #
            #
            # best_points_ = []
            # for ii in range(len(x_best)):
            #     if ii != 0 and x_best[ii] == 0:
            #         continue
            #     best_points_.append(x_best[ii])
            # best_points_coordinate = self.points[best_points_, :]
            # plt.rcParams["figure.figsize"] = (8, 7)
            # for index in range(self.n_dim):
            #     plt.annotate(index, (self.points[index, 0], self.points[index, 1]))
            #     plt.plot(self.points[index, 0], self.points[index, 1], 'o-r')
            # plt.plot(best_points_coordinate[:, 0],
            #          best_points_coordinate[:, 1], 'o-r')
            # plt.annotate("iteration: %2d" % (i + 1), (0, 0), (0, -20), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            # plt.annotate("flight length: %.4f km" % y_best, (0, 0), (90, -20), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            # plt.annotate("visited num: %2d" % (self.n_dim-unvis_best), (0, 0), (250, -20), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            #
            # plt.annotate("Best:", (0, 0), (0, -40), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            # plt.annotate("flight length: %.4f km" % y_best_iter, (0, 0), (50, -40), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            # plt.annotate("visited num: %2d" % (self.n_dim - unvis_best_iter), (0, 0), (200, -40), xycoords='axes fraction',
            #              textcoords='offset points', va='top')
            # plt.show()
            # #==============================================================================================

            # подсчёт феромона, который будет добавлен к ребру
            delta_tau = np.zeros((self.n_dim, self.n_dim))
            for j in range(self.size_pop):  # для каждого муравья
                for k in range(self.n_dim - 1 - number_of_unvisited_target[j][0]):  # для каждой вершины
                    # муравьи перебираются из вершины n1 в вершину n2
                    n1, n2 = self.Table[j, k], self.Table[j, k + 1]
                    # delta_tau[n1, n2] += 1 / y[j]  # нанесение феромона
                    delta_tau[n1, n2] += (self.n_dim-number_of_unvisited_target[j][0]-2)/ (self.n_dim-2)/y[j]  # нанесение феромона
                # муравьи ползут от последней вершины обратно к первой
                # n1, n2 = self.Table[j, self.n_dim - 1], self.Table[j, 0]
                # delta_tau[n1, n2] += 1 / y[j]  # нанесение феромона

            self.Tau = (1 - self.rho) * self.Tau + delta_tau

        # best_generation = np.array(self.generation_best_N).argmin()
        best_generation=best_gen
        self.best_x = self.generation_best_X[best_generation]
        self.best_y = self.generation_best_Y[best_generation]
        return self.best_x, self.best_y, self.n_dim-unvis_best_iter

    fit = run