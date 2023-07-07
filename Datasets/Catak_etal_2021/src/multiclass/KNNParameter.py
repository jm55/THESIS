

class KNNParameter:
    def __init__(self, n_neighbors, p, algorithm):

        #Embedding
        self.n_neighbors = n_neighbors
        self.p = p
        self.algorithm = algorithm



class KNNParameters:
    def __init__(self):
        # model
        self.parameters = []
        # 2019-07-06 09_09_39.367144
        #1- 33 self.parameters.append(KNNParameter(3))
        #2- 31 self.parameters.append(KNNParameter(5))
        #3- 31 self.parameters.append(KNNParameter(9))
        #4- 32 self.parameters.append(KNNParameter(15))

        # 2019-07-06 13_51_03.456234
        #5- 30 self.parameters.append(KNNParameter(21))

        self.parameters.append(KNNParameter(3, 3, "auto"))
        self.parameters.append(KNNParameter(3, 5, "auto"))
        self.parameters.append(KNNParameter(3, 7, "auto"))

        self.parameters.append(KNNParameter(3, 2, "ball_tree"))
        self.parameters.append(KNNParameter(3, 2, "kd_tree"))
        self.parameters.append(KNNParameter(3, 2, "brute"))

        self.parameters.append(KNNParameter(5, 2, "ball_tree"))
        self.parameters.append(KNNParameter(5, 2, "kd_tree"))
        self.parameters.append(KNNParameter(5, 2, "brute"))

        self.parameters.append(KNNParameter(7, 2, "brute"))

        self.parameters.append(KNNParameter(3, 3, "auto"))
        self.parameters.append(KNNParameter(3, 5, "auto"))
        self.parameters.append(KNNParameter(3, 7, "auto"))

        self.parameters.append(KNNParameter(3, 2, "ball_tree"))
        self.parameters.append(KNNParameter(3, 2, "kd_tree"))
        self.parameters.append(KNNParameter(3, 2, "brute"))

        self.parameters.append(KNNParameter(5, 2, "ball_tree"))
        self.parameters.append(KNNParameter(5, 2, "kd_tree"))
        self.parameters.append(KNNParameter(5, 2, "brute"))

        self.parameters.append(KNNParameter(7, 2, "brute"))

        self.index = 0


