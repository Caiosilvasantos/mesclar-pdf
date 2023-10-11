import PyPDF2
import os

mesclar = PyPDF2.PdfMerger()

#os.listdir é para listar o que há dentro da pasta "arquivos"
listar_arquivos = os.listdir("arquivos")
listar_arquivos.sort()

for arquivo in listar_arquivos:
    if ".pdf" in arquivo:
        mesclar.append(f"arquivos/{arquivo}")

mesclar.write("PDF2 Final.pdf")        