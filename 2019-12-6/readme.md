# CosmoLab meeting: 12/06/19

Attending: Vera Gluscevic, Tim Morton, Siavash Yasini, Aryan Rahimieh, Remy Gerras, Sydney Feldman, Javier Zhao, Chris Lindsay, David Liu, Jack Lashner, Connor Powers, Isabella Johansson, Yeojin Choi. 


## Classy and Bayesian inference in practice
This was a hands-on meeting. We did a quick recap on what was done so far in hacks. We then introduced python wrapper for CLASS code, called classy. We used classy to output Pk for a cosmology corresponding to the Chabanier et al paper (the source of our Pk measurements from Ly-alpaha). We then overplotted Pk calculated from classy over our data points. Match! 

Note on Pk normalization: classy and the data points use different factors of h (Hubble parameter) when dealing with Pk; if you want the data to match the calculation, make sure you reconcile the normalizations.


Suggested exercises: 
- Plot Cl/Pk using classy


 