def negyedik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
        #   leszedi a /n-t
    beFajl.close()

    #   lista kiírás fájlba
    kiFajl = open("fajlok/negyedik.txt", "w", encoding="utf-8")
    for i in range(0, len(lista), 1):
        daraboltSor = lista[i].split(' ')
        #   Sorokat darabolja praméter(szóköz) mentén
        print(daraboltSor[0],file=kiFajl, end="\n")
        # Lista 0. elemlét írja ki minden sornak
        # kiFajl.write(lista[i])
                                    #   2 FAJTA FÁJLBAÍRÁS
    kiFajl.close()

