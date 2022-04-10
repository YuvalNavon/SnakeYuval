BOARD_HEIGHT = 5
BOARD_WIDTH = 6
HEART_ROW = 2
HEART_COL = 3
EMPTY_CELL = 0
HEART_CELL = '♥'


def eithul(matriz):
        for i in range(BOARD_HEIGHT):
            list2 = []
            for j in range(BOARD_WIDTH):
                if i==HEART_ROW and j == HEART_COL: list2.append(HEART_CELL)
                else: list2.append(EMPTY_CELL)
            matriz.append(list2)
def printer(matriz):
        for i in matriz:
            print (i)


if __name__ == '__main__':
    lister = []
    eithul(lister)
    printer(lister)