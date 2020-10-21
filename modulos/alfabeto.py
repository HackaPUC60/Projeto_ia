"""
@Author Willian Antunes
HackaPuc60
21/10/2020

não foram usadas as letras: H, J, K, X, ,Y , Z
devido ao movimento adicional para a execução correta das letras.
Estas letras podem ser analisadas em uma função diferente, com transicao entre os movimentos
"""


class Alfabeto:
    def __init__(self):
        self.A = ['polegar esticado vertical: afastado do indicador', 'indicador dobrado: proximo ao medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.B = ['polegar dobrado: afastado do indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: proximo ao anelar', 'anelar esticado vertical: proximo ao minimo',
                  'minimo esticado vertical: proximo ao anelar']
        self.C = ['polegar esticado horizontal: afastado do indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: proximo ao anelar', 'anelar esticado vertical: proximo ao minimo',
                  'minimo esticado vertical: proximo ao anelar']
        self.D = ['polegar esticado horizontal: afastado do indicador',
                  'indicador esticado vertical: afastado do medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.E = ['polegar dobrado: afastado do indicador', 'indicador dobrado: proximo ao medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.F = ['polegar esticado vertical: proximo ao indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.G = ['polegar esticado vertical: proximo ao indicador', 'indicador esticado vertical: afastado do medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.I = ['polegar dobrado: proximo ao indicador', 'indicador dobrado: proximo ao medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: afastado do minimo',
                  'minimo esticado vertical: afastado do anelar']
        self.L = ['polegar esticado vertical: afastado do indicador', 'indicador esticado vertical: afastado do medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.M = ['polegar esticado vertical: proximo ao indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: proximo ao anelar', 'anelar esticado vertical: proximo ao minimo',
                  'minimo esticado vertical: proximo ao anelar']
        self.N = ['polegar esticado horizontal: afastado do indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.O = ['polegar esticado horizontal: afastado do indicador', 'indicador dobrado: proximo ao medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.P = ['polegar esticado vertical: afastado do indicador', 'indicador esticado vertical: afastado do medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.Q = ['polegar esticado vertical: afastado do indicador', 'indicador esticado vertical: afastado do medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: afastado do minimo',
                  'minimo esticado vertical: afastado do anelar']
        self.R = ['polegar dobrado: afastado do indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.S = ['polegar dobrado: proximo ao indicador', 'indicador dobrado: proximo ao medio',
                  'medio dobrado: proximo ao anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.T = ['polegar esticado horizontal: afastado do indicador', 'indicador dobrado: afastado do medio',
                  'medio esticado vertical: proximo ao anelar', 'anelar esticado vertical: proximo ao minimo',
                  'minimo esticado vertical: proximo ao anelar']
        self.U = ['polegar esticado horizontal: afastado do indicador', 'indicador esticado vertical: proximo ao medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.V = ['polegar esticado horizontal: afastado do indicador',
                  'indicador esticado vertical: afastado do medio',
                  'medio esticado vertical: afastado do anelar', 'anelar dobrado: proximo ao minimo',
                  'minimo dobrado: proximo ao anelar']
        self.W = ['polegar esticado horizontal: afastado do indicador',
                  'indicador esticado vertical: afastado do medio',
                  'medio esticado vertical: proximo ao anelar', 'anelar esticado vertical: afastado do minimo',
                  'minimo dobrado: afastado do anelar']

        self.letras = [self.A, self.B, self.C, self.D, self.E, self.F, self.G, self.I, self.L, self.M, self.N, self.O,
                       self.P, self.Q, self.R, self.S, self.T, self.U, self.V, self.W]
