# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_utils.ipynb.

# %% auto 0
__all__ = ['FloatInt', 'create_folds']

# %% ../nbs/05_utils.ipynb 3
import pandas as pd
from fastcore.utils import Path
from sklearn.model_selection import StratifiedKFold

# %% ../nbs/05_utils.ipynb 7
def create_folds(workdir: Path = "input", n_splits: int = 5):
    """
    To separate the dataframe into stratified folds.
    """
    if isinstance(workdir, str): workdir=Path(workdir)
    df = pd.read_csv(workdir / "train.csv")
    X_names = df.columns[:-1].to_list()
    y_name = df.columns[-1]
    df["fold"] = -1
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True)
    for fold, (train_idx, val_idx) in enumerate(cv.split(df[X_names], df[y_name])):
        df["fold"].iloc[[val_idx]] = fold
    return df


# %% ../nbs/05_utils.ipynb 18
from PIL import Image
import numpy as np
from numpy.typing import NDArray
from typing import Iterable, Union, Tuple

# %% ../nbs/05_utils.ipynb 19
FloatInt = Union[float, int]
