from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from covar.ranks import to_ranks

ROOT = Path(__file__).resolve().parents[1]

# Load the returns saved
returns = pd.read_csv(ROOT / "data" / "raw" / "JPM_GSPC.csv",
                      index_col=0, parse_dates=True)
ranks = to_ranks(returns)

# How many days are in the lower-left corner?
p = 0.05
both_bad = ((ranks["bank"] <= p) & (ranks["system"] <= p)).sum()
expected = len(ranks) * p * p
print(f"Days where both are in their worst {p:.0%}: {both_bad}")
print(f"Expected if they were independent: {expected:.1f}")

# Two pictures side by side: raw returns and ranks
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

ax1.scatter(returns["bank"], returns["system"], s=4, alpha=0.3)
ax1.set_title("Daily returns (%)")
ax1.set_xlabel("Bank (JPM)")
ax1.set_ylabel("System (S&P 500)")

ax2.scatter(ranks["bank"], ranks["system"], s=4, alpha=0.3)
ax2.set_title("Ranks: the copula")
ax2.set_xlabel("Bank rank")
ax2.set_ylabel("System rank")
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_aspect("equal")

plt.tight_layout()
(ROOT / "figures").mkdir(exist_ok=True)
plt.savefig(ROOT / "figures" / "copula_jpm_sp500.png", dpi=150)
plt.show()
