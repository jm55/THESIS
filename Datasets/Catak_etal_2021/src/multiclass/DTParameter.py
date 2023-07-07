

class DTParameter:
    def __init__(self, random_state, min_samples_split, min_samples_leaf, max_depth):

        #Embedding
        self.random_state = random_state
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_depth = max_depth


class DTParameters:
    def __init__(self):
        # model
        self.parameters = []

        #2019-07-06 09_09_39.367144

        self.parameters.append(DTParameter(0, 3, 2, 1))
        self.parameters.append(DTParameter(0, 5, 2, 3))
        self.parameters.append(DTParameter(0, 10, 2, 7))

        self.parameters.append(DTParameter(0, 3, 3, 1))
        self.parameters.append(DTParameter(0, 5, 5, 3))
        self.parameters.append(DTParameter(0, 10, 7, 5))

        self.parameters.append(DTParameter(0, 10, 7, 7))
        self.parameters.append(DTParameter(0, 10, 7, 9))
        self.parameters.append(DTParameter(0, 3, 2, 1))
        self.parameters.append(DTParameter(0, 5, 2, 3))
        self.parameters.append(DTParameter(0, 10, 2, 7))

        self.parameters.append(DTParameter(0, 3, 3, 1))

        self.parameters.append(DTParameter(0, 3, 2, 1))
        self.parameters.append(DTParameter(0, 5, 2, 3))
        self.parameters.append(DTParameter(0, 10, 2, 7))

        self.parameters.append(DTParameter(0, 3, 3, 1))
        self.parameters.append(DTParameter(0, 5, 5, 3))
        self.parameters.append(DTParameter(0, 10, 7, 5))

        self.parameters.append(DTParameter(0, 10, 7, 7))
        self.parameters.append(DTParameter(0, 10, 7, 9))


        self.index = 0


