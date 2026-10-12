# Code from my Stack Overflow answer https://stackoverflow.com/a/75638136 (posted 2023-03-04), extracted verbatim; may need the question's context to run.
dwarfs, colors = [], {}
while (entry := input())!='Once upon a time':
    name,hat_color,physics = entry.split(" <:> ")
    obj = Dwarf(name, hat_color, int(physics))

    for i, d in enumerate(dwarfs):
        if d.name==name and d.hat_color==hat_color:
            dwarfs.pop(i)
            break
    else: colors[hat_color] = colors.get(hat_color,0)+1
    dwarfs.append(obj) 

# colors = dict(sorted(colors.items(),key=lambda x:-x[1])) # ? unnecessary ?
dwarfs.sort(key=lambda x:(-x.physics, -colors[x.hat_color]))

print(*dwarfs, sep='\n')
