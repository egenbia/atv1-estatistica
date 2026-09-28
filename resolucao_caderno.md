# ATV1 — Estatística Aplicada — Resolução para o caderno

## PARTE 1 — Conceitos

### Questão 1
a) **População:** os 10.000 usuários cadastrados.
b) **Amostra:** os 500 usuários sorteados para a pesquisa.
c) **Unidade estatística:** cada usuário (um único indivíduo cadastrado).

**Diferença:** população é o conjunto completo de elementos que se quer estudar; amostra é um subconjunto dela, usado para tirar conclusões sobre o todo quando estudar todos é caro ou inviável.

### Questão 2
a) **Aleatória simples:** numerar os 10.000 usuários (1 a 10.000) e sortear 500 números sem repetição (por exemplo, com gerador de números aleatórios). Todo usuário tem a mesma chance (500/10.000 = 5%) de ser escolhido.

b) **Estratificada:** dividir a população em estratos (Android, iOS, outros) e sortear aleatoriamente dentro de cada um, na mesma proporção que ele tem na população. Exemplo: se 60% são Android, sortear 300 Android; se 30% são iOS, 150 iOS; se 10% são outros, 50.

**Vantagem:** garante que todos os sistemas estejam representados na proporção correta, evitando que um grupo pequeno (outros) fique sub-representado ou ausente por azar no sorteio. A amostra fica mais representativa e com menos variabilidade.

### Questão 3
É um **viés de seleção**: só entrevistando quem já deu 5 estrelas, a amostra contém apenas usuários satisfeitos. Quem deu notas baixas ou médias não tem chance de ser escolhido, então a amostra não representa a população. O resultado tenderia a "provar" que todos estão satisfeitos, superestimando a satisfação real. Correção: amostragem aleatória de todos os usuários, independentemente da nota.

---

## PARTE 2 — Python
Ver arquivo `parte2_questoes_4_a_7.py` (e gráfico `q6_usuarios_por_sistema.png`).

**Q5:** Android = 6 (60%), iOS = 3 (30%), Windows = 1 (10%).
**Q6:** O sistema com maior frequência é o **Android** (6 usuários).
**Q7:** média = 129,8 | mediana = 129 | moda = amodal (nenhum valor se repete) | mín = 110 | máx = 150 | amplitude = 150 − 110 = 40.

Média e mediana são **muito próximas** (diferença de 0,8 ms). Isso indica distribuição aproximadamente **simétrica**, sem valores extremos que puxem a média, ou seja, o tempo de resposta é estável e a média é uma boa medida do valor típico.

---

## PARTE 3 — Dispersão (contas à mão)

### Questão 8
Média: (120+130+115+140+125+150+135+110+128+145)/10 = 1298/10 = **129,8**

| x | x − 129,8 | (x − 129,8)² |
|---|---|---|
| 120 | −9,8 | 96,04 |
| 130 | 0,2 | 0,04 |
| 115 | −14,8 | 219,04 |
| 140 | 10,2 | 104,04 |
| 125 | −4,8 | 23,04 |
| 150 | 20,2 | 408,04 |
| 135 | 5,2 | 27,04 |
| 110 | −19,8 | 392,04 |
| 128 | −1,8 | 3,24 |
| 145 | 15,2 | 231,04 |
| **Soma** | | **1503,6** |

a) Variância populacional: σ² = 1503,6 / 10 = **150,36 ms²**
b) Desvio padrão populacional: σ = √150,36 ≈ **12,26 ms**

**Significado:** em média, os tempos se afastam cerca de 12,26 ms da média (129,8 ms). Como isso é ~9,4% da média (baixa variação), o sistema responde de forma consistente.

### Questão 9
Dados: 120, 130, 115, 140, 125, 150, 135, 110, 128, 500

- **Média:** soma = 1653 → 1653/10 = **165,3**
- **Mediana:** ordenados: 110, 115, 120, 125, **128, 130**, 135, 140, 150, 500 → (128+130)/2 = **129**
- **Amplitude:** 500 − 110 = **390**
- **Desvio padrão:** quadrados dos desvios (em relação a 165,3):

| x | x − 165,3 | (x − 165,3)² |
|---|---|---|
| 120 | −45,3 | 2052,09 |
| 130 | −35,3 | 1246,09 |
| 115 | −50,3 | 2530,09 |
| 140 | −25,3 | 640,09 |
| 125 | −40,3 | 1624,09 |
| 150 | −15,3 | 234,09 |
| 135 | −30,3 | 918,09 |
| 110 | −55,3 | 3058,09 |
| 128 | −37,3 | 1391,29 |
| 500 | 334,7 | 112024,09 |
| **Soma** | | **125718,10** |

σ² = 125718,10 / 10 = 12571,81 → σ = √12571,81 ≈ **112,12 ms**

**Comparação:**

| Medida | Sem outlier | Com outlier |
|---|---|---|
| Média | 129,8 | 165,3 |
| Mediana | 129 | 129 |
| Amplitude | 40 | 390 |
| Desvio padrão | 12,26 | 112,12 |

### Questão 10
O valor 500 está muito distante dos demais. A **média** usa todos os valores na soma, então um valor extremo a puxa para cima (129,8 → 165,3). **Amplitude** depende só do máximo e do mínimo, e o **desvio padrão** eleva os desvios ao quadrado, o que amplifica o efeito do valor distante (12,26 → 112,12). A **mediana** depende apenas da posição central, por isso não mudou (129).

**Melhor medida do comportamento típico: a mediana.** Com o outlier, a média (165,3) é maior que 9 dos 10 tempos, e não representa nenhum tempo real observado; a mediana (129) continua refletindo o que a maioria das requisições vive.

---

## PARTE 4 — Probabilidade

### Questão 11
- Total de requisições: 10
- Com erro (erros > 0): usuários 2, 4, 6, 7, 9, 10 → **6**
- P(A) = 6/10 = **0,6**
- Porcentagem: **60%**

### Questão 12
P(Aᶜ) = 1 − P(A) = 1 − 0,6 = **0,4 (40%)** (confere: 4 requisições sem erro em 10).

### Questão 13
Android = 6, iOS = 3, Windows = 1 (total 10).
a) P(Android) = 6/10 = **0,6**
b) P(iOS) = 3/10 = **0,3**
c) P(não Android) = 1 − 0,6 = 4/10 = **0,4**

### Questão 14
Primos em um dado: 2, 3, 5 → P teórica = 3/6 = **0,5**.
Simulação (10.000 lançamentos, `parte4_questoes_11_a_15.py`): P experimental = **0,5023** (varia conforme a semente).

**Por que diferem:** a simulação envolve aleatoriedade, então a frequência relativa de uma amostra finita oscila em torno do valor teórico. Pela Lei dos Grandes Números, quanto mais lançamentos, mais o valor experimental se aproxima do teórico.

### Questão 15 — Relatório
**Estatística descritiva:** média = 129,8 ms; mediana = 129 ms; amplitude = 40 ms; desvio padrão populacional = 12,26 ms (coeficiente de variação ≈ 9,4%).
**Frequência:** Android 60%, iOS 30%, Windows 10%.
**Probabilidade de erro:** P(erro) = 0,6 (60%).
**Gráficos:** `q15_graficos.png`.

**Interpretação:** Em relação ao **tempo de resposta**, o sistema é estável: média e mediana quase coincidem (129,8 e 129), a amplitude é pequena (40 ms) e o desvio padrão de 12,26 ms é baixo frente à média, e não há valores extremos. Em relação aos **erros**, porém, o comportamento é preocupante: 60% das requisições apresentaram ao menos um erro, o que é muito alto. Assim, o sistema é consistente em desempenho, mas tem problema de confiabilidade. A base é predominantemente Android (60%), então convém investigar se os erros se concentram em algum sistema. Ressalva: são apenas 10 registros, então as conclusões são indicativas e devem ser confirmadas com uma amostra maior e representativa.
