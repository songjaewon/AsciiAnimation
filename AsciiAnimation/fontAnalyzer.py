#-*- coding: utf-8 -*-

__author__ = 'cimple'

"""
..module:: malgunAnalyzer

..moduleauthor:: Jaewon Song <songjaewon@kaist.ac.kr>
"""

import freetype
import cv2
import numpy as np

class FontAnalyzer():
    '''
    한글 주석이 실행되는지 테스트입니다. 아마도 되기는 힘들겠죠..?

    **Note**
    Now it's only for the 2byte Han-gul(Korean word) TTF(True type font).
    '''
    def __init__(self):
        """Initialize class for FontAnalyzer
        Args:
            numCharacter(int): Number of characters
            fontStartIdx(int): Start index of Hangul
        """
        self.numCharacter = 0

        self.fontStartIdx = 0
        self.fontEndIdx = 0
        self.charIntensityValDic = {}
        self.orderedIdxBasedOnIntensity = []
        self.uKoreanCharList = []

        self.fontName = ''
        self.fontSize = 0.0
        #self.face = freetype.Face()
        self.face = None

    def init_setuKoreanCharacterList(self, uKoreanString):
        """
        Setup the Korean characters during the initialize step.
        :param uKoreanString: Unicode Korean Characters.
        :return: Nothing
        """
        encodeList = uKoreanString.encode('cp949')
        self.numCharacter = len(encodeList)/2
        for i in range(self.numCharacter):
            char = encodeList[i*2] + encodeList[i*2+1]
            u_char = char.decode('cp949')
            self.uKoreanCharList.append(u_char)

    def init_setFont(self, fontName, fontSize=48*64):
        self.fontName = fontName
        self.fontSize = fontSize
        self.face = freetype.Face(self.fontName)
        self.face.set_char_size(self.fontSize)

    def init_setFontStartEndIdx(self, startIdx, endIdx):
        """
        Setup the font start and end index during the initialize step.
        :param startIdx: (int) start index of the font
        :param endIdx: (int) end index of the font
        :return: Nothing
        """
        self.fontStartIdx = startIdx
        self.fontEndIdx = endIdx
        self.numCharacter = endIdx-startIdx+1

    def createCharIntensityValDicByChar(self):
        for char in self.uKoreanCharList :
            self.face.load_char(char)
            bitmap = self.face.glyph.bitmap.buffer
            nonZeroBitMap = filter(lambda a: a!=0, bitmap)
            intensity = len(nonZeroBitMap)

            if len(self.orderedIdxBasedOnIntensity) == 0:
                self.orderedIdxBasedOnIntensity.append([char, intensity])
            else:
                tmpSize = len(self.orderedIdxBasedOnIntensity)
                for i, current_elem in enumerate(self.orderedIdxBasedOnIntensity):
                    current_intensity = current_elem[1]
                    if intensity < current_intensity :
                        self.orderedIdxBasedOnIntensity.insert(self.orderedIdxBasedOnIntensity.index(current_elem), [char, intensity])
                        break
                if tmpSize == len(self.orderedIdxBasedOnIntensity):
                    self.orderedIdxBasedOnIntensity.append([char, intensity])

    def createCharIntensityValDicByIdx(self):
        for i in range(self.fontStartIdx, self.fontEndIdx+1):
            self.face.load_glyph(i)
            bitmap = self.face.glyph.bitmap.buffer
            nMap = filter(lambda a: a!=0, bitmap)

            if len(self.orderedIdxBasedOnIntensity) == 0:
                self.orderedIdxBasedOnIntensity.append([i, len(nMap)])
            else:
                tmpSize = len(self.orderedIdxBasedOnIntensity)
                for j, fontIdxVal in enumerate(self.orderedIdxBasedOnIntensity):
                    if len(nMap) < fontIdxVal[1] :
                        self.orderedIdxBasedOnIntensity.insert(self.orderedIdxBasedOnIntensity.index(fontIdxVal), [i, len(nMap)])
                        break
                if tmpSize==len(self.orderedIdxBasedOnIntensity):
                    self.orderedIdxBasedOnIntensity.append([i, len(nMap)])

class ImgAnalyzer():
    def __init__(self):
        self.imgName = ''
        self.image = None
        self.imgWidth = 0
        self.imgHeight = 0

    def getGrayscaleImg(self, imgName):
        self.imgName = imgName
        self.image = cv2.imread(self.imgName, 0)
        self.imgWidth = np.shape(self.image)[1]
        self.imgHeight = np.shape(self.image)[0]




def createHangulAsciiArt(uKoreanCharacterList, fontName, imgName):
    fa = FontAnalyzer()
    fa.init_setFont(fontName, 100*100)
    fa.init_setuKoreanCharacterList(uKoreanCharacterList)
    fa.createCharIntensityValDicByChar()
    factor = 255.0 / (fa.numCharacter+1)

    # for i in range(fa.numCharacter):
    #     print fa.orderedIdxBasedOnIntensity[i][0].encode('cp949'),

    ia = ImgAnalyzer()
    ia.getGrayscaleImg(imgName)

    f = open(imgName[:-4]+'.txt', 'w')
    for i in range(ia.imgHeight) :
        for j in range(ia.imgWidth):
            charIdx = int(ia.image[i][j]/factor)
            if charIdx == fa.numCharacter+1 :
                f.write('  ')
            else:
                f.write(fa.orderedIdxBasedOnIntensity[charIdx-1][0].encode('cp949'))
        f.write('\n')
    f.close()

    for i in range(ia.imgHeight) :
        for j in range(ia.imgWidth):
            charIdx = int(ia.image[i][j]/factor)
            if charIdx == fa.numCharacter + 1:
                print '  ',
            else:
                print fa.orderedIdxBasedOnIntensity[charIdx-1][0].encode('cp949'),
        print


#standardKoreanCharacters = u'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄲㄸㅃㅆㅉㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢㄲㅆㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄ'
#vmChar = u'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄲㄸㅃㅆㅉㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢㄲㅆㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄ카이스트비주얼미디어랩'


#createHangulAsciiArt(vmChar, 'malgun.ttf', 'vml100px.png')
# for i in range(786):
#     if i<10:
#         fileName = 'yuna00'+str(i)+'.jpg'
#     elif i>=10 and i<100 :
#         fileName = 'yuna0'+str(i)+'.jpg'
#     else :
#         fileName = 'yuna'+str(i)+'.jpg'
#     createHangulAsciiArt(standardKoreanCharacters, 'malgun.ttf', 'seq/'+fileName)


