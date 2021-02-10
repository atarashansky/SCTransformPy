# SCTransformPy


This is a python port of the R package [SCTransform](https://github.com/ChristophH/sctransform).

Currently, I only use log UMI counts as a single latent variable (the default in the R package). I'm planning on allowing the user to define custom regression models as is done in the R implementation. 

Implementation notes:
- Poisson regression is done using the `statsmodels` package and parallelized with `multiprocessing`. 
- Improved Sheather & Jones bandwidth calculation is implemented by the `KDEpy` package.
- Estimating `theta` using MLE was translated from the `theta.ml` function in R.
- Pearson residuals are automatically clipped to be in the range `[0, sqrt(N/30)]` where `N` is the number of cells. This ensures that sparsity structure is preserved in the data. Practically, the results do not change much when allowing for dense, negative values.

#TODO 
- Provide comparison between the python and R implementations here to show that results are highly similar.
- Clean up code and prepare for integration with `scanpy`.
