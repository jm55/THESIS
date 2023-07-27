

class RFParameter:
    def __init__(self, n_estimators, max_depth, min_samples_split, min_samples_leaf = 1, class_weights={}):

        #Embedding
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.class_weights = class_weights



class RFParameters:
    def __init__(self):
        # model
        self.parameters = []
        # 2019-07-06 09_09_39.367144
        #1 - 49 self.parameters.append(RFParameter(50))
        #2 - 51 self.parameters.append(RFParameter(100))

        # 2019-07-06 13_51_03.456234
        #3 - 52 self.parameters.append(RFParameter(250))

        #4 - 51 self.parameters.append(RFParameter(500))

        self.parameters.append(RFParameter(1, None, 2))
        self.parameters.append(RFParameter(2, None, 2))
        self.parameters.append(RFParameter(3, None, 2))
        self.parameters.append(RFParameter(6, None, 2))
        self.parameters.append(RFParameter(16, None, 2))

        self.parameters.append(RFParameter(32, None, 2))
        self.parameters.append(RFParameter(64, None, 2))
        self.parameters.append(RFParameter(100, None, 2))
        self.parameters.append(RFParameter(200, None, 2))
        self.parameters.append(RFParameter(500, None, 2))
        self.parameters.append(RFParameter(1, None, 2))
        self.parameters.append(RFParameter(2, None, 2))
        self.parameters.append(RFParameter(3, None, 2))
        self.parameters.append(RFParameter(6, None, 2))
        self.parameters.append(RFParameter(16, None, 2))

        self.parameters.append(RFParameter(32, None, 2))
        self.parameters.append(RFParameter(64, None, 2))
        self.parameters.append(RFParameter(100, None, 2))
        self.parameters.append(RFParameter(200, None, 2))
        self.parameters.append(RFParameter(500, None, 2))
        #
        # self.parameters.append(RFParameter(200,1, 2))
        # self.parameters.append(RFParameter(200,3, 2))
        #
        # self.parameters.append(RFParameter(200,7, 2))
        #
        # self.parameters.append(RFParameter(200,11, 2))
        # self.parameters.append(RFParameter(200,15, 2))
        # self.parameters.append(RFParameter(200,19, 2))
        # self.parameters.append(RFParameter(200,23, 2))
        # self.parameters.append(RFParameter(200,27, 2))
        # self.parameters.append(RFParameter(200,32, 2))
        #
        # self.parameters.append(RFParameter(200, None, 2))
        # self.parameters.append(RFParameter(200, None, 3))
        # self.parameters.append(RFParameter(200, None, 5))
        # self.parameters.append(RFParameter(200, None, 7))
        # self.parameters.append(RFParameter(200, None, 9))
        # self.parameters.append(RFParameter(200, None, 15))
        # self.parameters.append(RFParameter(200, None, 25))
        #
        # self.parameters.append(RFParameter(200, None, 2, 1))
        # self.parameters.append(RFParameter(200, None, 2, 2))
        # self.parameters.append(RFParameter(200, None, 2, 3))
        # self.parameters.append(RFParameter(200, None, 2, 5))
        # self.parameters.append(RFParameter(200, None, 2, 9))
        # self.parameters.append(RFParameter(200, None, 2, 15))
        # self.parameters.append(RFParameter(200, None, 2, 25))





        self.index = 0


