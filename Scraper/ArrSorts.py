"""Sorts through an array using insertionSort or mergeSort"""

class ArrSorts():
    def __init__(self, arr) -> None:
        self.arr = arr

    def insertionSort(self, val) -> list:  # calls insertion sort based on input
        if val == "market cap":
            return self.insertionSort_MC()
        elif val == "pe":
            return self.insertionSort_PE()
        elif val == "eps":
            return self.insertionSort_EPS()
        elif val == "volume":
            return self.insertionSort_volume()
        else:
            return self.insertionSort_beta()

    def insertionSort_PE(self) -> list:  # insertion sort based on price to earnings
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            try:
                key = self.arr[i]
                j = i-1
                if key.PE != 'N/A':
                    while j >= 0 and key.PE < self.arr[j].PE:
                            self.arr[j + 1] = self.arr[j]
                            j -= 1
                    self.arr[j + 1] = key
                else:
                    self.arr.remove(key)
                    print(key.name + " has not released their PE values")
            except:
                break

        returnedArr = []
        for elem in self.arr:
            returnedArr.append(elem.name)
        return returnedArr

    def insertionSort_EPS(self) -> list:  # insertion sort based on earnings per share
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            try:
                key = self.arr[i]
                j = i-1
                if key.EPS != 'N/A':
                    while j >= 0 and key.EPS < self.arr[j].EPS:
                            self.arr[j + 1] = self.arr[j]
                            j -= 1
                    self.arr[j + 1] = key
                else:
                    self.arr.remove(key)
                    print(key.name + " has not released their EPS values")
            except:
                break
        returnedArr = []
        for elem in self.arr:
            returnedArr.append(elem.name)
        return returnedArr

    def insertionSort_volume(self) -> list:  # insertion sort based on volume
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            try:
                key = self.arr[i]
                j = i-1
                if key.volume != 'N/A':
                    while j >= 0 and key.volume < self.arr[j].volume:
                            self.arr[j + 1] = self.arr[j]
                            j -= 1
                    self.arr[j + 1] = key
                else:
                    self.arr.remove(key)
                    print(key.name + " has not released their volume values")
            except:
                break
            
        returnedArr = []
        for elem in self.arr:
            returnedArr.append(elem.name)
        return returnedArr
    
    def insertionSort_MC(self) -> list:  # insertion sort based on market cap
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            try:
                key = self.arr[i]
                j = i-1
                if key.marketCap != 'N/A':
                    while j >= 0 and key.marketCap < self.arr[j].marketCap:
                            self.arr[j + 1] = self.arr[j]
                            j -= 1
                    self.arr[j + 1] = key
                else:
                    self.arr.remove(key)
                    print(key.name + " has not released their market cap values")
            except:
                break
            
        returnedArr = []
        for elem in self.arr:
            returnedArr.append(elem.name)
        return returnedArr

    def insertionSort_beta(self) -> list:  # insertion sort based on beta
        # Traverse through 1 to len(arr)
        for i in range(1, len(self.arr)):
            try:
                key = self.arr[i]
                j = i-1
                if key.beta != 'N/A':
                    while j >= 0 and key.beta < self.arr[j].beta:
                            self.arr[j + 1] = self.arr[j]
                            j -= 1
                    self.arr[j + 1] = key
                else:
                    self.arr.remove(key)
                    print(key.name + " has not released their beta values")
            except:
                break

        returnedArr = []
        for elem in self.arr:
            returnedArr.append(elem.name)
        return returnedArr


    def mergeSort(self, val) -> list:  # calls insertion sort based on input
        if val == "market cap":
            return self.mergeSort_MC()
        elif val == "pe":
            return self.mergeSort_PE()
        elif val == "eps":
            return self.mergeSort_EPS()
        elif val == "volume":
            return self.mergeSort_volume()
        else:
            return self.mergeSort_beta()

    def mergeSort_MC_r(self, arr) -> list:
        try:
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                self.mergeSort_MC_r(left)
                self.mergeSort_MC_r(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i].marketCap < right[j].marketCap:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                return arr
        except:
            return arr

    def mergeSort_MC(self) -> list:  # insertion sort based on market cap
        changedList = self.arr
        # for elem in changedList:
        #     if elem.marketCap == 'N/A':
        #         changedList.remove(elem)
        return self.mergeSort_MC_r(changedList)

    def mergeSort_volume_r(self, arr) -> list:
        try:
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                self.mergeSort_volume_r(left)
                self.mergeSort_volume_r(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i].volume < right[j].volume:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                return arr
        except:
            return arr

    def mergeSort_volume(self) -> list:  # insertion sort based on volume
        changedList = self.arr
        # for elem in changedList:
        #     if elem.volume == 'N/A':
        #         changedList.remove(elem)
        return self.mergeSort_volume_r(changedList)
    
    def mergeSort_beta_r(self, arr) -> list:
        try:
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                self.mergeSort_beta_r(left)
                self.mergeSort_beta_r(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i].beta < right[j].beta:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                return arr
        except:
            return arr

    def mergeSort_beta(self) -> list:  # insertion sort based on beta
        changedList = self.arr
        # for elem in changedList:
        #     if elem.beta == 'N/A':
        #         changedList.remove(elem)
        return self.mergeSort_beta_r(changedList)

    def mergeSort_EPS_r(self, arr) -> list:
        try:
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                self.mergeSort_EPS_r(left)
                self.mergeSort_EPS_r(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i].EPS < right[j].EPS:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                return arr
        except:
            return arr

    def mergeSort_EPS(self) -> list:  # insertion sort based on earnings per share
        changedList = self.arr
        # for elem in changedList:
        #     if elem.EPS == 'N/A':
        #         changedList.remove(elem)
        return self.mergeSort_EPS_r(changedList)

    def mergeSort_PE_r(self, arr) -> list:
        try:
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                self.mergeSort_PE_r(left)
                self.mergeSort_PE_r(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i].PE < right[j].PE:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                return arr
        except:
            return arr

    def mergeSort_PE(self) -> list:  # insertion sort based on price to earnings
        changedList = self.arr
        # for elem in changedList:
        #     if elem.PE == 'N/A':
        #         changedList.remove(elem)
        return self.mergeSort_PE_r(changedList)