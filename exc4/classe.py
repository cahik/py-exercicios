

# Atençao! neste código o prisioneiro = lula e policial = puliça

aviao = []
terminal = ['piloto','oficial1','oficial2','chefe','comissaria1','comissaria2','lula','puliça']



def indo( p1,p2):
    terminal.remove(p1)
    terminal.remove(p2)
    aviao.append(p1)
    aviao.append(p2)
    print(f'Fortwo em movimento, levando o motorista {p1} e o passageiro {p2} para o avião{aviao}')

def vindo(p1):
    aviao.remove(p1)
    terminal.append(p1)
    print(f'Fortwo em movimento, levando o motorista {p1} para o terminal{terminal}')

