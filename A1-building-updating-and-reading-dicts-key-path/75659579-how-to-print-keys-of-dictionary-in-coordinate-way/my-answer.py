# Code from my Stack Overflow answer https://stackoverflow.com/a/75668131 (posted 2023-03-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
bgChar = '+' # '▪' # '●' # ' ' # '⁜' # set a "background" character
dic2 = {(0,0):'⬃', (-2,-2):'⇩', (-2,-3):'⇩'}

getRange = lambda l: (min(l), max(l))
x_min, x_max = getRange([c[0] for c in dic2])
y_min, y_max = getRange([c[1] for c in dic2])

myCanvas = [[f'{bgChar:^3}']*(x_max-x_min+3) for _ in range(y_max-y_min+3)]
for (x,y),v in dic2.items(): 
    myCanvas[y+1-y_min][x+1-x_min] = f'{v:^3}'

print(' '*3+''.join([f'{i+1+x_min:^3}' for i in range(x_max - x_min + 3)]))
for i, r in list(enumerate(myCanvas))[::-1]: 
    print(''.join([f'{i-1+y_min:^3}']+r))

# --- block 2 ---
import matplotlib.pyplot as plt

dic2={(0,0):'⬃',(-2,-2):'⇩',(-2,-3):'⇩'}
getRange = lambda l: (min(l), max(l))
x_min, x_max = getRange([c[0] for c in dic2])
y_min, y_max = getRange([c[1] for c in dic2])

fig, myCanvas = plt.subplots()
myCanvas.set_xlim(x_min-1, x_max+1)
myCanvas.set_ylim(y_min-1, y_max+1)

for xy, v in dic2.items(): myCanvas.annotate(v, xy, xy)
plt.show()
