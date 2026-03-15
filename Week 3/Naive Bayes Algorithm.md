# Kelompok 4
| Name           | NRP        |
| ---            | ---        |
| Andie Azril Alfrianto | 5025241054 |
| Azil Alriansyah Hidayat | 5025241070 |
| Farras Nizar | 5025241143 |
| Rafi Aqila Maulana | 5025241165 |

### Teori Bayes
Bayes’ Theorem is a probability theory used to determine the probability of an event based on prior knowledge or existing evidence.
```
P(A|B) = P(B|A)P(A)
         ----------
            P(B)
```
Explanation:
P(A|B) : Probability of event A given that B occurs
P(B|A) : Probability of event B given that A occurs
P(A) : Prior probability of A
P(B) : Probability of B

### Naive Bayes Algorithm
Naive Bayes is a classification algorithm in machine learning that applies Bayes’ Theorem with a simplifying assumption that all features are independent of each other.
The basic steps are:
1. Calculate Prior Probability
Determine the probability of each class in the dataset.
2. Calculate Likelihood
Determine the probability of each feature appearing in each class.
3. Calculate Posterior Probability
Apply Bayes’ Theorem to determine the probability of each class given the input data.
4. The class with the highest probability is chosen as the prediction result.
