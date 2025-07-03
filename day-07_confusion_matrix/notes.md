# 🧩 Confusion Matrix in Machine Learning

A **confusion matrix** is a fundamental tool for evaluating classification models. It shows how well a model's predicted labels match the actual labels — helping identify where the model is getting things right and where it's going wrong.

---

## 🧠 What is a Confusion Matrix?

A confusion matrix is a **square table** used to visualize the performance of a classification algorithm. It compares:

- **Actual values (ground truth)** vs. **Predicted values (model output)**

For a binary classification problem, the confusion matrix is a 2×2 table:

|                        | **Predicted Positive** | **Predicted Negative** |
|------------------------|------------------------|------------------------|
| **Actual Positive**    | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative**    | False Positive (FP)    | True Negative (TN)     |

- The **diagonal cells** (TP, TN) are correct predictions.
- The **off-diagonal cells** (FP, FN) are errors.

---

## 📊 Example: Binary Classification

```plaintext
Predicted ➡
           Positive   Negative
Actual ↓
Positive     45         5
Negative     3         47