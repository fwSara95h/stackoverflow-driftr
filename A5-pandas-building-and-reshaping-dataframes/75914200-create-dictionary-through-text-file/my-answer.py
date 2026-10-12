# Code from my Stack Overflow answer https://stackoverflow.com/a/75915909 (posted 2023-04-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
def main():
    inp_filepath = 'world_cup_champions.txt'

    df = pd.read_csv(inp_filepath) ## read from file 
    champions_df = df.groupby('Country').agg(
        Wins=('Year',len), Years=('Year',list), 
        Captains=('Captain', list), Coaches=('Coach', list) )

    champions = champions_df.to_dict('index')

    print(champions_df[['Wins']].assign(
        Years=champions_df['Years'].apply(lambda y: ', '.join(f'{i}' for i in y)) 
    ).sort_values('Wins', ascending=False).to_markdown(tablefmt='rst'))

# --- block 2 ---
> {
>   'Argentina': {'Wins': 2, 'Years': [1978, 1986], 'Captains': ['Daniel Passarella', 'Diego Maradona'], 'Coaches': ['Cesar Luis Menotti', 'Carlos Bilardo']},
>   'Brazil': {'Wins': 5, 'Years': [1958, 1962, 1970, 1994, 2002], 'Captains': ['Hilderaldo Bellini', 'Mauro Ramos', 'Carlos Alberto', 'Dunga', 'Cafu'], 'Coaches': ['Vicente Feola', 'Aymore Moreira', 'Mario Zagallo', 'Carlos Alberto Parreira', 'Luiz Felipe Scolari']},
>   'England': {'Wins': 1, 'Years': [1966], 'Captains': ['Bobby Moore'], 'Coaches': ['Alf Ramsey']},
>   'France': {'Wins': 1, 'Years': [1998], 'Captains': ['Didier Deschamps'], 'Coaches': ['Aime Jacquet']},
>   'Germany': {'Wins': 4, 'Years': [1954, 1974, 1990, 2014], 'Captains': ['Fritz Walter', 'Franz Beckenbauer', 'Lothar Matth�us', 'Philipp Lahm'], 'Coaches': ['Sepp Herberger', 'Helmut Schon', 'Franz Beckenbauer', 'Joachim Low']},
>   'Italy': {'Wins': 4, 'Years': [1934, 1938, 1982, 2006], 'Captains': ['Gianpiero Combi', 'Giuseppe Meazza', 'Dino Zoff', 'Fabio Cannavaro'], 'Coaches': ['Vittorio Pozzo', 'Vittorio Pozzo', 'Enzo Bearzot', 'Marcello Lippi']},
>   'Spain': {'Wins': 1, 'Years': [2010], 'Captains': ['Iker Casillas'], 'Coaches': ['Vicente del Bosque']},
>   'Uruguay': {'Wins': 2, 'Years': [1930, 1950], 'Captains': ['Jose Nasazzi', 'Obdulio Varela'], 'Coaches': ['Alberto Suppici', 'Juan Lopez']}
> }
>

# --- block 3 ---
> =========  ======  ============================
> Country      Wins  Years
> =========  ======  ============================
> Brazil          5  1958, 1962, 1970, 1994, 2002
> Germany         4  1954, 1974, 1990, 2014
> Italy           4  1934, 1938, 1982, 2006
> Argentina       2  1978, 1986
> Uruguay         2  1930, 1950
> England         1  1966
> France          1  1998
> Spain           1  2010
> =========  ======  ============================
>

# --- block 4 ---
def createDict(file_lines):
    finalDict = {}
    rKeys = ['Years', 'Coaches', 'Captains']
    fData = [l.strip().split(',') for l in file_lines[1:]]

    for year,country,coach,captain in fData:
        finalDict.setdefault(country, {'Wins':0, **{k:[] for k in rKeys}})
        finalDict[country]['Wins'] += 1
        for k,v in zip(rKeys,[year,coach,captain]): 
            finalDict[country][k].append(v)
    return finalDict

# --- block 5 ---
def printChamps(unsorted_dict, idx='Country',idxLen=10,ctKey='Wins',cLen=4,**lenRef):
    if not lenRef: 
        lenRef = {'Years':30} ## {'Years':30,'Captains':70,'Coaches':50} ## 

    vals_n_lens = [(idx,idxLen), (ctKey,cLen), *lenRef.items()]
    print("  ".join(f"{k:{l}}" for k,l in vals_n_lens))
    print("  ".join(f"{'='*len(k):{l}}" for k,l in vals_n_lens))

    for c, rDict in sorted(unsorted_dict.items()):
        vals_n_lens = [(c,idxLen), (rDict[ctKey],cLen)]
        vals_n_lens += [(', '.join(rDict.get(k,[])), l) for k, l in lenRef.items()]
        print("  ".join(f"{k:<{l}}" for k,l in vals_n_lens))

# --- block 6 ---
def main():
    inp_filepath = 'world_cup_champions.txt'
    with open(inp_filepath, 'r') as f: 
        champions = createDict(f.readlines())
    printChamps(champions)

# --- block 7 ---
> Country     Wins  Years                         
> =======     ====  =====                         
> Argentina   2     1978, 1986                    
> Brazil      5     1958, 1962, 1970, 1994, 2002  
> England     1     1966                          
> France      1     1998                          
> Germany     4     1954, 1974, 1990, 2014        
> Italy       4     1934, 1938, 1982, 2006        
> Spain       1     2010                          
> Uruguay     2     1930, 1950                    
>

# --- block 8 ---
> Country     Wins  Years                           Captains                                                                Coaches                                           
> =======     ====  =====                           ========                                                                =======                                           
> Argentina   2     1978, 1986                      Daniel Passarella, Diego Maradona                                       Cesar Luis Menotti, Carlos Bilardo                
> Brazil      5     1958, 1962, 1970, 1994, 2002    Hilderaldo Bellini, Mauro Ramos, Carlos Alberto, Dunga, Cafu            Vicente Feola, Aymore Moreira, Mario Zagallo, Carlos Alberto Parreira, Luiz Felipe Scolari
> England     1     1966                            Bobby Moore                                                             Alf Ramsey                                        
> France      1     1998                            Didier Deschamps                                                        Aime Jacquet                                      
> Germany     4     1954, 1974, 1990, 2014          Fritz Walter, Franz Beckenbauer, Lothar Matth�us, Philipp Lahm          Sepp Herberger, Helmut Schon, Franz Beckenbauer, Joachim Low
> Italy       4     1934, 1938, 1982, 2006          Gianpiero Combi, Giuseppe Meazza, Dino Zoff, Fabio Cannavaro            Vittorio Pozzo, Vittorio Pozzo, Enzo Bearzot, Marcello Lippi
> Spain       1     2010                            Iker Casillas                                                           Vicente del Bosque                                
> Uruguay     2     1930, 1950                      Jose Nasazzi, Obdulio Varela                                            Alberto Suppici, Juan Lopez                                        
>
