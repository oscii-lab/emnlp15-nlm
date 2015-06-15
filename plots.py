import matplotlib.pyplot as plt

days = [3, 4, 5]
orig = [0.2577, 0.2577, 0.2577]
repeat_all = [0.2335, 0.2493, 0.2704]
repeat_symbol = [0.2351, 0.2644, 0.2652]
no_repeats = [0.2404, 0.2542, 0.2579]

plt.plot(days, orig, "k--", days, repeat_all, "r", days, repeat_symbol, "g", days, no_repeats, "b")
plt.axis([3, 5, 0.23, 0.28])
plt.xlabel("Days trained")
plt.ylabel("BLEU score")
plt.legend(["Original System, 5 days", "Repeat-All", "Repeat-Symbol", "No-Repeats"], loc=4)
plt.savefig("images/graph.png")
plt.show()
