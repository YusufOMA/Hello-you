import time

print("Hoi ik vlucht uit syrie ik ben mijn naam vergeten hoe heet ik?")
name = input('')
print(f"Hallo {name}")

def vraag1():

    print("Ik vluchtte uit Syrië, voor een beter toekomst.")    
    print("Hoe kan ik veilig Syrie verlaten?")
    print("a: boot")
    print("b: vliegtuig")
    antwoord1 = input()
    if antwoord1.lower() == "a":
        print("ja dat is veilig")
        vraag2()
    elif antwoord1.lower() == "b":
        print("de terroristen bombarderen de vliegtuig je bent dood")
        vraag1()
    else:
        print("kies a,b")
        vraag1()



def vraag2():
    
    print("je komt nu een smokkelaar tegen hij bied $750 aan om naar Turkije te vluchten, geef je het geld?")
    print("a: ja")
    print("b: nee")
    antwoord2 = input()
    if antwoord2.lower() == "a":
        print("de man was een oplichter hij pakt je geld en rent weg je hebt nu geen geld.")
        vraag3()
    elif antwoord2.lower() =="b":
        print("slimme keus want de man bleek een oplichter te zijn")
        vraag3()
    else:
        print("kies a,b")
        vraag2()



def vraag3():
    print("je loopt nu helemaal alleen door de straten. je komt nu een man tegen hij vraagt of je wilt werken voor geld accepteer je het?")
    print("a: ja ik wil weer geld verdienen")
    print("b: nee ik vertrouw de man niet")
    antwoord = input()
    if antwoord.lower() == "a":
        print("slimme keus.")
        vraag4()
    elif antwoord.lower() =="b":
        print("Je hebt een domme keus gemaakt je hebt nu geen geld en verhongerd van de honger")
        print("GAME OVER begin opnieuw")
        time.sleep(3)
        vraag1()
    else:
        print("kies a,b")
        vraag3()


def vraag4():
    print("de terroristen zien dat je werkt en dat mag niet ze willen je gaan pakken en in de gevangenis zetten wat doe je?")
    print("a: wegrennen")
    print("b: je zelf over geven")
    print("c: doen alsof je niks doorhebt in hoop dat ze niet op je in gaan")
    antwoord = input()
    if antwoord.lower() == "a":
        print("1 van de teroristen schiet je dood.")
        print("GAME OVER")
        print("begin opnieuw")
        time.sleep(3)
        vraag1()
    elif antwoord.lower() =="b":
        print("oke de teroristen spreken je aan")
        vraag5()
    elif antwoord.lower() =="c":
        print("de terroristen die komen boos op je aflopen")
        vraag6()
    else:
        print("kies a,b,c")
        vraag4()

def vraag5():
    print("ze vragen wat je aan het doen bent. Ga jij de waar heid vertellen of liegen?")
    print("a: waarheid vertellen")
    print("b: liegen")
    antwoord=input()
    if antwoord.lower() == "a":
        print("je mag niet werken schreeuwt er 1.")
        vraag7()
    elif antwoord.lower() =="b":
        print("slimme keus")
        vraag8()
    else:
        print("kies a,b")
        vraag5()


def vraag6():
    print("ze vragen waarom je niet reageert en houden je vast hoe ga jij reageren?")
    print("a: terug vechten")
    print("b: schreeuwen om hulp")
    print("c: niks doen")
    antwoord=input()
    if antwoord.lower() == "a":
        print("de terrorist begint je irritand te vinden en schiet je dood.")
        print("Game over")
        time.sleep(3.5)
        vraag1()
    elif antwoord.lower() =="b":
        print("iedereen is bang niemand komt je helpen")
        vraag9()
    elif antwoord.lower() =="c":
        print("ze beginnen je te slaan en brengen ze je naar de gevangenis")
        vraag10()
    else:
        print("kies a,b,c")
        vraag6()

def vraag7():
    print("daarom moet je naar de gevangenis wat ga je doen?")
    print("a: ik ga mee lopen")
    print("b: ik ga schreeuwen om hulp")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze brengen je naar de gevangenis.")
        vraag11()
    elif antwoord.lower() =="b":
        print("iedereen is bang niemand komt je helpen en omdat je ging schreeuwen, schieten ze op je voet en ga je uiteindelijk dood door dat je te veel bloed hebt verliest.")
        print("Game over")
        time.sleep(3)
        vraag1()
    else:
        print("kies a,b")
        vraag7()

def vraag8():
    print("wat ga je zeggen?")
    print("a: ik weet niks ik ben hier op vakantie gekomen van Bulgarije")
    print("b: nee ik werk hier niet ik help een vriend")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze geloven je niet helemaal.")
        vraag12()
    elif antwoord.lower() =="b":
        print("ze vragen aan je: wie is je vriend.")
        vraag13()
    else:
        print("kies a,b")
        vraag8()


def vraag9():
    print("ze zeggen dat je stil moet zijn en schieten je dood?")
    print("GAME OVER begin opnieuw")
    time.sleep(3)
    vraag1()


def vraag10():
    print("5 maanden later...")
    time.sleep(2)
    print("je komt uit de gevangenis voor een voorwaarden en dat is dat je moet gaan werken voor de terroristen.")
    time.sleep(1)
    print("accepteer je dat")
    print("a: ja")
    print("b: nee")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze vertrouwen je en je mag weer naar buiten.")
        vraag15()
    elif antwoord.lower() =="b":
        print("ze beginnen te schreeuwen en maken je dood.")
        print("GAME OVER")
        time.sleep(2)
        vraag1()
    else:
        print("kies a,b")
        vraag10()


def vraag11():
    print("je komt aan in de gevangenis")
    print("2 maanden later...")
    time.sleep(2)
    vraag10()

def vraag12():
    print("ga je vloed praten? of ga je stotterend praten?")
    print("a: stotterend")
    print("b: vloed")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze vragen naar je paspoort")
        vraag16()
    elif antwoord.lower() =="b":
        print("omdat je vloeiend praat weten ze dat je niet van bulgarije komt daarom ga je dood")
        vraag1()
    else:
        print("kies a,b")
        vraag12()

def vraag13():
    print("a: ik vertel de waarheid")
    print("b: ik verzin een naam")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze schieten je dood.")
        print("game over")
        time.sleep()
        vraag1()
    elif antwoord.lower() =="b":
        print("ze zeggen dat je hun naar de adres van je vriend moet gaan brengen")
        vraag14()
    else:
        print("kies a,b")
        vraag13

def vraag14():
    print("je weet geen adres en daarom ga je de gevangenis in voor het liegen")
    vraag7()
    vraag14()

def vraag15():
    print("de teroristen brengen je naar een plek je weet niet waar dat is je kijkt goed om je heen ze willen dat je met hun meegaat naar de oorlog gebied en mensen dood gaat maken")
    print("a: je gaat mee")
    print("b: je zegt dat je dat niet wilt")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ze brengen je gelijk naar de plek.")
        vraag17()
    elif antwoord.lower() =="b":
        print("GAME OVER.")
        vraag1()
    else:
        print("kies a,b")
        vraag15()


def vraag16():
    print("je hebt geen paspoort en je wordt doodgemaakt")
    print("GAME OVER")
    vraag1()

def vraag17():
    print("je komt aan bij de plek je merkt dat je weg kan rennen")
    print("ga je wegrennen?")
    print("a: ja gelijk ik wil zo snel mogelijk weg")
    print("b: nee ik ben bang")
    antwoord=input()
    if antwoord.lower() == "a":
        print("je rent weg heel hard.")
        vraag18()
    elif antwoord.lower() =="b":
        print("de teroristen roepen speciaal jou naar voren in het dorp.")
        vraag19()
    else:
        print("kies a,b")
        vraag17()
    vraag17()


def vraag18():
    print("je komt opnieuw een smokkelaar tegen hij zegt dat hij je kan brengen naar Turkije (stiekem)")
    print("a: je accepteert het omdat je zo snel mogelijk weg wit")
    print("b: je zegt nee omdat je het niet vertrouwd")
    antwoord=input()
    if antwoord.lower() == "a":
        print("je mag gelijk in een bootje en je gaat eindelijk weg van Syrie.")
        vraag20()
    elif antwoord.lower() =="b":
        print("dat was geen slimme keus want de teroristen die zitten achter je aan. Ze hebben je gevonden en maken je dood.")
        vraag1()
    else:
        print("kies a,b")
        vraag15()
    vraag15()

def vraag19():
    print("ze zeggen dat je een famillie moet doden")
    print("a: je zegt nee ik ga dat niet doen")
    print("b: je zegt ja en je maakt ze dood")
    antwoord=input()
    if antwoord.lower() == "a":
        print("omdat je nee hebt gezegd maken de teroristen jou dood.")
        print("Game over")
        time.sleep(1)
        vraag1()
    elif antwoord.lower() =="b":
        print("de teroristen beginnen te juichen en ze vertrouwen jou meer.")
        vraag18()
    else:
        print("kies a,b")
        vraag19()

    


def vraag20():
    print("5 uur later")
    time.sleep(3)
    print("eindelijk ben je veilig aangekomen in Turkije, je bent opzoek naar werk.")
    time.sleep(1)
    print("gelukkig heeft de regering werk voor mij gevonden in de supermarkt. Ik  moet daar van alles doen spiegelen,kassa en noem maar op het is leuk en gezellig.")
    print("5 jaar later...")
    time.sleep(3.5)
    print("je werkt nu full time 5 jaar lang in een supermarkt omdat je 5 jaar lang in turkije bent krijg je je eigen paspoort maar je hebt 1 probleem en dat is dat je niet echt goed verdient en dus twijfel ik om mijn eigen winkel te openen.")
    print("ga ik eeen eigen winkel openen?")
    print("a: ja ik wil beter verdienen ")
    print("b: nee ik blij werken bij de supermarkt")
    antwoord=input()
    if antwoord.lower() == "a":
        print("slimme keus je wordt rijk.")
        vraag21()
    elif antwoord.lower() =="b":
        print("je blijft werken...")
        einde()
        time.sleep(2)
    else:
        print("kies a,b")
        vraag20()



def vraag21():
    print("je opent je eigen winkel de winkel loopt goed de inkomen stijgt en je wordt steeds succer.")
    print("ga ik een huis kopen?")
    print("a: nee")
    print("b: ja")
    antwoord=input()
    if antwoord.lower() == "a":
        print("ik blijf wonen in een huur huis.")
        einde()
    elif antwoord.lower() =="b":
        print("slimme keus je hebt nu je eigen huis.")
        einde()
    else:
        print("kies a,b")
        vraag21()
    
def einde():
    print("4 maanden later...")
    time.sleep(2)
    print("ik heb nu een vrouw en 3 kinderen we zijn super gelukkig!!")
    time.sleep(1.2)
    print("EINDE JE BENT GESLAAGD")
    time.sleep(5)
    vraag1()
    einde()


vraag1()
vraag2()
vraag3()
vraag4()
vraag5()
vraag6()
vraag7()
vraag8()
vraag9()
vraag10()
vraag11()
vraag12()
vraag13()
vraag14()
vraag15()
vraag16()
vraag17()
vraag18()
vraag19()
vraag21()
einde()



