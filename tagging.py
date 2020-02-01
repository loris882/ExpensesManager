def tag(transacts):
    for n in transacts:
        if n[2].find("SCHMIT LORIS") != -1 or n[2].find("TRESORERIE")!= -1 or n[3] == "Argent de poche et repas":
            tag = "Einkommen"
        elif n[2].find("SCHECK-IN") != -1 or n[2].find("REWE") != -1 or n[2].find("KAUFLAND") != -1 or  n[2].find("DER FRISCHE MARKT") != -1 or n[2].find("Cactus") != -1:
            tag = "Essen"
        elif n[2].find("RETRAIT") != -1:
            tag = "Bar"
        elif n[2].find("VISA") != -1:
            tag = "Visa"
        elif n[2].find("DECATHLON") != -1 or n[2].find("BASISLAGER") != -1 or n[2].find("BIKE & OUTDOOR") != -1:
            tag = "Sport"
        elif n[2].find("1und1") != -1 or n[2].find("Rundfunk ARD, ZDF") != -1 or n[2].find("Stadtwerke Karlsruhe") != -1:
            tag = "Wohnen"
        elif n[2].find("DM-Drogerie Markt") != -1 or n[2].find("Rossmann") != -1:
            tag = "Drogerie"
        elif n[2].find("AMAZON") != -1:
            tag = "Amazon"
        elif n[2].find("Saturn") != -1 or n[2].find("Media Markt") != -1:
            tag = "Elektro"
        elif n[2].find("THALIA") != -1:
            tag = "Buch"
        elif n[1] == "INTERETS":
            tag = "Zinsen"
        else:
            print(n)
            tag = input("tag: ")
        n.append(tag)
    return transacts

def tagObject(transacts):
    for n in transacts:
        if n.sender.find("SCHMIT LORIS") != -1 or n.sender.find("TRESORERIE")!= -1 or n.reference == "Argent de poche et repas":
            tag = "Einkommen"
        elif n.sender.find("SCHECK-IN") != -1 or n.sender.find("REWE") != -1 or n.sender.find("KAUFLAND") != -1 or  n.sender.find("DER FRISCHE MARKT") != -1 or n.sender.find("Cactus") != -1:
            tag = "Essen"
        elif n.sender.find("RETRAIT") != -1:
            tag = "Bar"
        elif n.sender.find("VISA") != -1:
            tag = "Visa"
        elif n.sender.find("DECATHLON") != -1 or n.sender.find("BASISLAGER") != -1 or n.sender.find("BIKE & OUTDOOR") != -1:
            tag = "Sport"
        elif n.sender.find("1und1") != -1 or n.sender.find("Rundfunk ARD, ZDF") != -1 or n.sender.find("Stadtwerke Karlsruhe") != -1:
            tag = "Wohnen"
        elif n.sender.find("DM-Drogerie Markt") != -1 or n.sender.find("Rossmann") != -1:
            tag = "Drogerie"
        elif n.sender.find("AMAZON") != -1:
            tag = "Amazon"
        elif n.sender.find("Saturn") != -1 or n.sender.find("Media Markt") != -1:
            tag = "Elektro"
        elif n.sender.find("THALIA") != -1:
            tag = "Buch"
        elif n.type == "INTERETS":
            tag = "Zinsen"
        else:
            print(n.date.strftime("%d/%m/%Y")+" "+n.sender+" "+n.reference+" "+str(n.amount))
            tag = input("tag: ")
        n.tag = tag
    return transacts
