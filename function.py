from math import pi
def calcular_quadrado():
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

    print(f'''
                ============================
                -=A area é de {(x)*(y):.2f} m²-=
                ============================
                            ''')



def calcular_circunferencia():
    raio = float(input('''
                ==========================
                 Digite o tamanho do raio
                        em metros 
                ==========================
                            '''))
    area = pi * raio * raio

    print(f'''
                =============================
                -=  A area é de {area:.2f} m²  =-
                =============================
                            ''')
