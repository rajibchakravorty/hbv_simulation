# Simulation of Mother-Child infection of HBV

## Set up (MAC)
The entire process, otherwise mentioned, is run on terminal.

### Installing pip, virtualenv

```bash
$ sudo easy_install pip
$ pip install virtualenv
```

### Creating Virtual Environment

Move to some folder of your choice, e.g /Users/your_user_name/favourite_folder.
We will call this FAV_FOLDER from now on

```bash
FAV_FOLDER $ virtualenv venv
```

### Activating the virtual environment

```bash
FAV_FOLDER $ source venv/bin/activate
(venv) FAV_FOLDER $
```
Note that if properly activated, you will see (venv) at the terminal.

From now on, untill deactivated, everything will be done when (venv)
is present.

## Download and run the code

### Download the code
Download the zip from [here](https://github.com/rajibchakravorty/hbv_simulation).
Click on the GREEN "clone or download" button. Unzip it within FAV_FOLDER.
We will call it CODE folder from now on.

## Changing the parameters
Look at ```constants.py``` and ```states.py```; You should be able to find majority
parameters here. You can open.edit the .py files in any text editor. For full Python
function, you can download the community version of PyCharm [here] (https://www.jetbrains.com/pycharm/download/#section=mac).

## Running the simulation.
```bash
(venv) CODE $ python simulations.py
```

If run properly, when finished, this will create two files 'mother_stats.pkl' and
'children_stats.pkl'. You can find these names in ```simulations.py``` and if required
can also change these names.

## Visualizing the result

### Run the jupyter notebook

```bash
(venv) CODE $ juptyer notebook
```
This will open the default browser (e.g. safari/firfox) and will show the content
of the folder. Click on ```views.ipynb``` to open it in a new window/tab and then
move to the new window. You will see visualization code.

From the top menu choose ```kernel->Restart and Run All```. This would reproduce
all the graphs.

### Editing visualization
In the second block check if the file names are correct. This uses the default name
and if those are changed, this block should be updated.

### What status to visualize
Each of the blocks 4-8 are same. You can change the list to view the graph for that
health state only.

For example, to only view the plot of mothers who have 'INFECTED' status in each year,
simply change the following

```python
mother_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED]
```

to

```python
mother_status = [INFECTED]
```
