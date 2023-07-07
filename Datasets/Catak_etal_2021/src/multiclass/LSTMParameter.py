

class LSTMParameter:
    def __init__(self, embedding_units, unit, dropout, recurrent_dropout, lstm_activation, loss_func, optimizer, epochs, batch_size):

        #Embedding
        self.embedding_units = embedding_units

        #model
        self.units = unit
        self.dropout = dropout
        self.recurrent_dropout = recurrent_dropout
        self.lstm_activation = lstm_activation

        #model.compile
        self.loss_func = loss_func
        self.optimizer = optimizer

        #model.fit
        self.epochs = epochs
        self.batch_size = batch_size

class LSTM2Parameter:
    def __init__(self, embedding_units, unit, dropout, recurrent_dropout, lstm_activation, loss_func, optimizer, epochs, batch_size):

        #Embedding
        self.embedding_units = embedding_units

        #model
        self.units = unit
        self.dropout = dropout
        self.recurrent_dropout = recurrent_dropout
        self.lstm_activation = lstm_activation

        #model.compile
        self.loss_func = loss_func
        self.optimizer = optimizer

        #model.fit
        self.epochs = epochs
        self.batch_size = batch_size


class LSTMParameters:
    def __init__(self):
        # model

        self.parameters = []
        #2019-07-06 09_09_39.367144
        #1- 30
        self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 2, 50))
        # #2- X
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "relu", "categorical_crossentropy", "adam", 50, 50))
        # #3- 46
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 50, 50))
        # #4- X
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "softplus", "categorical_crossentropy", "adam", 50, 50))
        # #5- 35
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 50, 50))
        # #6- 31
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "softmax", "categorical_crossentropy", "adam", 50, 50))
        # #7- X
        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "linear", "categorical_crossentropy", "adam", 50, 50))
        #
        # # 2019-07-06 13_51_03.456234
        # #8- 31
        # self.parameters.append(LSTMParameter(16, 100, 0.1, 0.1, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # #9- 46
        # self.parameters.append(LSTMParameter(16, 100, 0.1, 0.1, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #10- 36
        # self.parameters.append(LSTMParameter(16, 100, 0.1, 0.1, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #11- 35
        # self.parameters.append(LSTMParameter(16, 100, 0.1, 0.1, "softmax", "categorical_crossentropy", "adam", 150, 50))
        #
        # #12- 37
        # self.parameters.append(LSTMParameter(16, 100, 0.3, 0.3, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # #13- 40
        # self.parameters.append(LSTMParameter(16, 100, 0.3, 0.3, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #14- 29
        # self.parameters.append(LSTMParameter(16, 100, 0.3, 0.3, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #15- 27
        # self.parameters.append(LSTMParameter(16, 100, 0.3, 0.3, "softmax", "categorical_crossentropy", "adam", 150, 50))
        #
        # #16- 44
        # self.parameters.append(LSTMParameter(16, 50, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #17- 44
        # self.parameters.append(LSTMParameter(32, 100, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #18- 47
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        #
        #
        # #19- 32
        # self.parameters.append(LSTMParameter(16, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 100, 25))
        # #20- 39
        # self.parameters.append(LSTMParameter(16, 300, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 100, 50))
        #
        # #21- 17
        # self.parameters.append(LSTMParameter(16, 200, 0.03, 0.03, "tanh", "categorical_crossentropy", "adam", 100, 50))
        # #22- 42
        # self.parameters.append(LSTMParameter(16, 200, 0.03, 0.03, "sigmoid", "categorical_crossentropy", "adam", 100, 50))
        # #23- 27
        # self.parameters.append(LSTMParameter(16, 200, 0.03, 0.03, "softsign", "categorical_crossentropy", "adam", 100, 50))
        # #24- 27
        # self.parameters.append(LSTMParameter(16, 200, 0.03, 0.03, "softmax", "categorical_crossentropy", "adam", 100, 50))
        #
        # #25 41
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #26 41
        # self.parameters.append(LSTMParameter(16, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 100))
        #
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "sgd", 150, 50))
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adagrad", 150, 50))
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adadelta", 150, 50))
        # self.parameters.append(LSTMParameter(32, 200, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "rmsprop", 150, 50))
        #
        # self.parameters.append(LSTMParameter(32, 50, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "sgd", 150, 50))
        # self.parameters.append(LSTMParameter(32, 50, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adagrad", 150, 50))
        # self.parameters.append(LSTMParameter(32, 50, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adadelta", 150, 50))
        # self.parameters.append(LSTMParameter(32, 50, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "rmsprop", 150, 50))

        # self.parameters.append(LSTMParameter(16, 100, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adagrad", 150, 50))
        # self.parameters.append(LSTMParameter(16, 100, 0.3, 0.3, "sigmoid", "categorical_crossentropy", "adagrad", 150, 50))

        self.index = 34


class LSTM2Parameters:
    def __init__(self):
        # model
        self.parameters = []

        # #2019-07-06 13_51_03.456234
        # #1- 35
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # #2- X
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "relu", "categorical_crossentropy", "adam", 150, 50))
        # #3- 32
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #4- X
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "softplus", "categorical_crossentropy", "adam", 150, 50))
        # #5- 37
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #6- 3
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "softmax", "categorical_crossentropy", "adam", 150, 50))
        # #7- X
        # self.parameters.append(LSTM2Parameter(16, 100, 0.2, 0.2, "linear", "categorical_crossentropy", "adam", 150, 50))
        #
        #
        # #2019-07-06 19_20_29.489964
        # #8- 35
        # self.parameters.append(LSTM2Parameter(16, 100, 0.1, 0.1, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # #9- 25
        # self.parameters.append(LSTM2Parameter(16, 100, 0.1, 0.1, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #10- 35
        # self.parameters.append(LSTM2Parameter(16, 100, 0.1, 0.1, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        # #11-35
        # self.parameters.append(LSTM2Parameter(16, 100, 0.3, 0.3, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # #12-27
        # self.parameters.append(LSTM2Parameter(16, 100, 0.3, 0.3, "sigmoid", "categorical_crossentropy", "adam", 150, 50))
        # #13-39
        # self.parameters.append(LSTM2Parameter(16, 100, 0.3, 0.3, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        #
        # #14 34
        # self.parameters.append(LSTM2Parameter(16, 100, 0.4, 0.4, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #15 37
        # self.parameters.append(LSTM2Parameter(16, 50,  0.4, 0.4, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        # #16 39
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #17 39
        # self.parameters.append(LSTM2Parameter(16, 50, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #18 38
        # self.parameters.append(LSTM2Parameter(16, 200, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #19 32
        # self.parameters.append(LSTM2Parameter(16, 300, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # #20 33
        # self.parameters.append(LSTM2Parameter(16, 100, 0.3, 0.3, "softsign", "categorical_crossentropy", "adam", 150, 100))
        # #21 37
        # self.parameters.append(LSTM2Parameter(32, 100, 0.3, 0.3, "softsign", "categorical_crossentropy", "adam", 150, 100))
        #
        # self.parameters.append(LSTM2Parameter(16, 15, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 10, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 5, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 2, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(32, 15, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 10, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 5, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 2, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(64, 15, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 10, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 5, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 2, 0.2, 0.2, "softsign", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "softsign", "categorical_crossentropy", "sgd", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "softsign", "categorical_crossentropy", "adagrad", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "softsign", "categorical_crossentropy", "adadelta", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "softsign", "categorical_crossentropy", "rmsprop", 150, 50))
        #
        #


        # self.parameters.append(LSTM2Parameter(16, 15, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 10, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 5, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 2, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(32, 15, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 10, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 5, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(32, 2, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(64, 15, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 10, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 5, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        # self.parameters.append(LSTM2Parameter(64, 2, 0.2, 0.2, "tanh", "categorical_crossentropy", "adam", 150, 50))
        #
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "tanh", "categorical_crossentropy", "sgd", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "tanh", "categorical_crossentropy", "adagrad", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "tanh", "categorical_crossentropy", "adadelta", 150, 50))
        # self.parameters.append(LSTM2Parameter(16, 25, 0.2, 0.2, "tanh", "categorical_crossentropy", "rmsprop", 150, 50))

        self.index = 34