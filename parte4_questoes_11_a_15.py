import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from dados import df

print("=== Questão 11 ===")
total = len(df)
com_erro = (df["erros"] > 0).sum()
p = com_erro / total
print("Total de requisições:", total)
print("Requisições com erro:", com_erro)
print("P(erro) =", f"{com_erro}/{total} = {p}")
print("Porcentagem:", f"{p*100:.0f}%")

print("\n=== Questão 12 ===")
print("P(sem erro) = 1 - P(A) =", round(1 - p, 2), f"({(1-p)*100:.0f}%)")

print("\n=== Questão 13 ===")
n = len(df)
android = (df["sistema"] == "Android").sum()
ios = (df["sistema"] == "iOS").sum()
print(f"a) P(Android) = {android}/{n} = {android/n}")
print(f"b) P(iOS) = {ios}/{n} = {ios/n}")
print(f"c) P(não Android) = 1 - {android/n} = {(n-android)}/{n} = {1 - android/n}")

print("\n=== Questão 14 ===")
rng = np.random.default_rng(42)
lancamentos = rng.integers(1, 7, size=10_000)
primos = np.isin(lancamentos, [2, 3, 5])
print("Probabilidade experimental (primo):", primos.mean())
print("Probabilidade teórica: 3/6 =", 3/6)
print("Diferença absoluta:", round(abs(primos.mean() - 0.5), 4))

print("\n=== Questão 15 ===")
t = df["tempo_ms"]
print("a) Estatística descritiva")
print("   Média:", t.mean(), "| Mediana:", t.median(),
      "| Amplitude:", t.max() - t.min(),
      "| Desvio padrão populacional:", round(t.std(ddof=0), 2),
      "| Desvio padrão amostral:", round(t.std(), 2))
freq = df["sistema"].value_counts()
print("b) Distribuição por sistema:\n", freq.to_string(),
      "\n", (df['sistema'].value_counts(normalize=True)*100).round(1).to_string())
print("c) P(erro) =", p)
print("   Coeficiente de variação:", round(t.std(ddof=0) / t.mean() * 100, 2), "%")

fig, axs = plt.subplots(1, 2, figsize=(11, 4))
freq.plot(kind="bar", ax=axs[0], color=["#3DDC84", "#555555", "#0078D4"], edgecolor="black")
axs[0].set_title("Distribuição dos sistemas operacionais")
axs[0].set_xlabel("Sistema"); axs[0].set_ylabel("Usuários")
axs[0].tick_params(axis="x", rotation=0)
axs[1].hist(t, bins=5, color="steelblue", edgecolor="black")
axs[1].axvline(t.mean(), color="red", linestyle="--", label=f"Média = {t.mean():.1f}")
axs[1].axvline(t.median(), color="green", linestyle=":", label=f"Mediana = {t.median():.1f}")
axs[1].set_title("Distribuição dos tempos de resposta")
axs[1].set_xlabel("tempo_ms"); axs[1].set_ylabel("Frequência"); axs[1].legend()
plt.tight_layout(); plt.savefig("q15_graficos.png", dpi=150); plt.close()
print("d) Gráficos salvos em q15_graficos.png")
