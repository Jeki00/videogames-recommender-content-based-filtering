# %% [markdown]
# # Persiapan data

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# dataset berasal dari kaggle: https://www.kaggle.com/datasets/gregorut/videogamesales

# %%
df = pd.read_csv('videogamesales/vgsales.csv')
df

# %% [markdown]
# # Data undestanding

# %%
df.shape

# %%
print('Jumlah judul video games:', len(df['Name'].unique()))
print('Jumlah Genre:', len(df['Genre'].unique()))

# %% [markdown]
# # Exploratory Data Analysis

# %%
df.info()

# %%
df.describe()

# %%

ax = df['Platform'].value_counts().sort_index().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Jumlah Video Games tiap Platform")
ax.set_xlabel("Platform")
ax.set_ylabel("Jumlah")
plt.show()

# %%

ax = df['Year'].value_counts().sort_index().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Jumlah Video Games tiap tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah")
plt.show()

# %%
ax = df['Genre'].value_counts().sort_index().plot(kind='pie',
                                    figsize=(14,8),
                                    title="Perbandingan tiap genre Video Games", autopct='%.2f%%')
plt.show()

# %% [markdown]
# # Data Preprocessing

# %%
vidya = df[['Name','Genre']]
vidya

# %% [markdown]
# Mengubah kata 'Role-Playing' menjadi 'RolePlaying' agar ketika di dilakukan TFIDF menjadi satu kata

# %%
vidya['Genre'] = vidya['Genre'].apply(lambda x: x.replace('-',''))
vidya

# %%
vidya.info()

# %%
vidya.duplicated().sum()

# %%
vidya = vidya.drop_duplicates(subset=['Name'])
vidya.shape

# %% [markdown]
# # Model and Result

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data cuisine
tf.fit(vidya['Genre']) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out() 

# %%
# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(vidya['Genre']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape 

# %%
# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# %%
pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names_out(),
    index=vidya['Name']
)

# %%
from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

# %%
cosine_sim_df = pd.DataFrame(cosine_sim, index=vidya['Name'], columns=vidya['Name'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df

# %%
def get_recommendations(nama, similarity_data=cosine_sim_df, items=vidya[['Name', 'Genre']], k=7):

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

# %%
vidya[vidya['Name']== "NBA 2K14"]

# %%
get_recommendations("NBA 2K14",k=10)


