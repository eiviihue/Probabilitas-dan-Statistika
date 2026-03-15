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
P(A|B) = (P(B|A) * P(A)) / P(B)
```
Explanation:<br>
P(A|B) : Probability of event A given that B occurs<br>
P(B|A) : Probability of event B given that A occurs<br>
P(A) : Prior probability of A<br>
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

### Dataset
| No | Outlook  | Temperature | Humidity | Wind   | Play Soccer |
| -- | -------- | ----------- | -------- | ------ | ----------- |
| 1  | Sunny    | Mild        | Normal   | Weak   | Play        |
| 2  | Overcast | Mild        | High     | Weak   | Play        |
| 3  | Sunny    | Cool        | Normal   | Weak   | Play        |
| 4  | Overcast | Hot         | High     | Strong | Not Play    |
| 5  | Rainy    | Mild        | High     | Strong | Not Play    |
| 6  | Sunny    | Mild        | Normal   | Strong | Play        |
| 7  | Rainy    | Cool        | Normal   | Weak   | Play        |
| 8  | Sunny    | Hot         | High     | Weak   | Not Play    |
| 9  | Rainy    | Mild        | High     | Weak   | Play        |
| 10 | Overcast | Cool        | Normal   | Strong | Not Play    |

#### Prior Probability
| Class    | Count | Probability |
| -------- | ----- | ----------- |
| Play     | 6     | 6/10 = 0.6  |
| Not Play | 4     | 4/10 = 0.4  |

#### Likelihood Probabilities
| Outlook  | Play | Not Play | P(Outlook&#124;Play) | P(Outlook&#124;Not Play) |
| -------- | ---- | -------- | --------------- | ------------------- |
| Sunny    | 3    | 1        | 3/6 = 0.50      | 1/4 = 0.25          |
| Overcast | 1    | 2        | 1/6 = 0.17      | 2/4 = 0.50          |
| Rainy    | 2    | 1        | 2/6 = 0.33      | 1/4 = 0.25          |

| Temperature | Play | Not Play | P(Temperature&#124;Play) | P(Temperature&#124;Not Play) |
| ----------- | ---- | -------- | ------------------- | ----------------------- |
| Hot         | 0    | 2        | 0/6 = 0             | 2/4 = 0.50              |
| Mild        | 4    | 1        | 4/6 = 0.67          | 1/4 = 0.25              |
| Cool        | 2    | 1        | 2/6 = 0.33          | 1/4 = 0.25              |

| Humidity | Play | Not Play | P(Humidity&#124;Play) | P(Humidity&#124;Not Play) |
| -------- | ---- | -------- | ---------------- | -------------------- |
| High     | 2    | 3        | 2/6 = 0.33       | 3/4 = 0.75           |
| Normal   | 4    | 1        | 4/6 = 0.67       | 1/4 = 0.25           |

| Wind   | Play | Not Play | P(Wind&#124;Play)  | P(Wind&#124;NotPlay) |
| ------ | ---- | -------- | ---------- | ------------ |
| Weak   | 5    | 1        | 5/6 = 0.83 | 1/4 = 0.25   |
| Strong | 1    | 3        | 1/6 = 0.17 | 3/4 = 0.75   |

#### Naive Bayes Calculation
```
P(Play|X) = P(Play) × P(O|Play) × P(T|Play) × P(H|Play) × P(W|Play)
```
```
P(NotPlay|X) = P(NotPlay) × P(O|NotPlay) × P(T|NotPlay) × P(H|NotPlay) × P(W|NotPlay)
```
| No | P(Play&#124;X) | P(NotPlay&#124;X) | Prediction |
|----|---------------|------------------|------------|
| 1  | 0.1110        | 0.0016           | Play       |
| 2  | 0.0187        | 0.0094           | Play       |
| 3  | 0.0550        | 0.0016           | Play       |
| 4  | 0.0000        | 0.0563           | Not Play   |
| 5  | 0.0074        | 0.0141           | Not Play   |
| 6  | 0.0228        | 0.0047           | Play       |
| 7  | 0.0360        | 0.0016           | Play       |
| 8  | 0.0000        | 0.0094           | Not Play   |
| 9  | 0.0366        | 0.0047           | Play       |
|10  | 0.0038        | 0.0094           | Not Play   |

#### Predicted vs Actual
| No | Actual   | Predicted | Result    |
| -- | -------- | --------- | --------- |
| 1  | Play     | Play      | Correct   |
| 2  | Play     | Play      | Correct   |
| 3  | Play     | Play      | Correct   |
| 4  | Not Play | Not Play  | Correct   |
| 5  | Not Play | Not Play  | Correct   |
| 6  | Play     | Play      | Correct   |
| 7  | Play     | Play      | Correct   |
| 8  | Not Play | Not Play  | Correct   |
| 9  | Play     | Play      | Correct   |
| 10 | Not Play | Play      | Correct |

Accuracy = (10 / 10) × 100%
         = 100%
