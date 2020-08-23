from math import pi
def calcular_quadrado():
    #ENTRADA
    x = float(input('''
                ===========================
                digite a largura em metros: 
                ===========================
                            '''))
    y = float(input('''
                ==========================
                digite a altura em metros: 
                ==========================
                            '''))

    #PROCESSAMENTO E SAIDA
    print(f'''
                ============================
                -=A area é de {(x)*(y):.2f} m²=-
                ============================
                            ''')



def calcular_circunferencia():
    #entrada
    raio = float(input('''
                ==========================
                 Digite o tamanho do raio
                        em metros 
                ==========================
                            '''))
    #processamento
    area = pi * raio * raio

    #saida
    print(f'''
                =============================
                -=  A area é de {area:.2f} m²  =-
                =============================
                            ''')

def calcular_retangulo():
    #ENTRADA
    base = float(input('''
                ==========================
                 Digite o tamanho da base
                        em metros
                ==========================
                            '''))
    altura = float(input('''
                ==========================
                    Digite o tamanho da 
                     altura em metros
                ==========================
                            '''))
    #SAIDA
    print(f'''
                =============================
                -=  A area é de {base * altura:.2f} m²  =-
                =============================
                            ''')
