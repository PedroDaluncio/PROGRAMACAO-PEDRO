def sem_selos_envelopes(qt_dinheiro, preco_envelope, preco_selo, qt_cartas=0):
    preco_carta = preco_envelope + preco_selo
    while qt_dinheiro >= preco_carta:
        qt_cartas += 1
        qt_dinheiro -= preco_carta
    return qt_cartas


def sem_selos_com_envelopes(qt_dinheiro, preco_envelope, preco_selo, qt_envelope, qt_cartas=0):
    preco_carta = preco_envelope + preco_selo
    while qt_dinheiro >= preco_selo:
        if qt_envelope > 0:
            qt_envelope -= 1
            qt_dinheiro -= preco_selo
        elif qt_dinheiro >= preco_carta:
            qt_dinheiro -= preco_carta
        else:
            break
        qt_cartas += 1
    return qt_cartas


def com_selos_sem_envelopes(qt_dinheiro, preco_envelope, preco_selo, qt_selo, qt_cartas=0):
    preco_carta = preco_envelope + preco_selo
    while qt_dinheiro >= preco_envelope:
        if qt_selo > 0:
            qt_selo -= 1
            qt_dinheiro -= preco_envelope
        elif qt_dinheiro >= preco_carta:
            qt_dinheiro -= preco_carta
        else:
            break
        qt_cartas += 1
    return qt_cartas


def com_ambos(qt_dinheiro, preco_envelope, preco_selo, qt_selo, qt_envelope):
    qt_cartas = 0
    while qt_selo > 0 and qt_envelope > 0:
        qt_selo -= 1
        qt_envelope -= 1
        qt_cartas += 1
    if qt_selo > 0:
        return com_selos_sem_envelopes(qt_dinheiro, preco_envelope, preco_selo, qt_selo, qt_cartas)
    if qt_envelope > 0:
        return sem_selos_com_envelopes(
            qt_dinheiro, preco_envelope, preco_selo, qt_envelope, qt_cartas)
    return sem_selos_envelopes(qt_dinheiro, preco_envelope, preco_selo, qt_cartas)


RS = float(input())
PE = float(input())
PS = float(input())
QS = int(input())
QE = int(input())
cartas = ''
if QS > 0 and QE > 0:
    cartas = com_ambos(RS, PE, PS, QS, QE)
elif QS > 0 and QE == 0:
    cartas = com_selos_sem_envelopes(RS, PE, PS, QS, QE)
elif QS == 0 and QE > 0:
    cartas = sem_selos_com_envelopes(RS, PE, PS, QS, QE)
else:
    cartas = sem_selos_envelopes(RS, PE, PS)

print(cartas)
