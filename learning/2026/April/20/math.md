# Math: Expanding the Feature Space

To teach a linear model how to see curves, seasons, and interactions, we do not change the algorithm. We change the data. We physically add new columns to our $X$ matrix that contain non-linear math. 

**1. Polynomial Features (The Parabola)**
We know energy spikes when it is very hot *and* when it is very cold. A straight line can't model a U-shape, but a squared number can. We engineer a new column by squaring the temperature.
$$x_{\text{temp\_sq}} = (\text{Temp})^2$$

**2. Interaction Terms (The Multiplier)**
Energy doesn't just depend on `occupants` or `hours` in isolation. The true draw happens when *both* are high. We create a new column by multiplying them together.
$$x_{\text{active}} = \text{Occupants} \times \text{Hours}$$

**3. Cyclical Encoding (The Calendar Loop)**
How do we make Day 365 sit right next to Day 1? We map the 1D timeline onto a 2D circle using Trigonometry. 

We take the day of the year ($d$) and engineer two new columns:
$$x_{\text{sin}} = \sin\left(\frac{2\pi \cdot d}{365}\right)$$
$$x_{\text{cos}} = \cos\left(\frac{2\pi \cdot d}{365}\right)$$
By feeding the model both the sine and cosine, it can perfectly track its position on the calendar loop without ever assuming that December is "greater" than January.