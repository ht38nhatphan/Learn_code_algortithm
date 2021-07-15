# Cho một chuỗi s chứa một biểu thức chỉ chứa:

# Các toán hạng.
# Các toán tử  "+-*^"
# Các dấu ngoặc "()"
# Ẩn x .
# Hãy trả về biểu thức rút gọn của biểu thức trong s. Biểu thức sau khi rút gọn sẽ theo quy tắc:

# Hệ số của ẩn sẽ được xếp trước ẩn.
# Ẩn có lũy thừa lớn hơn sẽ được xếp trước.
# Các dấu ngoặc sẽ biến mất.
# Ví dụ:

# Với s = "3*(x^2+x)+15" thì compactExpression(s)="3*x^2+3*x+15".
# Với s = "3-x" thì compactExpression(s)="-x+3".
# Với s = "(9*x^3+5*x)*6*x+4" thì compactExpression(s)="54*x^4+30*x^2+4".
# [Đầu vào/Đầu ra]:

# [Thời gian chạy]: 0.1s với C++, 0.6s với Java và C#, 0.8s với Python, Go và JavaScript.
# [Đầu vào]string 
# Đầu vào luôn thỏa mãn các hệ số và số mũ nhỏ hơn hoặc bằng 10^4 , các ẩn sẽ không nằm trên các lũy thừa và các lũy không âm.
# 1<=s.length<=100
# [Đầu ra]string
#code by nhat phan


def compactExpression(s):
    s = s.replace("^","**")
    chot = 1000000000/2
    s2 = str(eval(s.replace("x","1000000000")))
    #print(len(s2))
    hs = []
    am = False
    if s2[0] == '-':
        am = True
        s2 = s2[1:]
    i = len(s2) - 1
    nho = False
    nho2 = False
    while i >= 0:
        if i >= 8:
            n = int(s2[i - 8: i + 1])
            if n <= chot:hs.append(n)
            else: hs.append(n - 1000000000);nho=True
        else :
            n = int(s2[0:i + 1])
            if n <= chot:hs.append(n)
            else: hs.append(n - 1000000000);nho=True
        i -= 9
        if nho2:
            nho2 = False
            hs[-1] += 1
        if nho: nho2 = True;nho = False
    if nho2: hs.append(1)
    if am:
        for i in range(len(hs)):
            hs[i] = -hs[i]
    res = ""
    for j in range(len(hs) - 1, -1, -1):
        if hs[j] == 0 :
            continue
        if hs[j] == 1 : pass
        elif hs[j] == -1 : res += '-'
        elif hs[j] > 0 : res += "+" + str(hs[j]) 
        else : res += str(hs[j])
        if j != 0 and (hs[j] == -1 or hs[j] == 1):
            if hs[j] == 1: res += "+x"
            else: res += "x"
        elif hs[j] != 0 and j != 0: res += "*x"
        elif (hs[j] == 1 or hs[j] == -1) and j == 0:
            if hs[j] == 1: res += "+1"
            else: res += "1"
        if j != 0 and j != 1:
            res += "^" + str(j)
    if res == "" : return "0"
    if res[0] == '+' : return res[1:]
    else: return res
strs = "3*(x^2+x)+15"
#run
print(compactExpression(strs))