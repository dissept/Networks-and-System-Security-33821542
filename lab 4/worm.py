import random
import time

TOTAL_HOSTS = 100
infected = set([0])

attempts_per_step = 5

print("Starting worm simulation...\n")

for step in range(20):

    new_infections = set()

    for host in infected:
        for _ in range(attempts_per_step):
            target = random.randint(0, TOTAL_HOSTS - 1)
            if target not in infected:
                new_infections.add(target)

    infected |= new_infections

    print(f"Step {step}: {len(infected)} infected hosts")

    if len(infected) == TOTAL_HOSTS:
        print("\nAll hosts infected!")
        break

print("\nSimulation complete.")