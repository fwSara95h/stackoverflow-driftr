---
title: "Generating txt file from HTML file using python"
site: stackoverflow
question_id: 74249278
url: https://stackoverflow.com/q/74249278
asked: 2022-10-29T22:24:42Z
asked_by: "Steve Yonkeu"
asked_by_url: https://stackoverflow.com/users/16436036
last_edited: 2022-10-29T23:06:05Z
tags: [python, css, python-3.x, beautifulsoup]
score: -1
views_at_snapshot: 117
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 63825595389c73771e74452fb483156696e84a222ababcd66da0e6c8524405a9
---

# Generating txt file from HTML file using python

Asked by [Steve Yonkeu](https://stackoverflow.com/users/16436036) on Stack Overflow, <https://stackoverflow.com/q/74249278>, 2022-10-29, last edited 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Have been trying to implement the HTML to plain text conversion and had some issues so far.

From an HTML format like this:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-html -->

    <style>
    .first{
      text-align: center;
    }
    .second{
      margin-left: 20px;
    }
    </style>

    <p class="first">Hello world to all</p>
    <p class="second">What is this</p>

<!-- end snippet -->

I should get an output as:

```txt
                              hello world to all

   what is this
```

I need an advice for this please. 

I tried beautifulsoup4 and html2text but they have some lacking and not giving the required output.

So far I tried this snippet, from [GeeksToGeeks][1]

```
# importing the library
from bs4 import BeautifulSoup
from urllib import request
 
# Initializing variable
url = "https://www.geeksforgeeks.org/matrix-introduction/"
gfg = BeautifulSoup(request.urlopen(url).read())
 
# Extracting data for article section
bodyHtml = gfg.find('article', {'class' : 'content'})
 
# Calculating result
res = bodyHtml.get_text()
 
# Printing the result
print(res)
```

### Output
<pre>Mathematics | Matrix IntroductionView Discussion

Improve Article

Save Article

Like Article

Difficulty Level :
EasyLast Updated :
17 Aug, 2022ReadDiscussView Discussion

Improve Article

Save Article

Like Article

A matrix represents a collection of numbers arranged in an order of rows and columns. It is necessary to enclose the elements of a matrix in parentheses or brackets. A matrix with 9 elements is shown below.   This Matrix [M] has 3 rows and 3 columns. Each element of matrix [M] can be referred to by its row and column number. For example, a23 = 6  Order of a Matrix: The order of a matrix is defined in terms of its number of rows and columns. Order of a matrix = No. of rows ×No. of columns Therefore Matrix [M] is a matrix of order 3 × 3. Transpose of a Matrix : The transpose [M]T of an m x n matrix [M] is the n x m matrix obtained by interchanging the rows and columns of [M]. if A = [aij] mxn , then AT = [bij] nxm where bij = aji Properties of the transpose of a matrix: (AT)T = A(A+B)T = AT + BT(AB)T = BTATSingular and Nonsingular Matrix: Singular Matrix: A square matrix is said to be a singular matrix if its determinant is zero i.e. |A|=0Nonsingular Matrix: A square matrix is said to be a non-singular matrix if its determinant is non-zero.Properties of Matrix addition and multiplication: A + B = B + A (Commutative)(A + B) + C = A + (B + C) (Associative)AB ? BA (Not Commutative)(AB) C = A (BC) (Associative)A (B+C) = AB + AC (Distributive)Types of Matrices:Square Matrix: A square Matrix has as many rows as it has columns. i.e. no of rows = no of columns. Symmetric matrix: A square matrix is said to be symmetric if the transpose of the original matrix is equal to its original matrix. i.e. (AT) = A. Skew-symmetric: A skew-symmetric (or antisymmetric or antimetric[1]) matrix is a square matrix whose transpose equals its negative.i.e. (AT) = -A. Diagonal Matrix: A diagonal matrix is a square matrix in which the entries outside the main diagonal are all zero. The term usually refers to square diagonal matrices. Identity Matrix: A square matrix in which all the elements of the principal diagonal are ones and all other elements are zeros. Identity matrix is denoted as I. Orthogonal Matrix: A matrix is said to be orthogonal if AAT = ATA = I Idempotent Matrix: A matrix is said to be idempotent if A2 = A Involuntary Matrix: A matrix is said to be Involuntary if A2 = I. Zero or Null Matrix: A matrix is said to zero or null matrix if all its elements are zeroUpper Triangular Matrix: A square matrix in which all the elements below the diagonal are zero is known as the upper triangular matrixLower Triangular Matrix: A square matrix in which all the elements above the diagonal are zero is known as the lower triangular matrixNote: Every Square Matrix can uniquely be expressed as the sum of a symmetric matrix and skew-symmetric matrix. A = 1/2 (AT + A) + 1/2 (A – AT). Determinant of a matrix :The determinant of a matrix is a number associated with that square matrix. The determinant of a matrix can only be calculated for a square matrix. It is represented by |A|.Example: Input: 2 X 2 MatrixThen, the determinant is -&gt; |A| = ad – bcAdjoint of a square matrix: The adjoint of a matrix A is the transpose of the cofactor matrix of A  Properties of Adjoint: A(Adj A) = (Adj A) A = |A| InAdj(AB) = (Adj B) . (Adj A)|Adj A| = |A|n-1Adj(kA) = kn-1 Adj(A)|adj(adj(A))| = |A| ^ (n-1) ^ 2adj(adj(A)) = |A| ^ (n-2)    *  AIf A = [L,M,N] then adj(A) = [MN, LN, LM]adj(I) = IWhere, “n = number of rows = number of columns”The inverse of a square matrix:  Here |A| should not be equal to zero, which means matrix A should be non-singular. Properties of the inverse: (A-1)-1 = A (AB)-1 = B-1A-1 only a non singular square matrix can have an inverse. Where should we use the inverse matrix? If you have a set of simultaneous equations: 7x + 2y + z = 213y – z = 5 -3x + 4y – 2x = -1 As we know when AX = B, then X = A-1B so we can calculate the inverse of A and by multiplying it by B, we can get the values of x, y, and z. Trace of a matrix: The trace of a matrix is denoted as tr(A) which is used only for square matrix and equals the sum of the diagonal elements of the matrix. Remember trace of a matrix is also equal to the sum of the eigenvalue of the matrix. For example:   This article is contributed by Nitika Bansal. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.My Personal Notes
arrow_drop_upSave
</pre>

### Expectation
From what I expected I was to get this result

```Mathematics | Matrix Introduction

    Difficulty Level : Easy
    Last Updated : 17 Aug, 2022

Read
Discuss

A matrix represents a collection of numbers arranged in an order of rows and columns. It is necessary to enclose the elements of a matrix in parentheses or brackets. 
A matrix with 9 elements is shown below. 
 

\begin{bmatrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9\end{bmatrix}
 

This Matrix [M] has 3 rows and 3 columns. Each element of matrix [M] can be referred to by its row and column number. For example, a23 = 6 

 
Order of a Matrix: 

The order of a matrix is defined in terms of its number of rows and columns. 
Order of a matrix = No. of rows ×No. of columns 
Therefore Matrix [M] is a matrix of order 3 × 3. 
Transpose of a Matrix : 

The transpose [M]T of an m x n matrix [M] is the n x m matrix obtained by interchanging the rows and columns of [M]. 
if A = [aij] mxn , then AT = [bij] nxm where bij = aji 
Properties of the transpose of a matrix: 

    (AT)T = A
    (A+B)T = AT + BT
    (AB)T = BTAT

Singular and Nonsingular Matrix: 

    Singular Matrix: A square matrix is said to be a singular matrix if its determinant is zero i.e. |A|=0
    Nonsingular Matrix: A square matrix is said to be a non-singular matrix if its determinant is non-zero.

Properties of Matrix addition and multiplication: 

    A + B = B + A (Commutative)
    (A + B) + C = A + (B + C) (Associative)
    AB ? BA (Not Commutative)
    (AB) C = A (BC) (Associative)
    A (B+C) = AB + AC (Distributive)

Types of Matrices:

    Square Matrix: A square Matrix has as many rows as it has columns. i.e. no of rows = no of columns. 
    Symmetric matrix: A square matrix is said to be symmetric if the transpose of the original matrix is equal to its original matrix. i.e. (AT) = A. 
    Skew-symmetric: A skew-symmetric (or antisymmetric or antimetric[1]) matrix is a square matrix whose transpose equals its negative.i.e. (AT) = -A. 
    Diagonal Matrix: A diagonal matrix is a square matrix in which the entries outside the main diagonal are all zero. The term usually refers to square diagonal matrices. 
    Identity Matrix: A square matrix in which all the elements of the principal diagonal are ones and all other elements are zeros. Identity matrix is denoted as I. 
    Orthogonal Matrix: A matrix is said to be orthogonal if AAT = ATA = I 
    Idempotent Matrix: A matrix is said to be idempotent if A2 = A 
    Involuntary Matrix: A matrix is said to be Involuntary if A2 = I. 
    Zero or Null Matrix: A matrix is said to zero or null matrix if all its elements are zero
    Upper Triangular Matrix: A square matrix in which all the elements below the diagonal are zero is known as the upper triangular matrix
    Lower Triangular Matrix: A square matrix in which all the elements above the diagonal are zero is known as the lower triangular matrix

Note: Every Square Matrix can uniquely be expressed as the sum of a symmetric matrix and skew-symmetric matrix. A = 1/2 (AT + A) + 1/2 (A – AT). 
Determinant of a matrix :

The determinant of a matrix is a number associated with that square matrix. The determinant of a matrix can only be calculated for a square matrix. It is represented by |A|.

Example: 

    Input: 2 X 2 Matrix

    \text{If A = }\begin{bmatrix} a & b \\ c & d \end{bmatrix}\text{then,}

    Then, the determinant is -> |A| = ad – bc

Adjoint of a square matrix: The adjoint of a matrix A is the transpose of the cofactor matrix of A

\text{If A = }\begin{bmatrix} a_1 & b_1 & c_1\\ a_2 & b_2 & c_2\\ a_3 & b_3 & c_3 \end{bmatrix}\text{then,}
 
\text{Adj A = Transpose of }\begin{bmatrix} A_1 & B_1 & C_1\\ A_2 & B_2 & C_2\\ A_3 & B_3 & C_3 \end{bmatrix}\text{=} \begin{bmatrix} A_1 & A_2 & A_3\\ B_1 & B_2 & B_3\\ C_1 & C_2 & C_3 \end{bmatrix}

\text Where, \begin{bmatrix} A_1 & B_1 & C_1\\ A_2 & B_2 & C_2\\ A_3 & B_3 & C_3 \end{bmatrix} \text {is cofactor matrix of A}
 
Properties of Adjoint: 

    A(Adj A) = (Adj A) A = |A| In
    Adj(AB) = (Adj B) . (Adj A)
    |Adj A| = |A|n-1
    Adj(kA) = kn-1 Adj(A)
    |adj(adj(A))| = |A| ^ (n-1) ^ 2
    adj(adj(A)) = |A| ^ (n-2)    *  A
    If A = [L,M,N] then adj(A) = [MN, LN, LM]
    adj(I) = I

Where, “n = number of rows = number of columns”
The inverse of a square matrix: 

A^{-1} = \frac{Adj A}{|A|}
 

Here |A| should not be equal to zero, which means matrix A should be non-singular. 
Properties of the inverse: 

    (A-1)-1 = A 
    (AB)-1 = B-1A-1 
    only a non singular square matrix can have an inverse. 

Where should we use the inverse matrix? 

If you have a set of simultaneous equations: 

7x + 2y + z = 21
3y – z = 5 
-3x + 4y – 2x = -1 

As we know when AX = B, then X = A-1B so we can calculate the inverse of A and by multiplying it by B, we can get the values of x, y, and z. 
Trace of a matrix: 

The trace of a matrix is denoted as tr(A) which is used only for square matrix and equals the sum of the diagonal elements of the matrix. Remember trace of a matrix is also equal to the sum of the eigenvalue of the matrix. For example: 

\begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9 \end{bmatrix} \text{ tr(A) = 1+5+9 = 15}
 

 

This article is contributed by Nitika Bansal. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
```

- If I want to include styling using CSS to the the html file before conversion, what should I use?

- For a more convenient generated file, is the `html` or `beautifulsoup4` or `html2txt` library convenient. 


  [1]: https://www.geeksforgeeks.org/converting-html-to-text-with-beautifulsoup/

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Grismar](https://stackoverflow.com/users/4390160)** (2022-10-29): Have a look at [on topic](https://stackoverflow.com/help/on-topic) and [how to ask](https://stackoverflow.com/help/ask). "How to solve this problem with code" is not [on topic for StackOverflow](https://meta.stackoverflow.com/questions/284236/why-is-can-someone-help-me-not-an-actual-question). Try to [make an honest attempt](https://meta.stackoverflow.com/questions/261592/how-much-research-effort-is-expected-of-stack-overflow-users) at solving the problem yourself, and then feel free to ask specific questions about your solution, or problems with it.
- **[saxbophone](https://stackoverflow.com/users/6177253)** (2022-10-29): Please show the actual output you're getting when you try the sample code you've shown
- **[A Haworth](https://stackoverflow.com/users/10867454)** (2022-10-30): What do you mean by 'plain text'. The example you show has done something to center that heading - tabs? or spaces? How much of the formatting are you going to try to emulate using spaces?
- **me** (2022-10-30): Are you looking for something like https://tex.stackexchange.com/questions/167523/html-to-latex-how-can-i-use-python-and-lxml-to-convert-an-html-document-to-late
- **[Steve Yonkeu](https://stackoverflow.com/users/16436036)** (2022-10-30): @Driftr95 that's not what I want.
- **[Steve Yonkeu](https://stackoverflow.com/users/16436036)** (2022-10-30): @AHaworth when I mean plaintext I'm talking of a formatted txt document with may be tabs and list included. So kind of proper formatting from the styling
- **[A Haworth](https://stackoverflow.com/users/10867454)** (2022-10-30): So it would be approximations to positioning using spaces, tabs, CR LF and any other characters you will allow? Is the text to be pure ASCII?
- **[Steve Yonkeu](https://stackoverflow.com/users/16436036)** (2022-10-30): ASCII will be find by me though
