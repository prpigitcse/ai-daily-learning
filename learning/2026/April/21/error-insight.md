# Developer's Insight: Reading the Non-Linear Matrix

After transforming my dataset with polynomial and cyclical features, I standardized the new matrix and ran it through my Gradient Descent engine. The weights the model learned told a fascinating story about what it "sees" in the data:

`[Temp: -78.8, Occupants: 236.8, Hours: -79.4, Weekend: 0.0, Temp_Sq: -71.2, Active: 202.0, Sin_Day: 247.0, Cos_Day: 0.0]`

**1. The Cyclical Discovery**
The model assigned a massive weight of 247.0 to `Sin_Day`, but exactly 0.0 to `Cos_Day`. This is mathematically perfect. When I generated the synthetic data, I programmed the seasonal background load using *only* a sine wave. The linear engine perfectly reverse-engineered the exact mathematical wave hidden in the data.

**2. Dropping Redundant Features**
I intentionally excluded the raw `devices` column and the raw `day_of_year` integer column from the engineered matrix. If I had kept `day_of_year`, the model would have tried to assign a weight to it, effectively saying, "Energy follows a wave, BUT it also linearly drifts upward every single day." By dropping the raw integer representation, I forced the model to view time strictly as a seasonal loop, curing the Straight Line Fallacy.