

class SVMParameter:
    def __init__(self, kernel, c, gamma, class_weights):

        #Embedding
        self.kernel = kernel
        self.c = c
        self.gamma = gamma
        self.class_weights = class_weights



class SVMParameters:
    def __init__(self):
        # model
        self.parameters = []
        # 2019-07-06 09_09_39.367144
        #1 - 29 self.parameters.append(SVMParameter("rbf", 1.0))
        #2 - 4  self.parameters.append(SVMParameter("sigmoid", 1.0))
        #3 - 29 self.parameters.append(SVMParameter("rbf", 10.0))
        #4 - 4  self.parameters.append(SVMParameter("sigmoid", 10.0))
        #5 - 29 self.parameters.append(SVMParameter("rbf", 100.0))
        #6 - 5 self.parameters.append(SVMParameter("sigmoid", 100.0))

        # 2019-07-06 13_51_03.456234
        #7 - 29 self.parameters.append(SVMParameter("rbf", 1000.0))

        #8 - 29 self.parameters.append(SVMParameter("rbf", 1.0, 0.1, {}))
        #9 - 29 self.parameters.append(SVMParameter("rbf", 1.0, 1, {}))
        #10 - 29 self.parameters.append(SVMParameter("rbf", 1.0, 10, {}))
        self.parameters.append(SVMParameter("rbf", 1.0, 100, {}))

        self.parameters.append(SVMParameter("rbf", 1.0, 1000, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 0.1, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 10, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 100, {}))

        self.parameters.append(SVMParameter("sigmoid", 100.0, 0.1, {}))
        self.parameters.append(SVMParameter("sigmoid", 100.0, 10, {}))
        self.parameters.append(SVMParameter("sigmoid", 100.0, 100, {}))
        self.parameters.append(SVMParameter("sigmoid", 10.0, 0.1, {}))
        self.parameters.append(SVMParameter("sigmoid", 10.0, 10, {}))

        self.parameters.append(SVMParameter("rbf", 1.0, 100, {}))

        self.parameters.append(SVMParameter("rbf", 1.0, 1000, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 0.1, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 10, {}))
        self.parameters.append(SVMParameter("rbf", 100.0, 100, {}))

        self.parameters.append(SVMParameter("sigmoid", 100.0, 0.1, {}))
        self.parameters.append(SVMParameter("sigmoid", 100.0, 10, {}))
        self.parameters.append(SVMParameter("sigmoid", 100.0, 100, {}))
        self.parameters.append(SVMParameter("sigmoid", 10.0, 0.1, {}))
        self.parameters.append(SVMParameter("sigmoid", 10.0, 10, {}))


        self.index = 0


