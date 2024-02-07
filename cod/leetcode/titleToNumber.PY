class Solution(object):
    
    def titleToNumber(self, columnTitle):
        dict_list = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        if(len(columnTitle)==1 and columnTitle in dict_list):
            return dict_list[columnTitle]
        else:
            val,temp = 1,(len(columnTitle)-1)
            for i in range(len(columnTitle)):
                if(i==(len(columnTitle)-1)):
                    val += dict_list[columnTitle[i]]
                else:
                    val = val + (26 ** temp)* dict_list[columnTitle[i]]
                    temp = temp -1
            return val-1
if __name__ == '__main__':
    sl = Solution()
    
    print(sl.titleToNumber("AA"))

