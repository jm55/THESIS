from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd
from keras import preprocessing
from keras.utils import to_categorical

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


class ModelUtil:

    def saveConfisuonMatrixAndResult(self, matrix, report, filePath):
        cm_file = open(filePath + "Result_report_matrix.txt", "w")
        cm_file.write(str(matrix))
        cm_file.write("\n\n")
        cm_file.write(report)
        cm_file.close()
        print(matrix)
        print(report)

    def saveModelLayer(self, model, filePath):
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        image = filePath + "img"
        plot_model(model, show_layer_names= False, show_shapes=True, to_file=image + ".png")
        plot_model(model, show_shapes=True, to_file=image + ".eps")

    def saveLostHistory(self, history, filePath):
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.ylabel('kayip', fontsize=18)
        plt.xlabel('devir', fontsize=18)
        plt.legend(['eğitim', 'doğrulama'], loc='upper left')
        plt.savefig(filePath + "loss.png")
        plt.savefig(filePath + "loss.eps")
        plt.close()

    def saveAccHistory(self, history, filePath):
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.ylabel('doğruluk', fontsize=18)
        plt.xlabel('devir', fontsize=18)
        plt.legend(['eğitim', 'doğrulama'], loc='upper left')
        plt.savefig(filePath + "acc.png")
        plt.savefig(filePath + "acc.eps")
        # plt.show()
        plt.close()