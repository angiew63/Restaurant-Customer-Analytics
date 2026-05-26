import joblib
import os

os.makedirs("../models", exist_ok=True)

joblib.dump(rf_pipeline, "../models/random_forest_model.pkl")
joblib.dump(dt_pipeline, "../models/decision_tree_model.pkl")
joblib.dump(xgb_pipeline, "../models/xgboost_model.pkl")

print("Models saved successfully.")
