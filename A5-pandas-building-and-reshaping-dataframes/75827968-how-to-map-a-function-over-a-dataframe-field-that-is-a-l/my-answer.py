# Code from my Stack Overflow answer https://stackoverflow.com/a/75845119 (posted 2023-03-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
df = pd.DataFrame(
    columns=['STUDENT_ID', 'RECORD_ID', 'NODE_NAME', 'ACTIVITY_NAME', 'ACTIVITY_GRADE'],
    data=[  ['FredID', 'gobbledeegook1', 'Node1', 'MyActivity1', 'PreK, Kindergarten PreK'], 
            ['FredID', 'gobbledeegook2', 'Node1', 'MyActivity1', 'Kindergarten PreK'], 
            ['FredID', 'gobbledeegook3', 'Node2', 'MyActivity2', '1st Grade 1st Grade'], 
            ['JaniceID', 'gobbledeegook4', 'Node3', 'MyActivity3', 'Kindergarten Kindergarten'], 
            ['JaniceID', 'gobbledeegook5', 'Node3', 'MyActivity3', '1st Grade Preschool']    ]
)

# --- block 2 ---
## I changed "Pre-K" to "PreK" since that's how it seems to be in your dataset
index_to_grade = {-2: 'Preschool', -1: 'PreK', 0: 'Kindergarten', 1: '1st Grade', 2: '2nd Grade', 3: '3rd Grade', 4: '4th Grade', 5: '5th Grade'}
# grade_to_index = {g: i for i, g in index_to_grade.items()} ## not needed for my solution

# --- block 3 ---
def get_min_gi(grades:str, refDict=index_to_grade, defaultVal=None):
    inds = [i for i,g in refDict.items() if g in grades]
    return min(inds) if inds else defaultVal

# --- block 4 ---
df['min_grade'] = df['ACTIVITY_GRADE'].apply(get_min_gi) ## will be over-written
min_node_grade_index = df.groupby('NODE_NAME')['min_grade'].transform('min')
df['min_grade'] = min_node_grade_index.map(index_to_grade) ## over-write

# --- block 5 ---
# df['row_min_grade'] = df['ACTIVITY_GRADE'].apply(get_min_gi) # temporary 
df['row_min_grade'] = [min([grade_to_index.get(v,v) for v in i]) for i in df['ACTIVITY_GRADE'].str.split(","‌​)] # temporary 
df['min_node_grade'] = df.groupby('NODE_NAME')['row_min_grade'].transform('min').map(inv_map) 
df['min_activity_grade'] = df.groupby('ACTIVITY_NAME')['row_min_grade'].transform('min').map(inv_map)
df.drop(['row_min_grade'], axis='columns') # drop temporary column
