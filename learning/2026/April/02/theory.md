# AI/ML Concept: The Loss Function

In machine learning, the formula we use to measure error is called the **Loss Function** (or Cost Function). 

An AI model does not have a brain. It does not understand what a house is, nor does it inherently know if a $300,000$ prediction makes sense. The *only* way an AI knows if it is doing a good job is by looking at the output of the Loss Function. 

The entire goal of training a machine learning model is to adjust the weights and biases (which we built in [Functions and Lines: Adding the Bias](/2026/february/25/functions-and-lines-adding-the-bias)) so that the Loss Function returns a number as close to zero as possible. 

Mean Squared Error (MSE) is the default loss function for regression tasks (predicting continuous numbers like prices, temperatures, or ages). Today, we give our engine the ability to realize when it has made a mistake.