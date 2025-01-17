# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

fake_news = pd.read_csv("./fake.csv")
print(fake_news.head(10).iloc[2:2,4:8])
print(fake_news.head(10)[['title', 'text']])

# Any results you write to the current directory are saved as output.