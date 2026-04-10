# AI/ML Concept: Multicollinearity

Why is linear dependence a problem for Artificial Intelligence? In data science, this concept is called **Multicollinearity**, and it destroys models.

Imagine you are predicting house prices. Your dataset ($X$) has two features (columns): "Square Footage" and "Square Meters". These two columns measure the exact same thing, just scaled differently. They are linearly dependent. 

When your model tries to learn the weight ($w$) for these features, it gets hopelessly confused.
* Scenario A: It assigns a weight of $\$100$ to SqFt and $\$0$ to SqMeters. 
* Scenario B: It assigns $\$0$ to SqFt and the equivalent value to SqMeters.
* Scenario C: It assigns $\$50,000$ to SqFt and $-\$49,900$ to SqMeters.

Because the data overlaps perfectly, there are infinite mathematical ways to balance those two weights to get the same prediction. As a result, your training loop becomes wildly unstable, and the weights will often explode into massive positive and negative numbers. To fix this, data scientists must hunt down and delete redundant columns before training.