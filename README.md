# 🏠 House Price Prediction — Streamlit

A simple, production-ready Streamlit app that predicts **house sale prices** from three inputs:

- **GrLivArea** — Living area in square feet  
- **BedroomAbvGr** — Bedrooms above ground  
- **FullBath** — Full bathrooms  

Built with a scikit‑learn **Pipeline** (StandardScaler ➜ LinearRegression) and deployed via **Streamlit**.

---

## ✨ What’s inside

- `deploy.py` — Streamlit app (rename to `app.py` is recommended)
- `house_price_prediction.py` — training script
- `house_price_model.pkl` — trained model artifact (StandardScaler + LinearRegression)
- `house_price.csv` — dataset (optional to include; consider Git LFS)
- `requirements.txt` — Python dependencies
- `.gitignore` — sensible defaults
- `.gitattributes` — optional Git LFS rules
- `LICENSE` — MIT

> **Note:** The model uses **only three features** (`GrLivArea`, `BedroomAbvGr`, `FullBath`). **Location is not used** in this version.

---

## 🧠 How prediction works (minute detail)

1. **User inputs** values in the Streamlit UI.
2. The app loads the saved pipeline (`house_price_model.pkl`) with:
   - `StandardScaler` to normalize numeric inputs using the **same statistics** learned during training.
   - `LinearRegression` that learned coefficients \(a, b, c\) and an intercept \(d\).
3. The input row is scaled → the linear model computes  
   \[ \hat{y} = a\cdot\text{GrLivArea} + b\cdot\text{BedroomAbvGr} + c\cdot\text{FullBath} + d \]
4. The predicted sale price is formatted and shown in the app.

**Training details (`house_price_prediction.py`):**
- Reads `house_price.csv`
- Selects features `["GrLivArea","BedroomAbvGr","FullBath"]` and target `SalePrice`
- Train/test split (80/20) with `random_state=42`
- Pipeline: `StandardScaler` → `LinearRegression`
- Evaluates with **RMSE** and **R²**
- Saves the fitted pipeline with `joblib.dump(..., "house_price_model.pkl")`

---

## 🗂 Recommended repository structure

```
.
├── app.py                     # (rename from deploy.py) Streamlit app entry
├── training/
│   └── house_price_prediction.py
├── models/
│   └── house_price_model.pkl  # tracked or LFS if >50MB
├── data/
│   └── house_price.csv        # optional/private; prefer LFS or keep local
├── requirements.txt
├── .gitignore
├── .gitattributes             # enables Git LFS for large binaries
├── LICENSE
└── README.md
```

> If you keep your current names, update the docs accordingly (e.g., keep `deploy.py`).

---

## ⚙️ Local setup

1. **Clone** the repository (or create it and add files):
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv/Scripts/activate   # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   # If you renamed to app.py
   streamlit run app.py

   # Or, if you kept the original name
   streamlit run deploy.py
   ```

5. **Retrain (optional)**
   ```bash
   python training/house_price_prediction.py
   # This prints RMSE/R² and overwrites models/house_price_model.pkl
   ```

> **Version compatibility tip:** If you ever see errors loading the pickle (`sklearn` version mismatch), pin the versions in `requirements.txt` to the ones you trained with.

---

## ☁️ Deploy to Streamlit Community Cloud (free)

1. Push your repo to GitHub (see steps below).
2. Go to https://share.streamlit.io/ and sign in with GitHub.
3. **New app** → choose your repo, branch, and **app entry file** (`app.py` or `deploy.py`).
4. Make sure `requirements.txt` exists at the repo root.
5. Click **Deploy** — the app will build and then go live.

> You can update the app by pushing commits to the selected branch.

---

## 🚀 Push to GitHub — step by step

```bash
# inside your project folder
git init
git add .
git commit -m "Initial commit: Streamlit House Price Prediction"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

**Optional: enable Git LFS** if your `.pkl` or `.csv` is large (>50MB):
```bash
git lfs install
git lfs track "*.pkl" "*.joblib" "data/*.csv"
git add .gitattributes
git add models/house_price_model.pkl  # or wherever your model is
git commit -m "Track large binaries with Git LFS"
git push
```

---

## 🧪 Quick test checklist

- [ ] `streamlit run app.py` opens at `http://localhost:8501`
- [ ] Enter sample values → prediction appears without errors
- [ ] `python training/house_price_prediction.py` runs and saves model
- [ ] App uses the **updated** model after retraining
- [ ] Repo builds on Streamlit Cloud

---

## 🔧 Common pitfalls & fixes

- **ModuleNotFoundError**: Ensure `requirements.txt` includes `streamlit`, `pandas`, `numpy`, `scikit-learn`, `joblib`.
- **Pickle load error**: Pin `scikit-learn` to the training version.
- **Large file push rejected**: Use **Git LFS** for `.pkl`/`.csv` or keep them local.
- **Path issues**: If you move data/model into `data/` or `models/`, update paths in scripts.

---

## 📄 License

This project is licensed under the MIT License — see `LICENSE` for details.
