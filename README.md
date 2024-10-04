## STAT3602 Group Project Part 1

fuckfuckfuckfuckfuckfuckfuckfuck why does `np.power(10, 10)` return `1410065408`

### Requirements

Requirements are listed in `requirements.txt`, run to install them:
```sh
pip install -r requirements.txt 
```
Note `specific_requirements.txt` included the specific versions of the packages that are confirmed to work, so if you encountered any errors due to a wrong version of the packages, you can run the following to fix it:
```sh
pip install -r specific_requirements.txt 
```

### `src/utils/dataset.py`

Contains the definition of the `Dataset` class, just a wrapper around all the data provided in the lecture.

### `src/utils/evaluate.py`

Records the prior/posterior for each $t = 0, 1, \ldots, T$.

### `src/methods/`

Stores the python implementation of each method for testing, suggested to just implement the prior and posterior function, see `src/methods/lecture.py` for reference.

### `src/`

Stores the testing files (in `ipynb` notebook format), feel free to create subfolders for each method, see `src/lecture.ipynb` for reference.