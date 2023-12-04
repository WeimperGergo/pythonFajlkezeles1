
def elso():
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    #   forrás hely ; írás/olvasás ; kódolás
    for sor in beFajl:
        print(sor.strip(), end="")
        #   leszedi a /n-t

    beFajl.close()