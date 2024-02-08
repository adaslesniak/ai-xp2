# artivical intelignece-experiment 2

The first goal of this experiment is to play with PCA and get my hands dirty with some code. Do all the bugs, fix them, be angry at unknown syntax to get used to it, etc.

But I'm also interested in following qustion: what PCA does with non linear relations, does it catches them? Does it yeilds any result. Idea is to check if I can combine results of PCA with original data and run PCA second time on this combined set, what will happen then. If PCA would full capture variability of the data results of the second PCA run on combined data should be no different than first run as all relations are described... 
If my intuition is right then running PCA on PCA+original features could be simple verification of PCA quality, is it right tool for the job, or do we need to mess with features.
But I'm even more curious if running PCA multiple times can get us automatically closer to the true shape of data without guessing how to mess with original data.

Therefore there will be two scenarios on one data set:
data set will contain two independent features: mass and speed, while there will be two labels: energy and momentum.

Momentum is to check how PCA will work with perfectly linear data.
Energy is to check how PCA runned iteratively will deal with exponential data.
