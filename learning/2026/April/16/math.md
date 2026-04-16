# Math: Z-Score Standardization

To prevent our math from exploding, we need all of our features to live on the exact same scale, ideally centered around 0. We do this using a statistical technique called **Standardization** (or Z-score normalization).


Standardization converts every raw number into a Z-score, which simply represents "how many standard deviations is this number away from the average?"

To standardize a feature column, we execute three steps:
1. **Calculate the Mean ($\mu$):** The average value of the column.
   $$\mu = \frac{1}{N} \sum x_i$$
2. **Calculate the Standard Deviation ($\sigma$):** How spread out the data is from that average.
   $$\sigma = \sqrt{\frac{1}{N} \sum (x_i - \mu)^2}$$
3. **Apply the Z-Score Formula:** Subtract the mean from the raw number, and divide by the standard deviation.
   $$z = \frac{x - \mu}{\sigma}$$

If a house is exactly average size, its standardized SqFt becomes 0.0. If it is huge, it might be 1.5. If it is tiny, it might be -1.2. Suddenly, a massive 3000.0 SqFt feature and a small 20.0 Age feature are transformed into the exact same numerical range!