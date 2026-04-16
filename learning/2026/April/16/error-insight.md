# Developer's Insight: The Zero Variance Trap

While writing the Z-score normalization function, I realized a hidden danger in the formula $z = \frac{x - \mu}{\sigma}$. 

What happens if every single house in the dataset has exactly 3 bedrooms? The mean of that column is 3. The difference between every house and the mean is 0. Therefore, the standard deviation ($\sigma$) becomes exactly 0. 

If I blindly loop through the math, Python will throw a `ZeroDivisionError` and crash the entire training pipeline. 

I implemented a defensive `if sigma == 0:` check to explicitly catch this. This isn't just a code bug; it represents a conceptual truth in machine learning. If a feature has zero variance (every data point is identical), it carries absolutely no predictive information. A neural network cannot learn a pattern from a signal that never changes.