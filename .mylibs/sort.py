class Sort:
    def sort(self, list1):
        self.__list1 = list1[:]
        self.__list2 = []
        for i in range(len(self.__list)):
            self.__list2.append(
                    self.__list1.pop(
                        self.__list1.index(
                            min(self.__list1)
                            )
                        )
                    )
        return self.__list2


sort = Sort()
