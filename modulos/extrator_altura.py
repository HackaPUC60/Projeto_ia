"""
@Author Willian Antunes
HackaPuc60
21/10/2020
"""


class Extrator_Altura:
    def __init__(self):
        pass

    @staticmethod
    def verificar_altura_mao(pontos):
        punho_V = 0
        ponta_polegar_V = 0
        ponta_indicador_V = 0
        ponta_medio_V = 0
        ponta_anelar_V = 0
        ponta_minimo_V = 0

        for indx, p in enumerate(pontos):
            if indx == 0:
                punho_V = p[1]
            if indx == 4:
                # ponta do polegar
                ponta_polegar_V = p[1]
            if indx == 8:
                # ponta do indicador
                ponta_indicador_V = p[1]
            if indx == 12:
                # ponta do medio
                ponta_medio_V = p[1]
            if indx == 15:
                # ponta do anelar
                ponta_anelar_V = p[1]
            if indx == 20:
                #  ponta do minimo
                ponta_minimo_V = p[1]
        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        # COMPARANDO NA VERITICAL
        if ponta_polegar_V < punho_V and ponta_indicador_V < punho_V and ponta_medio_V < punho_V and ponta_anelar_V < \
                punho_V and ponta_minimo_V < punho_V:
            return 'acima'
        else:
            return 'abaixo'
