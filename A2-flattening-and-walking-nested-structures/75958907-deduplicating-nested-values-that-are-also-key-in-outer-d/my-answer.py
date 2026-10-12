# Code from my Stack Overflow answer https://stackoverflow.com/a/75961692 (posted 2023-04-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for k in [*x]: 
    for z in x.get(k, []): 
        x.pop(z, None)

# --- block 2 ---
for k in [*x]: [x.pop(z,None) for z in x.get(k,[])]

# --- block 3 ---
x_dedup = {k: [z for z in y if z not in x] for k,y in x.items()}

# --- block 4 ---
> {
>   'A fantastic gift for art lovers': ['Designed for adults, this stunning piece of 3D art can be proudly displayed on a wall following a rewarding build experience.'],
>   'Build and relax': ['Art lovers can enjoy a relaxing and immersive building experience as they create this unique artwork from 1,810 pieces.'],
>   'Create your own artwork': ['Build Hokusai’s The Great Wave with layers of LEGO® bricks.'],
>   'Finishing touch': ['Add a decorative tile with Hokusai’s signature.'],
>   'Hokusai – The Great Wave': [
>     'Build Hokusai’s The Great Wave with layers of LEGO® bricks.',
>     'The picture’s multiple layers create a stunning 3D effect.',
>     'Add a decorative tile with Hokusai’s signature.'
>   ],
>   'Immerse yourself in the world of art': ['Listen to the set’s Soundtrack, tailor-made with content to enhance the time you spend building this Japanese wall art.'],
>   'Recreate an iconic piece of Japanese art': ['Celebrate your passion for Japanese art when you build this incredible LEGO® version of Hokusai’s The Great Wave.'],
>   'The Great Wave comes to life!': ['The picture’s multiple layers create a stunning 3D effect.']
> }
>
