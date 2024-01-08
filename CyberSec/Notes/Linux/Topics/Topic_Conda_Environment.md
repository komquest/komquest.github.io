# Use Minda Conda With Sudo:

```
#Get environment when used with normal user:
which python

#now run with sudo
sudo -E /home/white/miniconda3/envs/impacket/bin/python odat.py all
 -s 10.10.10.82
```

# Install MiniConda:

https://docs.conda.io/en/latest/miniconda.html#linux-installers

Windows: start --> anaconda
Linux: Path already defined during install

```
conda create -n myenv python=3.6
conda activate myenv
conda install {Package}
conda evn list
```

Jupyter install and theme setup
-----

```
conda install -c conda-forge notebook
conda install -c conda-forge jupyterlab
conda install -c conda-forge jupyterthemes
jt -t oceans16
#Note, themes do not work for jupyter labs


"jupyter notebook" or "jupyter lab"




```

view Github Jupyter files:
https://nbviewer.jupyter.org/

install themes tutorial:
https://towardsdatascience.com/7-essential-tips-for-writing-with-jupyter-notebook-60972a1a8901
-----

# Conda environment Doc:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# Conda cheat sheet

https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf


# Create New Conda Environment:

conda create -n NAME python=3.7

# List Environments

conda info --envs

conda info -e

# Change to different environment 

conda activate Python3.9


# Miniconda, Good if you just want conda

https://docs.conda.io/en/latest/miniconda.html#linux-installers


# Article?:
https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e