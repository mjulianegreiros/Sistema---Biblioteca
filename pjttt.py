from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aluno",
    database="BIBLIOTECA"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    linha7 = formulario.lineEdit_7.text()
    linha8 = formulario.lineEdit_8.text()
    
    print("Nome: ",linha1)
    print("Curso: ",linha2)
    print("Telef: ",linha3)
    print("Emp: ",linha4)
    print("Dev: ",linha5)
    print("Tombo: ",linha6)
    print("Título: ",linha7)
    print("Autor: ",linha8)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO fichas(Nome, Curso , Telefone , Emp , Dev , Tombo , Nome_do_livro , Autor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),str(linha7),str(linha8))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    
def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM FICHAS"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(9)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 9):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton_2.clicked.connect(funcao_principal)
formulario.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela=uic.loadUi("lista_de_cadastro.ui")

formulario.show()
app.exec()


