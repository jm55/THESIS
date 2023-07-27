class LatexReporter:


    def prepareLSTMSectionTitle(self, index, alg):
        return "\\subsubsection {"+str(alg)+" Katmanlı LSTM Analiz-" + str(index) +" Sonuçları}"

    def prepareGSectionTitle(self, index, alg):
        return "\\subsubsection {"+str(alg)+" Analiz-" + str(index) +" Sonuçları}"

    def prepareLSTMDef(self, prefix):
        return str(prefix) + " katmanlı bir LSTM modeli oluşturulmuştur. Bu model 0-7 arasında bir çıktı üretmektedir. Bu değerler zararlı yazılım türlerini temsil etmektedir."

    def prepareGDef(self, prefix):
        return str(prefix) + " algoritması kullanılarak bir sınıflandırma modeli oluşturulmuştur. Bu model 0-7 arasında bir çıktı üretmektedir. Bu değerler zararlı yazılım türlerini temsil etmektedir."

    def prepareLSTMParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item Embedding units: """ + str(param.embedding_units) + """
                         \\item units: """ + str(param.units) + """
                         \\item dropout: """ + str(param.dropout) + """
                         \\item recurrent_dropout: """ + str(param.recurrent_dropout) + """
                         \\item activation: """ + param.lstm_activation + """
                         \\item loss_func: """ + param.loss_func + """
                         \\item optimizer: """ + param.optimizer + """
                         \\item epochs: """ + str(param.epochs) + """
                         \\item batch_size: """ + str(param.batch_size) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepare2LSTMParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item Embedding units: """ + str(param.embedding_units) + """
                         \\item units: """ + str(param.units) + """
                         \\item dropout: """ + str(param.dropout) + """
                         \\item activation: """ + param.lstm_activation + """
                         \\item loss_func: """ + param.loss_func + """
                         \\item optimizer: """ + param.optimizer + """
                         \\item epochs: """ + str(param.epochs) + """
                         \\item batch_size: """ + str(param.batch_size) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepareSVMParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item kernel: """ + str(param.kernel) + """
                         \\item C: """ + str(param.c) + """
                         \\item gamma: """ + str(param.gamma) + """
                         \\item class_weights: """ + str(param.class_weights) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepareKNNParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item n_neighbors: """ + str(param.n_neighbors) + """
                         \\item p: """ + str(param.p) + """
                         \\item algorithm: """ + str(param.algorithm) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepareRFParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item n_estimators: """ + str(param.n_estimators) + """
                         \\item max_depth: """ + str(param.max_depth) + """
                         \\item min_samples_split: """ + str(param.min_samples_split) + """
                         \\item min_samples_leaf: """ + str(param.min_samples_leaf) + """
                         \\item class_weight: """ + str(param.class_weights) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepareDTParameters(self, param):
        latexStr = """Bu model oluşturulurken kullanılan parametreler aşağıdadır.
                     \\begin{itemize}[noitemsep,nolistsep]
                         \\item random_state: """ + str(param.random_state) + """
                         \\item min_samples_split: """ + str(param.min_samples_split) + """
                         \\item max_depth: """ + str(param.max_depth) + """
                     \\end{itemize}"""

        return latexStr.replace("_", "\\_")

    def prepareDefFigures(self, index):
        latexStr = """İlgili parametreler kullanılarak oluşturulan modelin eğitim geçmişi, doğruluk (accuracy) ve kayıp (loss) grafikleri 
        Şekil \\ref{fig:lstm_model_""" + str(index) + """_acc_lost}‘ de verilmiştir."""
        return latexStr

    def prepareTrainFigure(self, analizePath, index, suffix):
        return """\\begin{figure}[H]
             \centering
             \\begin{subfigure}[b]{0.48\\textwidth}
                 \includegraphics[width=\\textwidth]{./Figures/""" + analizePath + """/acc.eps}
                 \caption{Doğruluk(accurancy) grafiği}
             \end{subfigure}
             ~ 
             \\begin{subfigure}[b]{0.48\\textwidth}
                 \includegraphics[width=\\textwidth]{./Figures/""" + analizePath + """/loss.eps}
                 \caption{Kayıp(loss) grafiği}
             \end{subfigure}
         	~ 
             \caption{LSTM""" + str(suffix) + """ Model-""" + str(index) + """ doğruluk-kayıp grafikleri}
             \label{fig:lstm_model_""" + str(index) + """_acc_lost}
             \end{figure}"""

    def prepareDefConfMatrix(self, index, alg):
        return """Eğitilen sınıflandırma modelinin test edilmesi sonucunda elde edilen Hata Matris (Confusion Matrix) bilgileri 
        Tablo \\ref{tablo_""" + str(alg) + """_conf_matrix_Model-""" + str(index) + """}‘ de verilmiştir."""

    def prepareConfisuonMatrix(self, matrix, index, alg):

        return """\\begin{table}[htb]
            \\caption{""" + str(alg) + """ Model-""" + str(index) + """ Analiz Hata Matrisi}
        	\\label{tablo_""" + str(alg) + """_conf_matrix_Model-""" + str(index) + """} 
            \\begin{center}
                \\footnotesize\\begin{tabular}{|c|c|c|c|c|c|c|c|}\hline
                 """+str(matrix[0][0])+""" & """+str(matrix[0][1])+""" & """+str(matrix[0][2])+""" & """+str(matrix[0][3])+""" & """+str(matrix[0][4])+""" & """+str(matrix[0][5])+""" & """+str(matrix[0][6])+""" & """+str(matrix[0][7])+""" \\\\ \hline
                 """+str(matrix[1][0])+""" & """+str(matrix[1][1])+""" & """+str(matrix[1][2])+""" & """+str(matrix[1][3])+""" & """+str(matrix[1][4])+""" & """+str(matrix[1][5])+""" & """+str(matrix[1][6])+""" & """+str(matrix[1][7])+""" \\\\ \hline
                 """+str(matrix[2][0])+""" & """+str(matrix[2][1])+""" & """+str(matrix[2][2])+""" & """+str(matrix[2][3])+""" & """+str(matrix[2][4])+""" & """+str(matrix[2][5])+""" & """+str(matrix[2][6])+""" & """+str(matrix[2][7])+""" \\\\ \hline
                 """+str(matrix[3][0])+""" & """+str(matrix[3][1])+""" & """+str(matrix[3][2])+""" & """+str(matrix[3][3])+""" & """+str(matrix[3][4])+""" & """+str(matrix[3][5])+""" & """+str(matrix[3][6])+""" & """+str(matrix[3][7])+""" \\\\ \hline
                 """+str(matrix[4][0])+""" & """+str(matrix[4][1])+""" & """+str(matrix[4][2])+""" & """+str(matrix[4][3])+""" & """+str(matrix[4][4])+""" & """+str(matrix[4][5])+""" & """+str(matrix[4][6])+""" & """+str(matrix[4][7])+""" \\\\ \hline
                 """+str(matrix[5][0])+""" & """+str(matrix[5][1])+""" & """+str(matrix[5][2])+""" & """+str(matrix[5][3])+""" & """+str(matrix[5][4])+""" & """+str(matrix[5][5])+""" & """+str(matrix[5][6])+""" & """+str(matrix[5][7])+""" \\\\ \hline
                 """+str(matrix[6][0])+""" & """+str(matrix[6][1])+""" & """+str(matrix[6][2])+""" & """+str(matrix[6][3])+""" & """+str(matrix[6][4])+""" & """+str(matrix[6][5])+""" & """+str(matrix[6][6])+""" & """+str(matrix[6][7])+""" \\\\ \hline
                 """+str(matrix[7][0])+""" & """+str(matrix[7][1])+""" & """+str(matrix[7][2])+""" & """+str(matrix[7][3])+""" & """+str(matrix[7][4])+""" & """+str(matrix[7][5])+""" & """+str(matrix[7][6])+""" & """+str(matrix[7][7])+""" \\\\ \hline
                \end{tabular} 
            \end{center}
        \end{table}"""


    def prepareDefResultTable(self, index, alg):
        return """Eğitilen sınıflandırma modelinin test edilmesi sonucunda elde edilen analiz sonuçları 
        Tablo \\ref{tablo_""" + str(alg) + """_result_Model-"""+str(index)+"""}' de gösterilmektedir."""

    def prepareResultTable(self, report, index, alg):

        arr = report.split("\n\n")
        values = arr[1].split("\n")

        adware = values[0].split()
        backdoor = values[1].split()
        downloader = values[2].split()
        dropper = values[3].split()
        spyware = values[4].split()
        trojan = values[5].split()
        virus = values[6].split()
        worm = values[7].split()

        avg = arr[2].split()

        latexStr = """\\begin{table}[htb]
        	      \\caption{""" + str(alg) + """ Model-"""+str(index)+""" Sınıflandırma Analiz Sonuçları}
	              \\label{tablo_""" + str(alg) + """_result_Model-"""+str(index)+"""} 
                    \\begin{center}
                        \\footnotesize\\begin{tabular}{|c|c|c|c|}\hline
                                        &Hassasiyet  &Anımsama &F1 \\\\ \hline
                            Adware  	&""" + adware[1] + """ 		 &""" +adware[2] + """     &""" +adware[3] + """\\\\ \hline
                            Backdoor    &""" + backdoor[1]+ """ 		 &""" + backdoor[2]+ """     &""" + backdoor[3]+ """\\\\ \hline
                            Downloader  &""" + downloader[1]+ """ 		 &""" + downloader[2]+ """     &""" + downloader[3]+ """\\\\ \hline
                            Dropper     &""" + dropper[1]+ """ 		 &""" + dropper[2]+ """     &""" + dropper[3]+ """\\\\ \hline
                            Spyware     &""" + spyware[1]+ """ 		 &""" + spyware[2]+ """     &""" + spyware[3]+ """\\\\ \hline
                            Trojan      &""" + trojan[1]+ """ 		 &""" + trojan[2]+ """     &""" + trojan[3]+ """\\\\ \hline
                            Virus       &""" + virus[1]+ """ 		 &""" + virus[2]+ """     &""" + virus[3]+ """\\\\ \hline
                            Worm        &""" + worm[1]+ """ 		 &""" + worm[2]+ """     &""" + worm[3]+ """\\\\ \hline
                        \end{tabular} 
                    \end{center}
                \end{table}

                Farklı modellerin karşılaştırılmasında kullanabileceğimiz, 
                Tablo \\ref{tablo_""" + str(alg) + """_result_Model-"""+str(index)+"""}' da gösterilen verilen ortalama bilgileri 
                Tablo \\ref{tablo_""" + str(alg) + """_result_sum_Model-"""+str(index)+"""}' da gösterilmektedir.

                \\begin{table}[htb]
                         \\begin{center}
        	             \\caption{""" + str(alg) + """ Model-"""+str(index)+""" Analiz Sonuç Ortalaması}
	                      \\label{tablo_""" + str(alg) + """_result_sum_Model-"""+str(index)+"""} 
                          \\footnotesize\\begin{tabular}{|c|c|c|c|}\hline
                            Ortalama        &""" + avg[3] + """ &""" + avg[4] + """  &""" + avg[5] + """\\\\ \hline
                                \end{tabular} 
                            \end{center}
                        \end{table}"""
        return latexStr

