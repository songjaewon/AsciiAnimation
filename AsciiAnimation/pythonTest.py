# #-*- coding: utf-8 -*-
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# from freetype import *
#
# #Load an color image in grayscale
# img = cv2.imread('seq/yuna000.jpg',0)
#
# print img[0][0]
#
# for i in range(img.shape[1]):
#     for j in range(img.shape[0]):
#         print img[i][j],
#     print

# f = open('youmi.txt', 'w')
# for i in range(134):
#     for j in range(100):
#         if img[i][j] == 0.0 : f.write('..')
#         elif img[i][j] >= 0.0 and img[i][j] < 25.0 : f.write('랑')
#         elif img[i][j] >= 25.0 and img[i][j] < 50.0 : f.write('사')
#         elif img[i][j] >= 50.0 and img[i][j] < 100.0 : f.write('미')
#         elif img[i][j] >= 100.0 and img[i][j] < 200.0 : f.write('유')
#         elif img[i][j] >=200 : f.write('ㅠ')
#     f.write('\n')
# f.close()



# import freetype
# face = freetype.Face("malgun.ttf")
# face.set_char_size( 100*100 )

# maxRows = 0.0
# maxRowsIdx = 0
# maxWidth = 0.0
# maxWidthIdx = 0
# for i in range(585, 12505):
#     face.load_glyph(i)
#     if face.glyph.bitmap.rows > maxRows :
#         maxRows = face.glyph.bitmap.rows
#         maxRowsIdx = i
#     if face.glyph.bitmap.width > maxWidth :
#         maxWidth = face.glyph.bitmap.width
#         maxWidthIdx = i
#
# print 'maxRow, maxRowIdx, maxWidth, maxWidthIdx : ', maxRows, maxRowsIdx, maxWidth, maxWidthIdx




#face.load_glyph(585) #ㄱ
#face.load_glyph(636) #가
#face.load_glyph(642) #갊

# a = u'송재'
# b = a.encode('cp949')
# c = b[0]+b[1]
# d = c.decode('cp949')

#print d.encode('cp949')




# face.load_char(d)

#face.load_char(u'송')
#face.load_glyph(3226)

# bitmap = face.glyph.bitmap.buffer
#
# print 'bitmap : ', bitmap
# print 'len(bitmap) : ', len(bitmap)
#
# import copy
# nMap = copy.deepcopy(bitmap)

# for i in nMap :
#     if i==0 : nMap.remove(i)
# print len(nMap)
#
# print 'bitmap rows : ', face.glyph.bitmap.rows
# print 'bitmap width : ', face.glyph.bitmap.width
# print 'bitmap top : ', face.glyph.bitmap_top
# print 'bitmap left : ', face.glyph.bitmap_left
# print 'bitmap pitch : ', face.glyph.bitmap.pitch


# img = np.zeros((face.glyph.bitmap.rows,face.glyph.bitmap.width,3), np.uint8)
# for i in range(face.glyph.bitmap.rows):
#     for j in range( face.glyph.bitmap.width):
#         img[i][j] = bitmap[i* face.glyph.bitmap.width+j]

# img = np.zeros((156,156,3), np.uint8)
# for i in range(face.glyph.bitmap.rows):
#     for j in range( face.glyph.bitmap.width):
#         img[i][j] = bitmap[i* face.glyph.bitmap.width+j]
#
#
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()







