import matplotlib.pyplot as plt

days = [3, 4, 5]
orig = [0.2577, 0.2577, 0.2577]
repeat_common = [0.2335, 0.2493, 0.2704]
repeat_symbol = [0.2, 0.2, 0.2]
no_repeats = [0.3, 0.3, 0.3]

plt.plot(days, orig, "k--", days, repeat_common, "r", days, repeat_symbol, "g", days, no_repeats, "b")
plt.axis([3, 5, 0.2, 0.28])
plt.xlabel("Days trained")
plt.ylabel("BLEU score")
plt.legend(["Original System, 5 days", "Repeat-Common", "Repeat-Symbol", "No-Repeats"], loc=4)
plt.show()
