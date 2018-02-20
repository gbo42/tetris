#colors
WHITE = (255, 255, 255)
GRAY = (51, 51, 51)

#block colors
ICOLOR = (219, 0, 0)
TCOLOR = (0, 255, 233)
SCOLOR = (224, 2, 216)
ZCOLOR = (46, 229, 13)
LCOLOR = (255, 119, 0)
JCOLOR = (2, 0, 142)
OCOLOR = (233, 255, 0)

#block types
blockI = {'size': 4, 'color': ICOLOR, 'grid': [[0,1,0,0],
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0]]}

blockT = {'size': 3, 'color': TCOLOR, 'grid': [[0,1,0],
          [1,1,1],
          [0,0,0]]}

blockS = {'size': 3, 'color': SCOLOR, 'grid': [[0,1,1],
          [1,1,0],
          [0,0,0]]}

blockZ = {'size': 3, 'color': ZCOLOR, 'grid': [[1,1,0],
          [0,1,1],
          [0,0,0]]}

blockL = {'size': 3, 'color': LCOLOR, 'grid': [[0,0,1],
          [1,1,1],
          [0,0,0]]}

blockJ = {'size': 3, 'color': JCOLOR, 'grid': [[1,0,0],
          [1,1,1],
          [0,0,0]]}

blockO = {'size': 2, 'color': OCOLOR, 'grid': [[1,1],
          [1,1]]}

#block list
minos = [blockI, blockS, blockZ, blockL, blockJ, blockT, blockO]
