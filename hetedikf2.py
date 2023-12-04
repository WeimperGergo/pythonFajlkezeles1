def hetedik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
        #   leszedi a /n-t
    beFajl.close()

    #   lista kiírás
    for i in range(len(lista)-1, -1, -1):
        print(lista[i], end="\n")

