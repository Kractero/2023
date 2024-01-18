import matplotlib.pyplot as plt
import numpy as np

# Hourly

hours = np.arange(24)
total_trades = [113436, 114036, 111010, 107194, 94599, 86013, 87508, 89604, 95962, 79598,
                71939, 79068, 83346, 91905, 98919, 109234, 116086, 116305, 120828, 127516,
                128689, 129783, 123905, 116696]
money_moved = [149892.53, 155002.44, 144957.68, 148705.67, 136951.67, 130416.53, 125992.13, 139170.92,
               199056.45, 120374.23, 83971.04, 75039.10, 75831.76, 93038.80, 101369.13, 103668.68,
               127366.42, 138870.67, 133231.79, 143125.11, 147428.60, 146909.10, 157420.83, 134427.53]

plt.figure(figsize=(10, 6))
plt.plot(hours, total_trades, label='Total Trades', marker='o')
plt.plot(hours, money_moved, label='Money Moved', marker='o')

plt.xlabel('Hour of the Day')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Hour of the Day')
plt.xticks(hours)
plt.legend()

plt.savefig('Hourly.png')

# Weekly

hours = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
total_trades = [397266, 352726, 352134, 349130, 329902, 341741, 370280]
money_moved = [509982.40, 461864.41, 456240.22, 431593.36, 411712.97, 396818.95, 444006.50]

plt.figure(figsize=(10, 6))
plt.plot(hours, total_trades, label='Total Trades', marker='o')
plt.plot(hours, money_moved, label='Money Moved', marker='o')

plt.xlabel('Day of the Week')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Day of the Week')
plt.xticks(hours)
plt.legend()

plt.savefig('Daily.png')

# Monthly

months = ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
total_trades = [271404, 193665, 222917, 185720, 219461, 185709, 209809, 231064, 188742, 185537, 195958, 203193]
money_moved = [292793.48, 193129.92, 259635.81, 253606.95, 232034.37, 172846.79, 291856.94, 381505.07, 224038.00, 260495.24, 217322.43, 332953.81]

plt.figure(figsize=(10, 6))
plt.plot(months, total_trades, label='Total Trades')
plt.plot(months, money_moved, label='Money Moved', alpha=0.7)

plt.xlabel('Month')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Month')
plt.xticks(months)
plt.legend()

plt.savefig('Monthly.png')