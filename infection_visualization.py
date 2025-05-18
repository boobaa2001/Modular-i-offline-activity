import numpy as np
import matplotlib.pyplot as plt

# Parameters
sensitivity = 0.99
specificities = [0.99, 0.999, 0.9999, 0.99999]
prevalence_range = np.linspace(0.00001, 0.5, 500)  # from 0.001% to 50%

# Compute posterior probabilities
posteriors = {}
for spec in specificities:
    numerator = sensitivity * prevalence_range
    denominator = numerator + (1 - spec) * (1 - prevalence_range)
    posteriors[spec] = numerator / denominator

# Plotting
plt.figure()
for spec, posterior in posteriors.items():
    plt.plot(prevalence_range * 100, posterior * 100, label=f'Specificity = {spec*100:.5f}%')
plt.xlabel('Prevalence (%)')
plt.ylabel('P(Infected | Positive) (%)')
plt.title('Posterior Probability vs. Prevalence\nfor Various Specificity Levels\n(Sensitivity fixed at 99%)')
plt.legend()
plt.grid(True)
plt.show()

# Integer-based check for the 5% prevalence, 99.5% specificity example
N = 10000
prevalence_demo = 0.05
specificity_demo = 0.995

infected = int(N * prevalence_demo)
uninfected = N - infected
true_positives = int(infected * sensitivity)
false_positives = int(uninfected * (1 - specificity_demo))
posterior_demo = true_positives / (true_positives + false_positives)

print(f"Out of {N} people, with prevalence {prevalence_demo*100:.1f}%:")
print(f"  Infected: {infected}, Uninfected: {uninfected}")
print(f"  True Positives: {true_positives}, False Positives: {false_positives}")
print(f"Posterior P(infected | +) ≈ {posterior_demo*100:.2f}%")
