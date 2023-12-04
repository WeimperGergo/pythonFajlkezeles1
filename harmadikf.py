def harmadik():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    lista = []
    for sor in beFajl:
        lista.append(sor.strip())
        #   leszedi a /n-t
    beFajl.close()

    #   lista kiírás fájlba
    kiFajl = open("fajlok/harmadik.txt", "w", encoding="utf-8")
    for i in range(0, len(lista), 1):
        print(lista[i],file=kiFajl, end="")
        kiFajl.write(lista[i])
        #   2 FAJTA FÁJLBAÍRÁS

