def CELtoFAR(CEL):
    return CEL * (9 / 5) + 32


def CELtoCEL(CEL):
    return CEL


def FARtoCEL(FAR):
    return (FAR - 32) / (9 / 5)


def KELtoCEL(KEL):
    return KEL - 273.15


def CELtoKEL(CEL):
    return CEL + 273.15


def M3toLIT(M3):
    return M3 * 1000


def LITtoM3(LIT):
    return LIT / 1000


def CM3toLIT(CM3):
    return CM3 / 1000


def LITtoCM3(LIT):
    return LIT * 1000


def GALtoLIT(GAL):
    return GAL * 3.78541


def LITtoGAL(LIT):
    return GAL * 0.264172


def PNTtoLIT(PNT):
    return PNT / 1.76


def LITtoPNT(LIT):
    return LIT * 1.76


def TBSPtoLIT(TBSP):
    return TBSP * 0.014787


def LITtoTBSP(LIT):
    return LIT / 0.014787


def TSPtoLIT(TSP):
    return TSP / 202.884136


def LITtoTSP(LIT):
    return LIT * 202.884136


def LITtoLIT(LIT):
    return LIT


def USDtoUSD(USD):
    return USD


def GBPtoUSD(GBP):
    return GBP / 0.8131


def USDtoGBP(USD):
    return USD * 0.8131


def CADtoUSD(CAD):
    return CAD / 1.4385


def USDtoCAD(USD):
    return USD * 1.4385


def EURtoUSD(EUR):
    return EUR / 0.9614


def USDtoEUR(USD):
    return USD * 0.9614


temp = [
    ["Farenheit", FARtoCEL, CELtoFAR],
    ["Celcius", CELtoCEL, CELtoCEL],
    ["Kelvin", KELtoCEL, CELtoKEL],
]
currency = [
    ["USD - USA", USDtoUSD, USDtoUSD],
    ["GBP - UK", GBPtoUSD, USDtoGBP],
    ["CAD - Canada", CADtoUSD, USDtoCAD],
    ["EUR - Euro", EURtoUSD, USDtoEUR],
]
volume = [
    ["Cubic metres", M3toLIT, LITtoM3],
    ["Cubic centimetres", CM3toLIT, LITtoCM3],
    ["Litres", LITtoLIT, LITtoLIT],
    ["Gallons", GALtoLIT, LITtoGAL],
    ["Pints", PNTtoLIT, LITtoPNT],
    ["Tablespoons", TBSPtoLIT, LITtoTBSP],
    ["Teaspoons", TSPtoLIT, LITtoTSP],
]
conversions = [
    ["Temperature", temp],
    ["Currencies", currency, "SUBJECT TO CHANGE - last updated 21/01/2025"],
    ["Volume", volume],
]

print("Which type of unit do you want to convert (type the number)?:")
for i in range(len(conversions)):
    notes = ""
    if len(conversions[i]) == 3:
        notes = "(" + conversions[i][2] + ")"
    print(f"{i+1}: {conversions[i][0]} {notes}")
choice = int(input("--->  ")) - 1
conv = conversions[choice][1]

for i in range(len(conv)):
    notes = ""
    if len(conv[i]) == 4:
        notes = "(" + conv[i][3] + ")"
    print(f"{i+1}: {conv[i][0]} {notes}")
choice1 = int(input("--->  ")) - 1
choice2 = int(input("--->  ")) - 1

quantity = float(input(f"What quantity of {conv[choice1][0]} do you want to convert to {conv[choice2][0]}?  "))
print(f"{quantity} {conv[choice1][0]} in {conv[choice2][0]} is:")
print(conv[choice2][2](conv[choice1][1](quantity)))
