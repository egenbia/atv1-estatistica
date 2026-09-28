import numpy as np
from dados import df

t = np.array(df["tempo_ms"])
print("=== Questão 8 (confirmação) ===")
print("Média:", t.mean())
print("Desvios (x - média):", np.round(t - t.mean(), 1))
print("Desvios ao quadrado:", np.round((t - t.mean())**2, 2))
print("Soma dos quadrados:", round(((t - t.mean())**2).sum(), 2))
print("a) Variância populacional:", round(np.var(t), 2))
print("b) Desvio padrão populacional:", round(np.std(t), 2))

print("\n=== Questão 9 (confirmação) ===")
c = np.array([120,130,115,140,125,150,135,110,128,500])
print("Média:", c.mean())
print("Mediana:", np.median(c))
print("Amplitude:", c.max() - c.min())
print("Variância populacional:", round(np.var(c), 2))
print("Desvio padrão populacional:", round(np.std(c), 2))

print("\nComparação (sem outlier -> com outlier):")
print(f"Média:   {t.mean():.1f} -> {c.mean():.1f}")
print(f"Mediana: {np.median(t):.1f} -> {np.median(c):.1f}")
print(f"Amplit.: {t.max()-t.min()} -> {c.max()-c.min()}")
print(f"Desvio:  {np.std(t):.2f} -> {np.std(c):.2f}")
