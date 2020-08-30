from math import pi
def calcular_trapezio():
    #ENTRADA
    bmaior = float(input('''
                ===========================
                    digite a base MAIOR 
                        em metros: 
                ===========================
                            '''))
    bmenor = float(input('''
                ===========================
                    digite a base MENOR 
                        em metros: 
                ===========================
                            '''))
    altura_trapezio = float(input('''
                ===========================
                        digite a ALTURA
                          em metros: 
                ===========================
                            '''))
    

    #PROCESSAMENTO E SAIDA
    area_trapezio = ((bmaior + bmenor) * altura_trapezio)

    print(f'''
                ============================
                -=A area é de {area_trapezio:.2f} m²=-
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
