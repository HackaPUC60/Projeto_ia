"""
@Author
  Willian Antunes
    HackaPuc60
    22/10/2020
"""
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from modulos import alfabeto
from modulos import extrator_proximidade
from modulos import extrator_posicao
from modulos import extrator_altura

captura = cv2.VideoCapture(0)

arquivo_proto = 'modelo/vggnet_rede.prototxt'
arquivo_pesos = 'modelo/modelo.caffemodel'

modelo = cv2.dnn.readNetFromCaffe(arquivo_proto, arquivo_pesos)

imagem_largura = 640
imagem_altura = 480
proporsao = imagem_largura / imagem_altura

entrada_altura = 368
entrada_largura = int(((proporsao * entrada_altura) * 8) // 8)
entrada_largura, entrada_altura

numero_pontos = 22
pares_pose = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 6], [6, 7], [7, 8],
              [0, 9], [9, 10], [10, 11], [11, 12], [0, 13], [13, 14], [14, 15],
              [15, 16], [0, 17], [17, 18], [18, 19], [19, 20]]

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'L', 'M', 'N', 'O', 'P',
          'Q', 'R', 'S', 'T', 'U', 'V', 'W']

cor_pontoA, cor_pontoB, cor_linha = (14, 201, 255), (255, 0, 128), (192, 192, 192)
cor_txtponto, cor_txtinicial, cor_txtandamento = (10, 216, 245), (255, 0, 128), (192, 192, 192)

tamanho_fonte, tamanho_linha, tamanho_circulo, espessura = 1, 1, 4, 2
fonte = cv2.FONT_HERSHEY_SIMPLEX

while (1):
    ret, frame = captura.read()
    cv2.flip(frame, 1, frame)
    frame_copia = np.copy(frame)

    tamanho = cv2.resize(frame, (imagem_largura, imagem_altura))
    mapa_suave = cv2.GaussianBlur(tamanho, (3, 3), 0, 0)
    fundo = np.uint8(mapa_suave > 0.1)

    entrada_blob = cv2.dnn.blobFromImage(frame, 1.0 / 255,
                                         (entrada_largura, entrada_altura),
                                         (0, 0, 0), swapRB=False, crop=False)

    modelo.setInput(entrada_blob)

    saida = modelo.forward()

    pontos = []

    for i in range(numero_pontos):
        mapa_confianca = saida[0, i, :, :]
        mapa_confianca = cv2.resize(mapa_confianca, (imagem_largura, imagem_altura))

        _, confianca, _, point = cv2.minMaxLoc(mapa_confianca)

        if confianca > 0.1:
            cv2.circle(frame_copia, (int(point[0]), int(point[1])),
                       tamanho_circulo, cor_pontoA, thickness=espessura,
                       lineType=cv2.FILLED)
            cv2.putText(frame_copia, "{}".format(i), (int(point[0]), int(point[1])),
                        fonte, .8,
                        cor_txtponto, 2, lineType=cv2.LINE_AA)

            pontos.append((int(point[0]), int(point[1])))
        else:
            pontos.append((0, 0))

    for par in pares_pose:
        parteA = par[0]
        parteB = par[1]

        if pontos[parteA] != (0, 0) and pontos[parteB] != (0, 0):
            cv2.line(frame, pontos[parteA], pontos[parteB], cor_linha,
                     tamanho_linha, lineType=cv2.LINE_AA)
            cv2.circle(frame, pontos[parteA], tamanho_circulo, cor_pontoA,
                       thickness=espessura, lineType=cv2.FILLED)
            cv2.circle(frame, pontos[parteB], tamanho_circulo, cor_pontoB,
                       thickness=espessura, lineType=cv2.FILLED)

            cv2.line(fundo, pontos[parteA], pontos[parteB], cor_linha,
                     tamanho_linha, lineType=cv2.LINE_AA)
            cv2.circle(fundo, pontos[parteA], tamanho_circulo, cor_pontoA,
                       thickness=espessura, lineType=cv2.FILLED)
            cv2.circle(fundo, pontos[parteB], tamanho_circulo, cor_pontoB,
                       thickness=espessura, lineType=cv2.FILLED)

    extrator_proximidade.posicoes = []

    # dedo polegar
    extrator_posicao.verificar_posicao_dedos(pontos[1:5], 'polegar', extrator_altura.verificar_altura_mao(pontos))

    # dedo indicador
    extrator_posicao.verificar_posicao_dedos(pontos[5:9], 'indicador', extrator_altura.verificar_altura_mao(pontos))

    # dedo médio
    extrator_posicao.verificar_posicao_dedos(pontos[9:13], 'medio', extrator_altura.verificar_altura_mao(pontos))

    # dedo anelar
    extrator_posicao.verificar_posicao_dedos(pontos[13:17], 'anelar', extrator_altura.verificar_altura_mao(pontos))

    # dedo mínimo
    extrator_posicao.verificar_posicao_dedos(pontos[17:21], 'minimo', extrator_altura.verificar_altura_mao(pontos))

    for i, a in enumerate(alfabeto.letras):
        if extrator_proximidade.verificar_proximidade_dedos(pontos) == alfabeto.letras[i]:
            cv2.putText(frame, 'Letra: ' + letras[i], (50, 50), fonte, 1,
                        cor_txtinicial, tamanho_fonte,
                        lineType=cv2.LINE_AA)
        else:
            cv2.putText(frame, 'Analisando', (250, 50), fonte, 1,
                        cor_txtandamento, tamanho_fonte,
                        lineType=cv2.LINE_AA)

    cv2.imshow("Video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()



