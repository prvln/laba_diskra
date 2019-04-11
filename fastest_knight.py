m = input("Input start: ")
n = input("Input finish: ")

W = 26 + 2
H = 26 + 2

dx_x = 0
dy_y = 0

C = 0                                               #scetchick

alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

bukva_1 = m[0]
chislo_1 = m[1:]

bukva_2 = n[0]
chislo_2 = n[1:]

for i in range(len(alfa)):                          #perevod bukv v chisla
    if bukva_1 == alfa[i]:
        bukva_1 = i + 1

    if bukva_2 == alfa[i]:
        bukva_2 = i + 1

bukva_1 = int(bukva_1)
bukva_2 = int(bukva_2)
chislo_1 = int(chislo_1)
chislo_2 = int(chislo_2)

h = [['0' for j in range(W)] for i in range(H)]

for i in range(W):                                  #mas doska
    h[0][i] = '*'
    h[i][0] = '*'
    h[i][W-1] = '*'
    h[W-1][i] = '*'
    h[bukva_1][chislo_1] = '$'                      # start
    h[bukva_2][chislo_2] = '~'                      # finish

dx = [2, 1, -1, -2, -2, -1, 1, 2]                   #vozmojnie hodi konya po X and Y
dy = [1, 2, 2, 1, -1, -2, -2, -1]

minimal = 50

rasstt = int(pow(pow(bukva_2 - bukva_1, 2) + pow(chislo_2 - chislo_1, 2), 0.5))
rasstt = rasstt/1.8
if rasstt < 4: rasstt = 4
            
last_rasst = pow(pow(bukva_2 - bukva_1, 2) + pow(chislo_2 - chislo_1, 2), 0.5)

def volna(C,x,y):
    
    global minimal
    global last_rasst
    
    last_rasst = pow(pow(bukva_2 - x, 2) + pow(chislo_2 - y, 2), 0.5)

    C += 1
    
    if C > rasstt:
        return 0
    
    for i in range(8):
        dx_x = dx[i]
        dy_y = dy[i]
        
        a = x + dx_x
        b = y + dy_y
        
        rasst = pow(pow(bukva_2 - a, 2) + pow(chislo_2 - b, 2), 0.5)

        if not(a > 26 or a < 1 or b > 26 or b < 1):
            
            if last_rasst <= rasst and C > 3:
                continue
            
            else:
                last_rasst = rasst
                
                if h[a][b] == '~':
                    
                    if minimal > C:                        
                        print("Otvet:",C)
                        minimal = C
                        
                    else:
                        continue
                else:
                    h[a][b] = C
                    volna(C,a,b)
        last_rasst = rasst

volna(C,bukva_1,chislo_1)

