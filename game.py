class Game:
    def __init__(self, array:list):
        self.__array = array
        self.__done = False
        self.__len_array = len(self.__array)

    @property
    def array(self):
        return print(self.__array[0], self.__array[1], self.__array[2], self.__array[3], self.__array[4], sep="\n")

    def walk(self, pos, robo):
        if(self.__array[pos[0] + 1][pos[1]] == '' or self.__array[pos[0] + 1][pos[1]] == '*'):
            if(self.__array[pos[0] + 1][pos[1]] == '*'):
                self.__array[pos[0] + 1][pos[1]] = robo
                self.__array[pos[0]][pos[1]] = 'V'
                self.__done = True
                return print("O robô encontrou o final")

            self.__array[pos[0] + 1][pos[1]] = robo
            self.__array[pos[0]][pos[1]] = 'V'
        elif(self.__array[pos[0] - 1][pos[1]] == '' or self.__array[pos[0] - 1][pos[1]] == '*'):
            if(self.__array[pos[0] - 1][pos[1]] == '*'):
                self.__array[pos[0] - 1][pos[1]] = robo
                self.__array[pos[0]][pos[1]] = 'V'
                self.__done = True
                return print("O robô encontrou o final")
            
            self.__array[pos[0] - 1][pos[1]] = robo
            self.__array[pos[0]][pos[1]] = 'V'
        elif(self.__array[pos[0]][pos[1] + 1] == '' or self.__array[pos[0]][pos[1] + 1] == '*'):
            if(self.__array[pos[0]][pos[1] + 1] == '*'):
                self.__array[pos[0]][pos[1] + 1] == robo
                self.__array[pos[0]][pos[1]] = 'V'
                self.__done = True
                return print("O robô encontrou o final")

            self.__array[pos[0]][pos[1] + 1] = robo
            self.__array[pos[0]][pos[1]] = 'V'
        elif(self.__array[pos[0]][pos[1] - 1] == '' or self.__array[pos[0]][pos[1] - 1] == '*'):
            if(self.__array[pos[0]][pos[1] - 1] == '*'):
                self.__array[pos[0]][pos[1] - 1] = robo
                self.__array[pos[0]][pos[1]] = 'V'
                self.__done = True
                return print("O robô encontrou o final")

            self.__array[pos[0]][pos[1] - 1] = robo
            self.__array[pos[0]][pos[1]] = 'V'
        else:
            print("Tá passando pelo else")

    def pos(self):
        linha = 0
        coluna = 0
        for x in self.__array:
            for y in x:
                if(y == 'S'):
                    return [linha, coluna]
                coluna += 1
                if(coluna == self.__len_array):
                    coluna = 0
            linha += 1
        return [linha, coluna]

    def win(self):
        if(self.__done == True):
            return self.__done