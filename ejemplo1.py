import numpy as np
import pandas as pd

# Una semilla fija genera los mismos número cada vez
# que se ejecuta el notebook
rng = np.random.default_rng(seed=42)

years = rng.uniform(0,12,size=30).round(1)
salary = 22_000 + 2_600 * years + rng.normal(0, 4_000, size=30)
df = pd.DataFrame({"YearsExperience": years, "Salary": salary.round(-2)})

# Mostrar las primeras cinco filas de los datos
print(df.head())

# Mostrar información sobre el DataFrame
print(df.info())
