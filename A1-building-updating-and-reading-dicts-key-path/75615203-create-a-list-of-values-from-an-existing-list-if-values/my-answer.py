# Code from my Stack Overflow answer https://stackoverflow.com/a/75637960 (posted 2023-03-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
apData = [{"Name": 'A', "Area": 10000, "Price": 100}, {"Name": 'B', "Area": 9500, "Price": 99}, {"Name": 'C', "Area": 11000, "Price": 101}, {"Name": 'D', "Area": 12000, "Price": 150}, {"Name": 'E', "Area": 14000, "Price": 200}, {"Name": 'F', "Area": 14500, "Price": 400}, {"Name": 'G', "Area": 12999, "Price": 159}]

threshRef = {'Area':1000, 'Price':10}
ck_margins = lambda c,n: all(abs(n[k]-c[k])<=threshRef[k] for k in threshRef)

# --- block 2 ---
selected, unselected = [], []
for i, cur in enumerate(apData):
    selectCur = any(ck_margins(cur,d) for di,d in enumerate(apData) if di!=i) 
    (selected if selectCur else unselected).append(cur)

# --- block 3 ---
selected, unselected = [], []
for i, cur in enumerate(apData):
    selectCur = False
    for di, d in enumerate(apData):
        if di!=i and ck_margins(cur,d):
            selectCur = True
            break
    (selected if selectCur else unselected).append(cur)

# --- block 4 ---
selected, unselected, hasNeighbor = [], [], [False]*len(apData)

for i1, d1 in enumerate(apData):
    for i2, d2 in enumerate(apData[i1+1:], i1+1):
        if ck_margins(d1,d2): hasNeighbor[i1] = hasNeighbor[i2] = True

for cur, selectCur in zip(apData,hasNeighbor): 
    (selected if selectCur else unselected).append(cur)

# --- block 5 ---
apSorted = sorted(apData, key=lambda d: [d[k] for k in threshRef])

selected, unselected = [], []
for prev, cur, nxt in zip([{}]+apSorted[:-1], apSorted, apSorted[1:]+[{}]):
    selectCur = any(ck_margins(cur, x) for x in [prev, nxt] if x)
    (selected if selectCur else unselected).append(cur)

# --- block 6 ---
ap_sort_pad = [{}] + sorted(apData, key=lambda d: [d[k] for k in threshRef]) + [{}]

selected, unselected = [], []
for i in range(len(ap_sort_pad)-2):
    prev, cur, nxt = ap_sort_pad[i:i+3]
    selectCur = any(ck_margins(cur, x) for x in [prev, nxt] if x)
    (selected if selectCur else unselected).append(cur)
