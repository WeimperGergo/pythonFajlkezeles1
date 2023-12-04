def hetedik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
    lista.reverse()
        #   leszedi a /n-t
    beFajl.close()

    #   lista kiírás
    kiFajl = open("fajlok/hetedik.txt", "w", encoding="utf-8")
    for i in range(0, len(lista), 1):
        print(lista[i], end="\n")
        print(lista[i], file=kiFajl)

    kiFajl.close()

