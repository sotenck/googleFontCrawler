from fontFamily import Family

class FontManager:

    def __init__(self):
        self.fontList = []

    def addFont(self, name, chars, unicode, style, weight, file):
        fontExists = self.checkFontList(name, chars)
        if fontExists  == True :
            # Noch nicht vergeben -> zur Liste Adden
            newFont = Family(name, chars, unicode)
            newFont.addStyle(style, weight, file)
            newFontSet = self.fontList.append(newFont)
        else:
            # Font gefunden -> Neuer Style anfuegen
            fontExists.addStyle(style, weight, file)
        return


    def checkFontList(self, fontName, fontCharset):
        for x in self.fontList:
            if fontName == x.name and fontCharset == x.charset:
                return x

        return True
