# 🤖 AI/ML Concept (20 Mins): Feature Representation

Computers do not natively understand real-world concepts like a "house," an "image," or a "song." To feed data into a Machine Learning model, we must translate these entities into vectors. This critical first step is called **feature representation**.

* 🏠 **Tabular Data:** If we are building a model to predict house prices, we might define a house using three features: number of bedrooms, number of bathrooms, and age in years. A 3-bedroom, 2-bathroom house built 15 years ago becomes a data point in 3D space: $\vec{h} = [3, 2, 15]$. 
* 🖼️ **Image Data:** A grayscale image is represented as a vector where each element corresponds to the brightness of a single pixel.
* 📝 **Text Data:** Words are mapped to high-dimensional vectors (often 300+ dimensions) where the numbers represent semantic meaning.

Every object an AI ever interacts with is converted into this numerical format so the underlying mathematical engine can process it.