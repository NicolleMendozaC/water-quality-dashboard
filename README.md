# 💧 Dashboard de Calidad del Agua

Dashboard interactivo desarrollado con **Dash + Python** para analizar la calidad del agua usando Machine Learning.

---

## 📊 Pestañas del Dashboard

| Pestaña | Contenido |
|---|---|
| 📌 Contexto | Impacto y relevancia del análisis de calidad del agua |
| 🔬 Metodología | Descripción del dataset y modelo utilizado |
| 📊 EDA | Análisis exploratorio con gráficos interactivos |

---

## 🤖 Modelo de Machine Learning

- **Algoritmo:** Regresión Logística
- **Librería:** Scikit-learn
- **Pipeline:** StandardScaler + LogisticRegression
- **División:** 80% entrenamiento / 20% prueba

---

## 🛠️ Tecnologías Utilizadas

- Python 3.10+
- Dash + Dash Bootstrap Components
- Plotly
- Scikit-learn
- Pandas / NumPy

---

## 📁 Estructura del Proyecto

```
water_quality_dashboard/
│
├── app.py                  # Archivo principal del dashboard
├── requirements.txt        # Dependencias del proyecto
│
├── data/
│   └── generate_data.py    # Generación del dataset
│
├── model/
│   ├── train_model.py      # Entrenamiento del modelo
│   └── model.pkl           # Modelo guardado
│
└── tabs/
    ├── contextoproblema.py
    ├── metodologia.py
    └── eda.py
```

---

## 🚀 Cómo Ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/NicolleMendozaC/water-quality-dashboard.git
cd water-quality-dashboard

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Generar datos
python data/generate_data.py

# 4. Entrenar modelo
python model/train_model.py

# 5. Lanzar dashboard
python app.py
```

Luego abre tu navegador en: **http://localhost:8050**

---

## 📋 Variables del Dataset

| Variable | Tipo | Descripción |
|---|---|---|
| pH | Numérica | Nivel de acidez del agua |
| Turbidez | Numérica | Claridad del agua (NTU) |
| Oxígeno Disuelto | Numérica | Concentración de O₂ (mg/L) |
| Conductividad | Numérica | Capacidad de conducir electricidad (µS/cm) |
| Calidad | Binaria 🎯 | 1 = Apta para consumo, 0 = No apta |

---

## 👩‍💻 Autora

**Nicolle Mendoza** — [@NicolleMendozaC](https://github.com/NicolleMendozaC)

> Proyecto desarrollado para el curso de Python.
