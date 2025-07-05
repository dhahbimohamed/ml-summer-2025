# 🎯 Understanding Bias and Variance in Machine Learning

This note explains the concepts of **bias** and **variance**, which are essential to understanding how well a machine learning model can generalize to new, unseen data.

---

## 📌 What is Bias?

Bias refers to a model’s **inability to capture the true relationship** between the features (input) and the target (output).

- A high-bias model makes **strong assumptions** about the data.
- It often **underfits**, meaning it performs poorly on both the training and testing sets.
- Example: Using a linear regression model to fit a highly nonlinear pattern.

> "Bias is the price you pay for simplicity."

---

## 📌 What is Variance?

Variance is the amount by which a model’s predictions would **change if it were trained on a different dataset**.

- High variance means the model is **too sensitive** to the training data.
- It performs well on training data but **poorly on testing data**.
- This is known as **overfitting** — the model has learned the noise instead of the signal.

> "Variance is the price you pay for flexibility."

---

## ⚖️ The Bias-Variance Tradeoff

In practice, we want to find a balance:

| Bias  | Variance | Outcome         |
|-------|----------|------------------|
| High  | Low      | Underfitting     |
| Low   | High     | Overfitting      |
| Low   | Low      | ✅ Good Generalization |

---

## 🛠 Detecting Bias and Variance

- **High training error, high testing error** → likely high bias (underfitting).
- **Low training error, high testing error** → likely high variance (overfitting).
- Use **cross-validation** to estimate how well your model generalizes.

---

## 🔄 Summary

- **Bias**: error from incorrect assumptions (model too simple).
- **Variance**: error from excessive sensitivity to training data (model too complex).
- **Goal**: Minimize both, and find a model that balances them to generalize well to new data.

> A good model is not the one that performs perfectly on training data, but the one that performs reliably on unseen data.
