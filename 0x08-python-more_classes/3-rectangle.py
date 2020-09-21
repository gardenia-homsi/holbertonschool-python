def my_print(self):
        str = ""
        if self.__size == 0:
            str += ""
        else:
            str += "\n" * self.__position[1]
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    str += " "
                for n in range(0, self.__size):
                    str += "#"
                if i != self.__size - 1:
                    str += "\n"
        return str

    def __str__(self):
        return self.my_print()
