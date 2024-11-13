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

### Structure

#### `src/utils/dataset.py`

Contains the definition of the `Dataset` class, just a wrapper around all the data provided in the lecture.

#### `src/utils/evaluate.py`

Records the prior/posterior for each $t = 0, 1, \ldots, T$.

#### `src/methods/`

Stores the python implementation of each method for testing, suggested to just implement the prior and posterior function, see `src/methods/lecture.py` for reference.

#### `src/`

Stores the testing files (in `ipynb` notebook format), feel free to create subfolders for each method, see `src/lecture.ipynb` for reference.

### Methods

#### Accessible data

- $t = 0, \ldots, T$: time $t$
- $m_t \geq 0$: number of letters from congwen at time $t$
- $n_t \geq 0$: number of letters from other frogs at time $t$

#### Lecture

- $\theta_{Frogs} = \theta_1 \sim \mathrm{Po}(10)$: number of frogs
- $\theta_{Love} = \theta_2 \in \{-1, 0, \ldots, \theta_1\}$, $F(\theta_{Love}) = 0.5 \;\text{if}\; \theta_{Love} = -1 \;\text{else}\; \frac{0.5}{\theta_{Frogs+1}}$: true love (-1 means no true love, 0 means congwen, rest means frog number $\theta_{Love}$)
- $\theta_p = \theta_3 \sim \mathrm{U}(0,1)$: $\Pr(\text{reply}|\text{is true love})$
- Each Frogs have probability 0.1 to send letter, and they will only send one letter
- Congwen will send a letter in sats and suns

#### Idea 1: Varying $\theta_{Frogs}$

- $\theta_{Frogs}^{(0)} \sim \mathrm{Po}(\lambda)$: initial number of frogs
- $\theta_{Frogs}^{(t)} = \theta_{Frogs}^{(t-1)} + R^{(t)}$: number of frogs at time $t$, $R^{(t)} \sim F_{r}$ is a random variable, can be Geometric, Possion, etc, with parameter $r$
- $\theta_{Love} \sim \mathrm{Geo}(p)$ (Can change dist): true love, (0 means don't want love, 1 means congwen, rest means frog number $\theta_{Love}$), assume first send letter $=$ more attractive
- $\theta_p = \theta_3 \sim \mathrm{U}(0,1)$: $\Pr(\text{reply}|\text{is true love})$
- Each Frogs have probability $p_{send}$ to send letter, and they will only send one letter
- Congwen will send a letter in sats and suns