# usc-cosmolab-hackspace

MY FORK!!! HAHAHAHA

Materials from USC CosmoLab weekly meetings live here.

Meetings have roughly three parts: Hacks, News, and Physics. In Fall 2019, the focus is on Hacks, with the main objective to provide astro grads, undergrads, and postdocs with computer-based tools for research. 

Meeting policy: CosmoLab is a safe learning space for cosmologists at USC to ask questions and to collaboratively think about the big problems in physics. Competition and judgement should be left for other venues; curiosity, critical thinking, and collegiality are welcome.

## conda environment

To set up a basic conda environment with packages you need for this group, do the following:

```
conda create -n cosmolab jupyterlab numpy scipy matplotlib cython python=3.7
```
For interactive visualization tools, do the following:
```
conda activate cosmolab
conda install -c pyviz holoviz
jupyter labextension install @pyviz/jupyterlab_pyviz
```


