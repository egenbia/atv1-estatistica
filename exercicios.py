import matplotlib.pyplot as plt
from dados import df
import numpy as np

print(" Questão 4 ")
print("a) Cinco primeiras linhas:\n", df.head())
print("\nb) Linhas e colunas:", df.shape, f"-> {df.shape[0]} linhas e {df.shape[1]} colunas")
print("\nc) Informações gerais:")
df.info()
print("\nd) Estatísticas descritivas:\n", df.describe())

print("\nQuestão 5 ")
freq = df["sistema"].value_counts()
perc = df["sistema"].value_counts(normalize=True) * 100
print("a) Quantidade por sistema:\n", freq)
print("\nb) Percentual por sistema (%):\n", perc.round(1))

print("\nQuestão 6")
freq.plot(kind="bar")
plt.title("Quantidade de usuários por sistema operacional")
plt.xlabel("Sistema operacional")
plt.ylabel("Nº de usuários")
plt.show()
print("Sistema com maior frequência:", freq.idxmax())

print("\nQuestão 7 ")
t = df["tempo_ms"]
print("Média   :", t.mean())
print("Mediana :", t.median())
print("Moda    :", t.mode().tolist())
print("Mínimo  :", t.min())
print("Máximo  :", t.max())
print("Amplitude:", t.max() - t.min())
print("Diferença média-mediana:", round(t.mean() - t.median(), 2))


tempo_ms = [120, 130, 115, 140, 125, 150, 135, 110, 128, 145]
tempo_com_outlier = [120, 130, 115, 140, 125, 150, 135, 110, 128, 500]

print("\nQuestão 8")
print("Variância populacional:", np.var(tempo_ms))
print("Desvio padrão populacional:", np.std(tempo_ms))

print("\nQuestão 9")
print("Média:", np.mean(tempo_com_outlier))
print("Mediana:", np.median(tempo_com_outlier))
print("Amplitude:", max(tempo_com_outlier) - min(tempo_com_outlier))
print("Desvio padrão:", np.std(tempo_com_outlier))

print("\nQuestão 11 ")
total = len(df)
com_erro = (df["erros"] > 0).sum()
p = com_erro / total
print("Total de requisições:", total)
print("Requisições com erro:", com_erro)
print("P(erro) =", f"{com_erro}/{total} = {p}")
print("Porcentagem:", f"{p*100:.0f}%")

print("\nQuestão 12 ")
print("P(sem erro) = 1 - P(A) =", round(1 - p, 2), f"({(1-p)*100:.0f}%)")

print("\nQuestão 13 ")
n = len(df)
android = (df["sistema"] == "Android").sum()
ios = (df["sistema"] == "iOS").sum()
print(f"a) P(Android) = {android}/{n} = {android/n}")
print(f"b) P(iOS) = {ios}/{n} = {ios/n}")
print(f"c) P(não Android) = 1 - {android/n} = {(n-android)}/{n} = {1 - android/n}")

print("\nQuestão 14 ")
rng = np.random.default_rng(42)
lancamentos = rng.integers(1, 7, size=10000)
primos = np.isin(lancamentos, [2, 3, 5])
print("Probabilidade experimental (primo):", primos.mean())
print("Probabilidade teórica: 3/6 =", 3/6)
print("Diferença absoluta:", round(abs(primos.mean() - 0.5), 4))

print("\nQuestão 15")
t = df["tempo_ms"]

print("a) Estatística descritiva")
print("Média:", t.mean())
print("Mediana:", t.median())
print("Amplitude:", t.max() - t.min())
print("Desvio padrão:", t.std(ddof=0))

print("\nb) Frequência por sistema")
print(df["sistema"].value_counts())

print("\nc) Probabilidade de erro")
p = (df["erros"] > 0).sum() / len(df)
print("P(erro) =", p)

# d) Gráficos
df["sistema"].value_counts().plot(kind="bar")
plt.title("Distribuição dos sistemas operacionais")
plt.xlabel("Sistema")
plt.ylabel("Usuários")
plt.show()

plt.hist(t, bins=5)
plt.title("Distribuição dos tempos de resposta")
plt.xlabel("tempo_ms")
plt.ylabel("Frequência")
plt.show()

