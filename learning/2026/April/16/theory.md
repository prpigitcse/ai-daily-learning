# AI/ML Concept: The Exploding Gradient

Why do neural networks demand scaled data? It comes down to the geometry of the Loss Landscape.


If you have one feature scaled in the thousands (SqFt) and one feature scaled in the tens (Age), the gradients for SqFt will naturally be hundreds of times larger than the gradients for Age. 

Geometrically, this stretches the error bowl into a steep, narrow canyon. If your learning rate is small enough to safely step down the canyon length (Age), it will take millions of epochs. If your learning rate is large enough to learn quickly, it will violently bounce off the steep canyon walls (SqFt), amplifying the error until the numbers physically overflow the computer's memory.

By standardizing the data, we reshape that canyon into a perfectly symmetrical, circular bowl. The gradients for every feature point directly to the center, allowing the model to learn incredibly fast without exploding.