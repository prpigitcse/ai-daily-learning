# AI/ML Concept: Proving Your Representation

Mean Squared Error (MSE) is great for the Gradient Descent loop, but it is terrible for human evaluation. An MSE of 15,000 doesn't mean anything unless you know the scale of the dataset. $R^2$ normalizes the error into a scale-free ratio, acting much like a percentage score.

By implementing $R^2$, we can run an A/B test to prove why feature engineering is so powerful. 

When you train your model on the raw matrix, it will struggle to draw a straight line through parabolic temperatures and seasonal sine waves. Its RSS will be high, resulting in a low $R^2$ score. When you train on the engineered matrix, it will effortlessly bend to fit the data, dropping the RSS and skyrocketing the $R^2$ score. This metric scientifically proves that "Linear Regression is powerful if you give it the right representation."