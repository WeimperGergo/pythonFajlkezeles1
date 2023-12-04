def masodik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
        #   leszedi a /n-t

    #   lista kiírás
    for i in range(0, len(lista), 1):
        print(lista[i], end="")
    beFajl.close()