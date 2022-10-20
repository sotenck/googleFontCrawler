from fontStyle import Style

class Family:

    def __init__(self, name, chars, unicodes):
        self.name = name
        self.charset = chars
        self.unicode = unicodes
        self.variations = []

    def __str__(self):
        return f"Font: {self.name} - Charset: {self.charset}"

    def addStyle(self, name, weight, font):
        if self.checkVariationList(name, weight):
            # Style not yet Set
            styleVariation = Style(name, weight, font)
            self.variations.append(styleVariation)

        return

    # Check if Style already exists
    def checkVariationList(self, style, width):
        # Loop through all Families and check if match is found
        for x in self.variations:
            if style == x.styleName and width == x.fontWeight :
                return False

        return True

    def cleanFamilyName(self):
        return f"{ self.name.replace(' ','-') }"
