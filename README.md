# Wine Quality Classification 🍷

Projeto desenvolvido como parte da pós-graduação em Data Analytics, com o objetivo de explorar características físico-químicas dos vinhos e investigar sua relação com a classificação de qualidade por meio de técnicas de análise de dados e Machine Learning.

## 🎯 Objetivo

Investigar quais características físico-químicas apresentam maior associação com a qualidade dos vinhos e avaliar a capacidade de modelos de aprendizado de máquina em identificar amostras classificadas como de média/baixa e alta qualidade.

**Pergunta central:**

> O que diferencia os vinhos de alta qualidade?

## 📊 Base de dados

O projeto utiliza o Wine Quality Dataset, composto por informações físico-químicas de amostras de vinhos e suas respectivas avaliações de qualidade.

Após a preparação dos dados, foram consideradas:

- **1143 amostras**
- **11 variáveis preditoras**
- Nenhum valor ausente identificado.
- Nenhum registro duplicado identificado.

A variável original `quality` foi transformada em uma classificação binária, denominada `quality_classification`:

| Classificação | Código | Critério |
|---|---:|---|
| Média/Baixa qualidade | 0 | Nota inferior a 7 |
| Alta qualidade | 1 | Nota igual ou superior a 7 |

A coluna `Id` foi mantida como identificador das amostras, mas não foi utilizada como variável preditora.

## 🔎 Etapas do projeto

O desenvolvimento foi organizado nas seguintes etapas:

1. **Preparação dos dados:** inspeção inicial, verificação de valores ausentes e duplicados e preparação da variável-alvo.
2. **Análise exploratória (EDA):** investigação da distribuição das classes, análise das características físico-químicas e identificação de possíveis associações com a qualidade.
3. **Modelagem:** treinamento e avaliação de diferentes algoritmos de classificação.
4. **Balanceamento das classes:** aplicação de oversampling para avaliar seu impacto nos resultados.
5. **Avaliação dos modelos:** comparação de métricas e análise das matrizes de confusão.
6. **Interpretação dos resultados:** identificação dos principais indicadores e de possíveis oportunidades para o negócio.

## 🤖 Modelos de Machine Learning

Foram avaliados quatro algoritmos de classificação:

- Logistic Regression
- Support Vector Classifier (SVC)
- Random Forest
- K-Nearest Neighbors (KNN)

Os modelos foram avaliados em dois cenários:

- Sem aplicação de oversampling.
- Com aplicação de oversampling para balanceamento das classes.

### Resultados

O Random Forest apresentou o melhor desempenho geral entre os modelos avaliados.

**F1-Score Macro:**

| Modelo | Sem Oversampling | Com Oversampling |
|---|---:|---:|
| Logistic Regression | 0.68 | 0.69 |
| SVC | 0.70 | 0.70 |
| Random Forest | 0.78 | 0.80 |
| KNN | 0.70 | 0.70 |

Apesar da melhora no resultado geral do Random Forest após o balanceamento, a análise da matriz de confusão demonstrou que essa estratégia não aumentou a identificação correta dos vinhos de alta qualidade.

Sem oversampling, o modelo identificou corretamente 21 das 32 amostras de alta qualidade. Com oversampling, esse número passou para 19.

Esse resultado evidencia a importância de avaliar o desempenho por classe, especialmente em bases de dados desbalanceadas.

## 📈 Principais descobertas

A análise exploratória e os resultados dos modelos permitiram identificar alguns pontos de destaque:

- **Distribuição das classes:** 86.09% das amostras foram classificadas como de média/baixa qualidade e 13.91% como de alta qualidade.
- **Teor alcoólico:** apresentou a maior associação positiva com a classificação de qualidade, com correlação de +0.40.
- **Acidez volátil:** apresentou a maior associação negativa, com correlação de -0.30.
- **Outras características relevantes:** ácido cítrico e sulfatos também apresentaram associações positivas com a qualidade.
- **Importância das variáveis:** teor alcoólico, sulfatos, ácido cítrico e acidez volátil estiveram entre as características de maior relevância para o modelo Random Forest.

Esses resultados indicam que determinadas características físico-químicas oferecem informações importantes para compreender as diferenças entre as amostras analisadas.

## 💡 Oportunidades para o negócio

Os resultados apontam oportunidades para utilizar a análise de dados como ferramenta complementar no acompanhamento da qualidade dos vinhos.

Entre as possibilidades estão:

- Acompanhar características físico-químicas que apresentaram maior relevância nas análises.
- Apoiar a identificação de padrões entre diferentes amostras.
- Complementar os processos de monitoramento e avaliação da qualidade.
- Utilizar modelos preditivos como apoio à análise e à tomada de decisão.

A proposta não é estabelecer uma fórmula única para definir a qualidade de um vinho, mas utilizar os dados para ampliar a compreensão sobre suas características e particularidades.

## ⚠️ Limitações

Os resultados devem ser interpretados considerando algumas limitações:

- A base representa um conjunto específico de amostras e não necessariamente reflete todo o mercado.
- A distribuição das classes observada no dataset não deve ser interpretada como representativa da distribuição de qualidade dos vinhos no mercado.
- Correlações e importâncias das variáveis não estabelecem relações de causa e efeito.
- A identificação de vinhos de alta qualidade apresentou limitações, mesmo no modelo com melhor desempenho geral.
- A avaliação físico-química não substitui a análise sensorial e a experiência dos especialistas.

## 📁 Estrutura do repositório

```text
wine-quality-classification/
│
├── data/                        # Base de dados utilizada       
├── notebooks/                   # Notebook com a análise e modelagem
├── src/                         # Scripts auxiliares
├── results/                     # Gráficos e relatórios
│   └── apresentacao_executiva
│   └── graficos
├── README.md                    # Descrição do projeto
└── requirements.txt             # Bibliotecas utilizadas
```

## ⚙️ Tecnologias e bibliotecas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## 🚀 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/kamiikg/wine-quality-classification.git
```

2. Acesse a pasta do projeto:

```bash
cd wine-quality-classification
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

5. Abra o notebook localizado em `notebooks/analise_win_quality_classification.ipynb`.

## 📝 Conclusão

O estudo permitiu identificar características físico-químicas que apresentam maior associação com a qualidade dos vinhos e avaliar a aplicação de diferentes modelos de Machine Learning nessa classificação.

Os resultados demonstram que a ciência de dados pode ampliar as possibilidades de análise e acompanhamento da qualidade, especialmente quando integrada à experiência dos especialistas.

**Mais do que buscar respostas definitivas, o objetivo é transformar dados em informações que apoiem decisões e contribuam para valorizar as particularidades de cada vinho.**

---

*Projeto acadêmico desenvolvido como parte da pós-graduação em Data Analytics.*