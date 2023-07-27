from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
from keras import preprocessing
from keras.utils import to_categorical
import numpy
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.layers.embeddings import Embedding
from keras.layers import Flatten
import matplotlib.pyplot as plt
import os
from keras import regularizers
import datetime
from keras.utils import plot_model
from keras.callbacks import EarlyStopping
from .ModelUtil import ModelUtil
from .LatexReporter import LatexReporter
from .LSTMParameter import LSTMParameters
from .LSTMParameter import LSTM2Parameters
from .SVMParameter import SVMParameters
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from .KNNParameter import KNNParameters
from sklearn.ensemble import RandomForestClassifier
from .RFParameter import RFParameters
from sklearn.tree import DecisionTreeClassifier
from .DTParameter import DTParameters
from sklearn.utils import class_weight
from sklearn.utils.class_weight import compute_class_weight



class AnalizeRunner:

    modelUtil = ModelUtil()
    latexReporter = LatexReporter()

    def startAnalize(self, X, y, path):


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.start2LayerLSTMAnalize(X_train, X_test, y_train, y_test, path)
        self.startLSTMAnalize(X_train, X_test, y_train, y_test, path)
        self.startSVMAnalize(X_train, X_test, y_train, y_test, path)
        self.startKNNAnalize(X_train, X_test, y_train, y_test, path)
        self.startDTAnalize(X_train, X_test, y_train, y_test, path)
        self.startRFAnalize(X_train, X_test, y_train, y_test, path)

    def startDTAnalize(self, X_train, X_test, y_train, y_test, path):
        dtPath = "DT\\"
        latex_file = self.createFolder(path + dtPath)

        params = DTParameters()

        index = params.index
        for param in params.parameters:

            analizePath = dtPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            matrix, report = self.dtModelFit(X_train, X_test, y_train, y_test, param)

            self.saveGResultFiles(matrix, report, (path + analizePath))
            self.createAndWriteDTLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()

    def startRFAnalize(self, X_train, X_test, y_train, y_test, path):
        rfPath = "RF\\"
        latex_file = self.createFolder(path + rfPath)

        params = RFParameters()

        index = params.index
        for param in params.parameters:

            analizePath = rfPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            matrix, report = self.rfModelFit(X_train, X_test, y_train, y_test, param)

            self.saveGResultFiles(matrix, report, (path + analizePath))
            self.createAndWriteRFLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()

    def startKNNAnalize(self, X_train, X_test, y_train, y_test, path):
        knnPath = "KNN\\"
        latex_file = self.createFolder(path + knnPath)

        params = KNNParameters()

        index = params.index
        for param in params.parameters:

            analizePath = knnPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            matrix, report = self.knnModelFit(X_train, X_test, y_train, y_test, param)

            self.saveGResultFiles(matrix, report, (path + analizePath))
            self.createAndWriteKNNLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()

    def startSVMAnalize(self, X_train, X_test, y_train, y_test, path):

        svmPath = "SVM\\"
        latex_file = self.createFolder(path + svmPath)

        params = SVMParameters()

        index = params.index
        for param in params.parameters:

            analizePath = svmPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            matrix, report = self.svmModelFit(X_train, X_test, y_train, y_test, param)

            self.saveGResultFiles(matrix, report, (path + analizePath))
            self.createAndWriteSVMLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()


    def startLSTMAnalize(self, X_train, X_test, y_train, y_test, path):

        lstmPath = "LSTM\\"
        latex_file = self.createFolder(path + lstmPath)

        params = LSTMParameters()

        index = params.index
        for param in params.parameters:

            analizePath = lstmPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            model, history = self.oneLayerlstmModelFit(X_train, y_train, param)
            prediction = model.predict_classes(X_test)
            matrix = confusion_matrix(y_test, prediction)
            report = classification_report(y_test, prediction)
            self.saveLSTMResultFiles(model, history, matrix, report, (path + analizePath))

            self.createAndWriteOneLayerLSTMLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()

    def start2LayerLSTMAnalize(self, X_train, X_test, y_train, y_test, path):

        lstmPath = "LSTM-2\\"
        latex_file = self.createFolder(path + lstmPath)

        params = LSTM2Parameters()

        index = params.index
        for param in params.parameters:

            analizePath = lstmPath + "Analize"+ str(index) +"\\"
            os.makedirs(path + analizePath)

            model, history = self.twoLayerlstmModelFit(X_train, y_train, param)
            prediction = model.predict_classes(X_test)
            matrix = confusion_matrix(y_test, prediction)
            report = classification_report(y_test, prediction)
            self.saveLSTMResultFiles(model, history, matrix, report, (path + analizePath))

            self.createAndWriteTwoLayerLSTMLatex(latex_file, report, matrix, param, index)

            index = index + 1

        latex_file.close()

    def twoLayerlstmModelFit(self, X_train, y_train, param):

        model = Sequential()
        model.add(Embedding(342, param.embedding_units, input_length=342))
        model.add(LSTM(param.units, activation=param.lstm_activation, return_sequences=True))
        model.add(Dropout(param.dropout))
        model.add(LSTM(param.units, activation= param.lstm_activation  ,dropout=param.dropout, recurrent_dropout=param.recurrent_dropout))
        model.add(Dense(8, activation='softmax'))
#        model.add(Dense(2, activation="softmax", kernel_regularizer=regularizers.l2(0.01),
 #                       activity_regularizer=regularizers.l1(0.01)))

        # compile the model
        model.compile(loss=param.loss_func, optimizer=param.optimizer, metrics=['acc'])
        # summarize the model
        model.summary()

        es = EarlyStopping(monitor='val_loss', verbose=1, min_delta=0.0001, patience=2, mode='auto')
        # evaluate the model

        history = model.fit(X_train, to_categorical(y_train), epochs=param.epochs, batch_size=param.batch_size, verbose=1,
                            validation_split=0.3, callbacks=[es])

        return model, history

    def oneLayerlstmModelFit(self, X_train, y_train, param):

        # define the model
        model = Sequential()
        model.add(Embedding(342, param.embedding_units, input_length=342))

        model.add(LSTM(param.units, activation= param.lstm_activation  ,dropout=param.dropout, recurrent_dropout=param.recurrent_dropout))
        model.add(Dense(8, activation='softmax'))
        # compile the model
        model.compile(loss=param.loss_func, optimizer=param.optimizer, metrics=['acc'])
        # summarize the model
        model.summary()

        es = EarlyStopping(monitor='val_loss', verbose=1, min_delta=0.0001, patience=2,  mode='auto')
        # evaluate the model

        history = model.fit(X_train, to_categorical(y_train), epochs=param.epochs, batch_size=param.batch_size, verbose=1,
                            validation_split=0.3, callbacks=[es])

        return model, history


    def dtModelFit(self, X_train, X_test, y_train, y_test, param):
        clf = DecisionTreeClassifier(random_state=param.random_state, min_samples_split=param.min_samples_split,
                                     min_samples_leaf=param.min_samples_leaf, max_depth=param.max_depth)
        clf.fit(X_train, y_train)

        predictions = clf.predict_proba(X_test)

        matrix = confusion_matrix(y_test, predictions.argmax(axis=1))
        report = classification_report(y_test, predictions.argmax(axis=1))

        return matrix, report

    def rfModelFit(self, X_train, X_test, y_train, y_test, param):

        class_weights = compute_class_weight('balanced', numpy.unique(y_train), y_train)

        dic = {0: class_weights[0], 1: class_weights[1], 2: class_weights[2], 3: class_weights[3], 4: class_weights[4],
         5: class_weights[5], 6: class_weights[6], 7: class_weights[7]}
        param.class_weights = dic

        clf = RandomForestClassifier(n_estimators=param.n_estimators, max_depth=param.max_depth,
                                     min_samples_split=param.min_samples_split, min_samples_leaf=param.min_samples_leaf,
                                     class_weight=dic)
        clf.fit(X_train, y_train)

        predictions = clf.predict_proba(X_test)

        matrix = confusion_matrix(y_test, predictions.argmax(axis=1))
        report = classification_report(y_test, predictions.argmax(axis=1))

        return matrix, report

    def knnModelFit(self, X_train, X_test, y_train, y_test, param):
        clf = KNeighborsClassifier(n_neighbors=param.n_neighbors, p=param.p,
                                   algorithm=param.algorithm)
        clf.fit(X_train, y_train)

        predictions = clf.predict_proba(X_test)

        matrix = confusion_matrix(y_test, predictions.argmax(axis=1))
        report = classification_report(y_test, predictions.argmax(axis=1))

        return matrix, report


    def svmModelFit(self, X_train, X_test, y_train, y_test, param):

        class_weights = compute_class_weight('balanced', numpy.unique(y_train), y_train)

        dic = {0: class_weights[0], 1: class_weights[1], 2: class_weights[2], 3: class_weights[3], 4: class_weights[4],
         5: class_weights[5], 6: class_weights[6], 7: class_weights[7]}
        param.class_weights = dic
        clf = SVC(probability=True, kernel=param.kernel, C=param.c, class_weight=dic)
        clf.fit(X_train, y_train)

        predictions = clf.predict_proba(X_test)

        matrix = confusion_matrix(y_test, predictions.argmax(axis=1))
        report = classification_report(y_test, predictions.argmax(axis=1))

        return matrix, report

    def createAndWriteOneLayerLSTMLatex(self, latex_file, report, matrix, param, index):
        figurePath = "LSTM/Analize" + str(index)

        self.writeToFile(self.latexReporter.prepareLSTMSectionTitle(index, "Tek"), latex_file)
        self.writeToFile(self.latexReporter.prepareLSTMDef("Tek"), latex_file)

        self.writeToFile(self.latexReporter.prepareLSTMParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefFigures(index), latex_file)
        self.writeToFile(self.latexReporter.prepareTrainFigure(figurePath, index, ""), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "LSTM"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "LSTM"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "LSTM"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "LSTM"), latex_file)

    def createAndWriteTwoLayerLSTMLatex(self, latex_file, report, matrix, param, index):
        figurePath = "LSTM-2/Analize" + str(index)

        self.writeToFile(self.latexReporter.prepareLSTMSectionTitle(index, "İki"), latex_file)
        self.writeToFile(self.latexReporter.prepareLSTMDef("İki"), latex_file)

        self.writeToFile(self.latexReporter.prepare2LSTMParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefFigures(index), latex_file)
        self.writeToFile(self.latexReporter.prepareTrainFigure(figurePath, index, "2"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "LSTM2"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "LSTM2"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "LSTM2"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "LSTM2"), latex_file)

    def createAndWriteSVMLatex(self, latex_file, report, matrix, param, index):

        self.writeToFile(self.latexReporter.prepareGSectionTitle(index, "SVM"), latex_file)
        self.writeToFile(self.latexReporter.prepareGDef("SVM"), latex_file)

        self.writeToFile(self.latexReporter.prepareSVMParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "SVM"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "SVM"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "SVM"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "SVM"), latex_file)

    def createAndWriteKNNLatex(self, latex_file, report, matrix, param, index):

        self.writeToFile(self.latexReporter.prepareGSectionTitle(index, "kNN"), latex_file)
        self.writeToFile(self.latexReporter.prepareGDef("kNN"), latex_file)

        self.writeToFile(self.latexReporter.prepareKNNParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "kNN"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "kNN"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "kNN"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "kNN"), latex_file)

    def createAndWriteRFLatex(self, latex_file, report, matrix, param, index):

        self.writeToFile(self.latexReporter.prepareGSectionTitle(index, "RF"), latex_file)
        self.writeToFile(self.latexReporter.prepareGDef("RF"), latex_file)

        self.writeToFile(self.latexReporter.prepareRFParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "RF"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "RF"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "RF"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "RF"), latex_file)

    def createAndWriteDTLatex(self, latex_file, report, matrix, param, index):

        self.writeToFile(self.latexReporter.prepareGSectionTitle(index, "DT"), latex_file)
        self.writeToFile(self.latexReporter.prepareGDef("DT"), latex_file)

        self.writeToFile(self.latexReporter.prepareDTParameters(param), latex_file)

        self.writeToFile(self.latexReporter.prepareDefConfMatrix(index, "DT"), latex_file)
        self.writeToFile(self.latexReporter.prepareConfisuonMatrix(matrix, index, "DT"), latex_file)

        self.writeToFile(self.latexReporter.prepareDefResultTable(index, "DT"), latex_file)
        self.writeToFile(self.latexReporter.prepareResultTable(report, index, "DT"), latex_file)

    def writeToFile(self, latexStr, file):
        file.write(str(latexStr))
        file.write("\n\n")

    def createFolder(self, fullPath):
        os.makedirs(fullPath)
        return open(fullPath + "LatexFile.txt", "w")

    def saveLSTMResultFiles(self, model, history, matrix, report, analizePath):
        model.save(analizePath + "Model")
        self.modelUtil.saveAccHistory(history, analizePath)
        self.modelUtil.saveLostHistory(history, analizePath)
        self.modelUtil.saveModelLayer(model, analizePath)
        self.modelUtil.saveConfisuonMatrixAndResult(matrix, report, analizePath)

    def saveGResultFiles(self, matrix, report, analizePath):
        self.modelUtil.saveConfisuonMatrixAndResult(matrix, report, analizePath)
