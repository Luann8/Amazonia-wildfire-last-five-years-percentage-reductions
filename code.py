import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, ]
wildfire_incidents = [34.176, 30.411, 28.641, 22.061]
percentage_reductions = [-11.5, -6.1, -24.8, -20.7]

fig, ax = plt.subplots()
bars = ax.bar(years, wildfire_incidents, color='blue')

plt.xlabel('Year')
plt.ylabel('Number of Wildfire Incidents')
plt.title('Wildfire Incidents in the Amazon in the Last 5 Years with Percentage Reductions')

for i, rect in enumerate(bars):
    height = rect.get_height()
    # Check if there's a corresponding percentage reduction for the current year
    if i < len(percentage_reductions):
        reduction_label = f'{height:.1f}%\nReduction: {percentage_reductions[i]:.1f}%'
        ax.text(rect.get_x() + rect.get_width() / 2, height, reduction_label,
                ha='center', va='bottom', color='black', fontweight='bold')

plt.grid(axis='y')
plt.show()
