#!/usr/bin/env python
"""
Display Model Metrics Summary
"""

import pandas as pd
import numpy as np

# LSTM Results
lstm_results = {
    'Rajamahendravaram': {'RMSE': 0.0757, 'MAE': 0.0583, 'R2': 0.8579},
    'Vishakapatnam': {'RMSE': 0.0555, 'MAE': 0.0425, 'R2': 0.9226},
    'Vellagapudi': {'RMSE': 0.0738, 'MAE': 0.0564, 'R2': 0.8480},
    'Tirumala': {'RMSE': 0.0759, 'MAE': 0.0587, 'R2': 0.8792}
}

# Random Forest Results
rf_results = {
    'Vishakapatnam': {'RMSE': 0.5310, 'MAE': 0.4042, 'R2': 0.9565},
    'Tirumala': {'RMSE': 0.7252, 'MAE': 0.5572, 'R2': 0.9531},
    'Vellagapudi': {'RMSE': 0.7688, 'MAE': 0.5734, 'R2': 0.9231},
    'Rajamahendravaram': {'RMSE': 0.8709, 'MAE': 0.6535, 'R2': 0.9323}
}

final_lstm_accuracy = 0.8769
final_rf_accuracy = 0.9413

# Print metrics
print("=" * 80)
print("📊 COMPREHENSIVE MODEL METRICS SUMMARY")
print("=" * 80)

print("\n🔹 LSTM MODEL METRICS:")
print("-" * 80)
for city in lstm_results:
    print(f"\n{city}:")
    print(f"  RMSE: {lstm_results[city]['RMSE']:.4f}")
    print(f"  MAE:  {lstm_results[city]['MAE']:.4f}")
    print(f"  R²:   {lstm_results[city]['R2']:.4f}")
print(f"\nOverall LSTM Accuracy (R²): {final_lstm_accuracy:.4f}")

print("\n" + "=" * 80)
print("\n🔹 RANDOM FOREST MODEL METRICS:")
print("-" * 80)
for city in rf_results:
    print(f"\n{city}:")
    print(f"  RMSE: {rf_results[city]['RMSE']:.4f}")
    print(f"  MAE:  {rf_results[city]['MAE']:.4f}")
    print(f"  R²:   {rf_results[city]['R2']:.4f}")
print(f"\nOverall Random Forest Accuracy (R²): {final_rf_accuracy:.4f}")

print("\n" + "=" * 80)
print("\n📈 MODEL COMPARISON:")
print("-" * 80)

lstm_rmse = [lstm_results[c]['RMSE'] for c in lstm_results]
rf_rmse = [rf_results[c]['RMSE'] for c in rf_results]

comparison_df = pd.DataFrame({
    'Metric': ['Overall R² Score', 'Avg RMSE', 'Avg MAE'],
    'LSTM': [
        f"{final_lstm_accuracy:.4f}",
        f"{np.mean(lstm_rmse):.4f}",
        f"{np.mean([lstm_results[c]['MAE'] for c in lstm_results]):.4f}"
    ],
    'Random Forest': [
        f"{final_rf_accuracy:.4f}",
        f"{np.mean(rf_rmse):.4f}",
        f"{np.mean([rf_results[c]['MAE'] for c in rf_results]):.4f}"
    ]
})

print(comparison_df.to_string(index=False))
print("\n" + "=" * 80)
print("\n✨ Key Insights:")
print("-" * 80)
print(f"• Best Model: Random Forest (R² = {final_rf_accuracy:.4f})")
print(f"• Best City (LSTM): Vishakapatnam (R² = {lstm_results['Vishakapatnam']['R2']:.4f})")
print(f"• Best City (RF): Vishakapatnam (R² = {rf_results['Vishakapatnam']['R2']:.4f})")
print(f"• LSTM advantage: Lower error margin ({np.mean(lstm_rmse):.4f} RMSE)")
print(f"• RF advantage: Better predictive accuracy ({final_rf_accuracy:.4f} R²)")
print("=" * 80)
