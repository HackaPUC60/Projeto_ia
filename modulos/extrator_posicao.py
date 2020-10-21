"""
@Author Willian Antunes
HackaPuc60
21/10/2020

Para verificar se os dedos estão dobrados ou esticados,
esta função faz a comparação da distancia entre pontos
e adiciona a lista de posições se o dedo está esticado, acima ou abaixo da base do dedo se está próximo ou afastado do dedo subsequente.
Para o dedo polegar, precisa de uma verificação adicional para saber se está esticado ou dobrado
comparando a diferença dos pontos na vertical e na horizontal
"""


class Extrator_Posicao:
    def __init__(self):
        self.pontos = []
        self.posicoes = []

    def verificar_posicao_dedos(self, pontos, dedo, mao):
        for indx, p in enumerate(reversed(pontos)):
            if indx == 2:
                # base do dedo
                baseDedo_V = p[1]
                baseDedo_H = p[0]
            if indx == 1:
                pontoAnterior_H = p[0]
            if indx == 0:
                # ponta do dedo
                pontaDedo_V = p[1]
                pontaDedo_H = p[0]

        if mao == 'acima':  # se a posição da mão está voltada para cima
            if dedo == 'polegar':  # o dedo polegar se move mais na horizontal do que na vertical
                if pontaDedo_H <= pontoAnterior_H:  # se a ponta do dedo polegar na horizontal for menor que o ponto anterior dele, então está dobrado
                    if (
                            baseDedo_H - pontaDedo_H) > 70:  # se o dedo estiver muito dobrado, então está esticado na horizontal
                        return self.posicoes.append('esticado horizontal')
                    elif (baseDedo_H - pontaDedo_H) <= 30:
                        return self.posicoes.append('esticado vertical')
                    else:  # senão está dobrado
                        return self.posicoes.append('dobrado')
                elif pontaDedo_V < baseDedo_V:  # se a ponta do dedo na vertical for menor que a base, então o dedo está esticado
                    return self.posicoes.append('esticado vertical')
                else:  # senão está dobrado
                    return self.posicoes.append('dobrado')

            elif pontaDedo_V < baseDedo_V:  # se o dedo não for o polegar, então verifica se a ponta do dedo na vertical for menor que a base, então o dedo está esticado
                return self.posicoes.append('esticado vertical')
            else:  # senão está dobrado
                return self.posicoes.append('dobrado')

        else:  # se a posição da mão estiver "abaixo"
            if dedo == 'polegar':  # o dedo polegar se move mais na horizontal do que na vertical
                if (
                        baseDedo_H - pontaDedo_H) < 70:  # verificar se o ponto está muito a esquerda: se o resultado for maior que 70
                    return self.posicoes.append('esticado horizontal')
                elif (baseDedo_H - pontaDedo_H) >= 30:
                    return self.posicoes.append('esticado vertical')
                else:  # senão está dobrado
                    return self.posicoes.append('dobrado')

            elif pontaDedo_V > baseDedo_V:  # se o dedo não for o polegar, então verifica se a ponta do dedo na vertical for menor que a base, então o dedo está esticado
                return self.posicoes.append('esticado vertical')
            else:  # senão está dobrado
                return self.posicoes.append('dobrado')

    @staticmethod
    def verificar_posicao_corpo(pontos):
        posicao1 = 0
        posicao2 = 0

        for indx, p in enumerate(pontos):
            if indx == 0:
                posicao1 = p[0] + p[1]
                print('posicao1', posicao1)
            if indx == 1:
                posicao2 = p[0] + p[1]
                print('posicao2', posicao2)

        if (posicao2 - posicao1) >= 0:
            return 'esticado'
        else:
            return 'dobrado'
