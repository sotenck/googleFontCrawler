class Style:

    def __init__(self, style, weight, file):
        self.styleName = style
        self.fontWeight = weight
        self.font = file

    def getFileAdding(self):
        return f"{self.styleName}-{self.fontWeight}"