# 📊 Confronto Prestazionale tra MongoDB e Neo4j

[![Tecnologie](https://img.shields.io/badge/DBMS-MongoDB%20%7C%20Neo4j-brightgreen)]()
[![Status](https://img.shields.io/badge/stato-Analisi%20completata-blue)]()
[![Licenza](https://img.shields.io/badge/licenza-MIT-green.svg)](LICENSE)

Questo progetto analizza e confronta le prestazioni di **MongoDB** (document-oriented) e **Neo4j** (graph-oriented) su uno **stesso dataset**, focalizzandosi sulle performance in termini di tempo di esecuzione di differenti query con varia complessità e presenza di relazioni.

---

## 🧠 Obiettivo

Lo scopo dell’esperimento è valutare quale dei due DBMS NoSQL si comporti meglio **in base alla natura delle interrogazioni**:  
- **MongoDB** per operazioni dirette su dati non relazionati  
- **Neo4j** per query complesse che coinvolgono **più entità e relazioni**

---

## ⚙️ Tecnologie Utilizzate

- **MongoDB**: per la gestione documentale del dataset
- **Neo4j**: per la modellazione a grafo e interrogazioni relazionali
- **Python**: per l’automazione dei test
- **Librerie Python**:
  - `pymongo`
  - `neo4j`
  - `time` / `datetime`
  - `matplotlib` per visualizzazione grafici

---

## 📈 Metodologia di Test

Ogni query è stata eseguita su:
- **diverse percentuali di dataset** (25%, 50%, 75%, 100%)
- **in modo ripetuto** (1 esecuzione iniziale + 30 successive)  
- I **tempi di esecuzione** sono stati registrati per ogni scenario.

### Query testate:

1. 🔍 Query semplice su un singolo campo **senza relazioni**
2. 🔗 Query con **relazioni semplici** tra entità
3. 🧩 Query più articolate con **relazioni multiple**
4. 🧠 Query complessa su **più livelli gerarchici**

---

## 📊 Risultati

### 🟢 MongoDB

- Prestazioni **eccellenti nelle query senza relazioni**
- Tempi medi **inferiori a 7 ms** su query 1
- **Scalabilità orizzontale** ottima con dataset voluminosi
- Performance **costanti ma alte** in presenza di molte relazioni

### 🔵 Neo4j

- Tempi iniziali **più lenti** per query semplici (fino a 47 ms)
- Estrema efficienza nel **gestire relazioni complesse**
- Uso ottimale del **caching** e **algoritmi di traversing**
- Performance migliorate fino al **70%** nelle esecuzioni successive

---

## 🧪 Conclusioni

- **MongoDB** è la scelta migliore quando si tratta di operazioni di **lettura/scrittura su dati disconnessi**, specialmente in architetture distribuite.
- **Neo4j** si dimostra superiore in presenza di **query relazionali complesse**, grazie alla sua struttura a grafo e all’efficienza degli algoritmi di traversamento.
  
> 📌 Per il caso di studio analizzato, **Neo4j è risultato più efficiente** in scenari complessi con molteplici entità correlate, mentre **MongoDB ha eccelso in operazioni atomiche e indipendenti**.
