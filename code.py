import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
wildfire_incidents = [34.176, 30.411, 28.641, 22.061, 17.852]

percentage_reductions = [-11.5, -6.1, -24.8, -20.7]

fig, ax = plt.subplots()
bars = ax.bar(years, wildfire_incidents, color='blue')

plt.xlabel('Year')
plt.ylabel('Number of Wildfire Incidents')
plt.title('Wildfire Incidents in the Amazon in the Last 5 Years with Percentage Reductions')

for i, rect in enumerate(bars):
    height = rect.get_height()
    label = f'{height:.1f}%\nReduction'
    ax.text(rect.get_x() + rect.get_width() / 2, height, label,
            ha='center', va='bottom', color='black', fontweight='bold')

plt.grid(axis='y')
plt.show()
