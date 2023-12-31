# -*- coding: utf-8 -*-
"""PRO-C138

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xDbcJOjelNe8RKx6MFCz4I_2aLg2k_hg
"""

!pip install kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d gspmoreira/articles-sharing-reading-from-cit-deskdrop

!ls

!unzip articles-sharing-reading-from-cit-deskdrop.zip

!ls

import pandas as pd
df1 = pd.read_csv('shared_articles.csv')
df2 = pd.read_csv('users_interactions.csv')

df1.head()

df2.head()

