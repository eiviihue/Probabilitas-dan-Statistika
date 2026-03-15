from collections import defaultdict

# Dataset 
dataset = [
    {"Outlook": "Sunny",    "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak",   "Label": "Play"},
    {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High",   "Wind": "Weak",   "Label": "Play"},
    {"Outlook": "Sunny",    "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Label": "Play"},
    {"Outlook": "Overcast", "Temperature": "Hot",  "Humidity": "High",   "Wind": "Strong", "Label": "Not Play"},
    {"Outlook": "Rainy",    "Temperature": "Mild", "Humidity": "High",   "Wind": "Strong", "Label": "Not Play"},
    {"Outlook": "Sunny",    "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Label": "Play"},
    {"Outlook": "Rainy",    "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Label": "Play"},
    {"Outlook": "Sunny",    "Temperature": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Label": "Not Play"},
    {"Outlook": "Rainy",    "Temperature": "Mild", "Humidity": "High",   "Wind": "Weak",   "Label": "Play"},
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Label": "Not Play"},
]

features = ["Outlook", "Temperature", "Humidity", "Wind"]
classes  = ["Play", "Not Play"]

total = len(dataset)

# Prior probabilities
class_count = defaultdict(int)
for row in dataset:
    class_count[row["Label"]] += 1

prior = {c: class_count[c] / total for c in classes}

# Likelihood: P(feature_value | class)
likelihood = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
for c in classes:
    class_rows = [r for r in dataset if r["Label"] == c]
    for feat in features:
        val_count = defaultdict(int)
        for row in class_rows:
            val_count[row[feat]] += 1
        for val, cnt in val_count.items():
            likelihood[c][feat][val] = cnt / class_count[c]

def predict(sample):
    scores = {}
    for c in classes:   
        prob = prior[c]
        for feat in features:
            prob *= likelihood[c][feat].get(sample[feat], 0)  # 0 if unseen value
        scores[c] = prob
    return max(scores, key=scores.get), scores

print(f"{'No':<4} {'Outlook':<10} {'Temp':<6} {'Humid':<7} {'Wind':<7} "
      f"{'P(Play)':<10} {'P(NotPlay)':<12} {'Predicted':<10} {'Actual':<10} {'Result'}")
print("-" * 95)

correct = 0
for i, row in enumerate(dataset, 1):
    sample = {f: row[f] for f in features}
    pred, scores = predict(sample)
    actual = row["Label"]
    result = "Correct" if pred == actual else "Incorrect"
    if pred == actual:
        correct += 1

    print(f"{i:<4} {row['Outlook']:<10} {row['Temperature']:<6} {row['Humidity']:<7} "
          f"{row['Wind']:<7} {scores['Play']:<10.4f} {scores['Not Play']:<12.4f} "
          f"{pred:<10} {actual:<10} {result}")

accuracy = correct / total * 100
print(f"\nAccuracy: {correct}/{total} = {accuracy:.0f}%")

print("\n── Predict new sample ──")
new_sample = {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "High", "Wind": "Strong"}
pred, scores = predict(new_sample)
print(f"Input  : {new_sample}")
print(f"P(Play)     = {scores['Play']:.6f}")
print(f"P(Not Play) = {scores['Not Play']:.6f}")
print(f"Prediction  : {pred}")
