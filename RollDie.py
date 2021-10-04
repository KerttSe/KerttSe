# coding: utf-8
import matplotlib.pyplot as plt
import numpy
import random
import seaborn as sns
import numpy as np
rolls = [random.randrange(1, 7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set-_style('whitegrid')
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
