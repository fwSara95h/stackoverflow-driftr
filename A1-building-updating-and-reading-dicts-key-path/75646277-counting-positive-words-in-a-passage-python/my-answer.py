# Code from my Stack Overflow answer https://stackoverflow.com/a/75646470 (posted 2023-03-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def calculate_words(x, pList=['good'], nList=['bad']):
    x_words = x.split() ## without cleaning
    # x_words = clean_text(x).split() ## words after cleaning
    num_pos_words, num_neg_words = 0, 0
    for w in x_words:
        if w in pList: num_pos_words += 1
        elif w in nList: num_neg_words += 1

    num_words_total = num_pos_words + num_neg_words # only count if +ve or -ve
    # num_words_total = len(x_words) # count ALL words

    return {  'num_pos_words': num_pos_words,
              'num_neg_words': num_neg_words,
              'num_words_total': num_words_total  }

passage_word_counts = calculate_words(passage_excerpt, pos_words, neg_words)

# --- block 2 ---
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 3}
>

# --- block 3 ---
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 15}
>

# --- block 4 ---
import collections

# passage_words = clean_text(passage_excerpt).split() 
passage_words = passage_excerpt.split()
passage_word_counts = {**collections.Counter(
    'num_pos_words' if w in pos_words else (
        'num_neg_words' if w in neg_words else 'num_na_words'
    ) for w in passage_excerpt.split()
), 'num_words_total': len(passage_words)}

# --- block 5 ---
> # passage_word_counts = \
> {'num_na_words': 12,
>  'num_pos_words': 2,
>  'num_neg_words': 1,
>  'num_words_total': 15}
>

# --- block 6 ---
import collections

# passage_words = clean_text(passage_excerpt).split() 
passage_words = passage_excerpt.split()
passage_word_counts = collections.Counter((
    'num_pos_words' if w in pos_words else 'num_neg_words'    
) for w in passage_excerpt.split() if w in pos_words+neg_words)
passage_word_counts['num_words_total'] = sum(passage_word_counts.values())

# --- block 7 ---
> # passage_word_counts = \
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 3}
>
