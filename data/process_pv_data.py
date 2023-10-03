# Formatage des données PV

```python
# data/process_pv_data.py

pv = pd.read_csv('generation/PV_plant.csv')

pv['datetime'] = pd.to_datetime(pv['datetime'])
pv = pv.set_index('datetime')
```