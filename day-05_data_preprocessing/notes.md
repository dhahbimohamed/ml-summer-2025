# Day 5 – Data Preprocessing

## ✅ Missing Values
- Empty cells in data are called NaN.
- We fix them using:
  - `.fillna()` with mean/median
  - Dropping the row using `.dropna()`
- Only fill numerical columns with mean.

## ✅ Scaling
- Features like Age and Salary have very different ranges.
- Models get confused if one number is huge and one is small.
- `StandardScaler` makes data have:
  - Mean = 0
  - Std = 1

## ✅ Train/Test Split
- We use 80% of data for training, 20% for testing.
- Done with `train_test_split()` from `sklearn.model_selection`

## 💡 My understanding: 8.5/10