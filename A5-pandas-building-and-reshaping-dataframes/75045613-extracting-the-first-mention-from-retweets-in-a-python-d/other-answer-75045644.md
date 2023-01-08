---
title: "Extracting the first mention from retweets in a python dataframe"
site: stackoverflow
question_id: 75045613
answer_id: 75045644
url: https://stackoverflow.com/a/75045644
author: "akuiper"
author_url: https://stackoverflow.com/users/4983450
posted: 2023-01-08T05:15:51Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d7d067edea4e509445a1440aa50bc0d13e3460aef647ba567b1090f8f7024919
role: another answer on the same question, kept as context; not my work
---

# Answer by [akuiper](https://stackoverflow.com/users/4983450) — 2023-01-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75045644>, 2023-01-08; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can use `numpy.where` to conditionally keep values from extracted value:

    dataframe2['usr_rt'] = np.where(
      dataframe2.rt == 'RT', 
      dataframe2.text_con_RT_t.str.extract('@(\w+)', expand=False).str.lower(), 
      ''
    )
    
    dataframe2
                                  text_con_RT_t  rt  usr_rt
    0  RT @Blanc_: ramdon text #hashtag quiere   RT  blanc_
    1                         @GonM ramdon text            
    2              RT @IvEc: @GonzM ramdon text  RT    ivec
    3                         hOLA ramdon text    

Or if retweets always start with `RT`, you can use regex `RT.*?@(\w+)`:

    dataframe2['usr_rt'] = dataframe2.text_con_RT_t.str.extract('RT.*?@(\w+)', expand=False).str.lower()

    dataframe2
                                  text_con_RT_t  rt  usr_rt
    0  RT @Blanc_: ramdon text #hashtag quiere   RT  blanc_
    1                         @GonM ramdon text         NaN
    2              RT @IvEc: @GonzM ramdon text  RT    ivec
    3                         hOLA ramdon text          NaN
