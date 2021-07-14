foreignDict = dict()
while True:
    dictEntryList = input().split()
    if dictEntryList:
        foreignDict[dictEntryList[1]] = dictEntryList[0]
    else:
        break

foreignString = None
translations = []
while foreignString != '':
    try:
        foreignString = input()
        translatedString = foreignDict.get(foreignString, 'eh')
        translations.append(translatedString)
    except: break
for translation in translations:
    print(translation)
