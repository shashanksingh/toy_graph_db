# Toy GraphDB

Just a toy graph db so that we can play around with graph algorithms 

# Aim

Use Cases I want to test out with this
1. Use a DAG of currency conversion to find how we can make money by doing rapid currency conversion AKA
Given a grid of currency conversion , between few currencies find Eulerian circuit 
that has to get X% over money over what I started.  
2. Find degree of friendship
3. For Grid : load a image as grid and find components in it, aka edge detection

# DB performance

Writing
`------------------------------------------------------------------ benchmark: 1 tests -----------------------------------------------------------------
Name (time in us)                                          Min       Max     Mean   StdDev   Median     IQR  Outliers  OPS (Kops/s)  Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------
test_performance_of_saving_all_graphs_into_storage     46.5050  132.3730  49.8334  10.7824  47.3340  0.5845     21;39       20.0669     412           1
------------------`-------------------------------------------------------------------------------------------------------------------------------------