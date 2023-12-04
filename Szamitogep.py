class Szamitogep:
    def __init__(self, szabadMemoria:float, beKapcsolva:bool):
        if szabadMemoria == 0:
            self.szabadMemoria = 1024
        else:
            self.szabadMemoria = szabadMemoria

        if beKapcsolva == 0:
            self.beKapcsolva = False
        else:
            self.beKapcsolva = beKapcsolva

    def kapcsol(self):
        if self.beKapcsolva:
            self.beKapcsolva = False
        else:
            self.beKapcsolva = True

    def programMasol(self, programMeret : float)->bool:
        #  -> (Változó típus)   <- megadjuk vele a függvény visszatérési típusát.
        gepreFer = False
        if self.beKapcsolva and self.szabadMemoria > programMeret:
            self.szabadMemoria -= programMeret
            gepreFer = True
            print("A másolás sikeres volt. Hátralévő tárhely: ", self.szabadMemoria, "MB")
        else:
            print("A másolás sikertelen! A gép nincs bekapcsolva, vagy nincs elég tárhely.")
        return gepreFer

    def __str__(self):
        bekapcsKiir = ""
        if self.beKapcsolva == False:
            bekapcsKiir = "Kikapcsolva"
        else:
            bekapcsKiir = "Bekapcsolva"
        return f"Szabad memória méret: {self.szabadMemoria}, állapot: {self.beKapcsolva}"






