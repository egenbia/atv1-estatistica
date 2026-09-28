import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from dados import df

print("=== Questão 4 ===")
print("a) Cinco primeiras linhas:\n", df.head())
print("\nb) Linhas e colunas:", df.shape, f"-> {df.shape[0]} linhas e {df.shape[1]} colunas")
print("\nc) Informações gerais:")
df.info()
print("\nd) Estatísticas descritivas:\n", df.describe())

print("\n=== Questão 5 ===")
freq = df["sistema"].value_counts()
perc = df["sistema"].value_counts(normalize=True) * 100
print("a) Quantidade por sistema:\n", freq)
print("\nb) Percentual por sistema (%):\n", perc.round(1))

print("\n=== Questão 6 ===")
ax = freq.plot(kind="bar", color=["#3DDC84", "#555555", "#0078D4"], edgecolor="black")
plt.title("Quantidade de usuários por sistema operacional")
plt.xlabel("Sistema operacional"); plt.ylabel("Nº de usuários")
plt.xticks(rotation=0)
for i, v in enumerate(freq):
    plt.text(i, v + 0.1, str(v), ha="center")
plt.tight_layout(); plt.savefig("q6_usuarios_por_sistema.png", dpi=150); plt.close()
print("Gráfico salvo: q6_usuarios_por_sistema.png")
print("Sistema com maior frequência:", freq.idxmax(), f"({freq.max()} usuários)")

print("\n=== Questão 7 ===")
t = df["tempo_ms"]
print("Média   :", t.mean())
print("Mediana :", t.median())
print("Moda    :", t.mode().tolist(), "(todos os valores aparecem 1 vez -> amodal)")
print("Mínimo  :", t.min())
print("Máximo  :", t.max())
print("Amplitude:", t.max() - t.min())
print("Diferença média-mediana:", round(t.mean() - t.median(), 2))
