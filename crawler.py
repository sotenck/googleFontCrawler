from selenium import webdriver
import geckodriver_autoinstaller
from FontManager import FontManager

class FontCrawl:

    def __init__(self, fontUrl):
        geckodriver_autoinstaller.install()
        browser = webdriver.Firefox()
        browser.get(fontUrl)
        browser.implicitly_wait(3)
        self.sourceCode = browser.page_source
        browser.close()

    def textSegment(self):
        # Text segmentation setup
        nextBracket = 1
        closeBracket = 0
        fontManager = FontManager()

        while nextBracket > 0:
            nextBracket = self.sourceCode.find("{", closeBracket)
            if nextBracket < 0:
                print("... text analyisis done")
                break
            closeBracket = self.sourceCode.find("}", nextBracket)

            fontObject = self.sourceCode[nextBracket+1:closeBracket].strip()
            # get Charset Prev Info
            openComment = self.sourceCode.rfind("/*", 0, nextBracket)
            if openComment < 0:
                print("Loop broke because of Syntax Error")
                break
            closeComment = self.sourceCode.find("*/", openComment)
            charInfo = (self.sourceCode[openComment+2:closeComment]).strip()

            if charInfo in {"latin-ext", "latin"}:
                # extract Values from fontObject
                checkSum = [False, False, False, False, False]

                styleOptions = fontObject.splitlines()
                for n in styleOptions:

                    # get first Doppelpunkt
                    splitPos = n.find(":")

                    cssProp = n[0:splitPos].strip()
                    cssVal = n[splitPos+1:-1].strip()

                    if cssProp == "font-family":
                        fontFamily = cssVal[1:-1]
                        checkSum[0] = True

                    elif cssProp == "font-style":
                        fontStyle = cssVal
                        checkSum[1] = True

                    elif cssProp == "font-weight":
                        fontWeight = int(cssVal)
                        checkSum[2] = True

                    elif cssProp == "unicode-range":
                        fontRange = cssVal
                        checkSum[3] = True

                    elif cssProp == "src":
                        fontFile = cssVal[cssVal.find("(")+1:cssVal.find(")")]
                        checkSum[4] = True

                # Check if All nessessary Data is availabel
                if False in set(checkSum):
                    print("Missing Value - Aborted")
                    continue
                else :
                    # Create Object and Add to List
                    fontManager.addFont(fontFamily, charInfo, fontRange, fontStyle, fontWeight, fontFile)

        return fontManager.fontList
