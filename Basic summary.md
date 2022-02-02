BI-VARIAT CORRELATION
Descriptive analysis for data science 

Correlations are useful to identify a pattern that provides a sense of prediction or probability decision-makers can rely on for going forward. Whatever the case, correlations are used regularly in business to make processes perform better.

ANALYASIS

What is Correlation?

The statistical relationship between two variables is referred to as their correlation. Variables within a dataset can be related for different number of reasons.

For example:

•	One variable could cause or depend on the values of another variable.

•	One variable could be lightly associated with another variable.

•	Two variables could depend on a third unknown variable.

It is very useful in data analysis and modeling to better understand the relationships between variables. The statistical relationship between two variables is referred to as their correlation.
A correlation could be positive, meaning both variables move in the same direction, or negative, meaning that when one variable’s value increases, the other variables’ values decrease. Correlation can also be neural or zero, meaning that the variables are unrelated.

•	Positive Correlation: both variables change in the same direction.

•	Neutral Correlation: No relationship in the change of the variables.

•	Negative Correlation: variables change in opposite directions.


This project is built on the basis of widely used process in machine learning and data science.

Pearson’s Correlation
The Pearson correlation coefficient (named for Karl Pearson) can be used to summarize the strength of the linear relationship between two data samples.
The Pearson’s correlation coefficient is calculated as the covariance of the two variables divided by the product of the standard deviation of each data sample. It is the normalization of the covariance between the two variables to give an interpretable score.
 

The coefficient returns a value between -1 and 1 that represents the limits of correlation from a full negative correlation to a full positive correlation. A value of 0 means no correlation. The value must be interpreted, where often a value below -0.5 or above 0.5 indicates a notable correlation, and values below those values suggests a less notable correlation.The pearsonr() SciPy function can be used to calculate the Pearson’s correlation coefficient between two data samples with the same length.
Covariance
Variables can be related by a linear relationship. This is a relationship that is consistently additive across the two data samples and can be summarized between two variables, called the covariance. It is calculated as the average of the product between the values from each sample, where the values haven been centered (had their mean subtracted).


	

