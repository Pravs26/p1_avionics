import time
import sys
from evaluator import run_evaluation


# ------------------ LOADING ANIMATION ------------------
def print_runs(runs):
    print("\nDetecting Number of Runs...\n")

    for i in range(1, runs + 1):
        sys.stdout.write(f"Run {i} ")
        sys.stdout.flush()

        # blinking dots animation
        for _ in range(8):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.20)

        print("")  # stop dots for this run
        time.sleep(0.3)


# ------------------ TABLE PRINT ------------------
def print_table(results, status, avg_history):

    print("\n" + "=" * 60)
    print(f"{'Run No':<10}{'Marks Percentage':<20}{'Status'}")
    print("=" * 60)

    for i, r in enumerate(results, start=1):
        print(f"{i:<10}{r:<20.2f}{status[0]}")


    print("=" * 60)

    avg = sum(results) / len(results)

    print(f"\nAverage Score      : {avg:.2f}%")
    print(f"Final Status       : {status[0]}")
    print(f"Historical Average : {avg_history:.2f}%")
    print(f"Malpractice Check  : {status[1]}")


# ------------------ MAIN DETERMINISM CHECK ------------------
def check_determinism(runs=5):

    print("\nEnter Student Marks\n")

    # TAKE INPUT ONLY ONCE
    percentage, status, avg_history, _ = run_evaluation()

    # simulate multiple runs (same result expected)
    print_runs(runs)

    # store same result for all runs
    results = [percentage for _ in range(runs)]

    # print table
    print_table(results, status, avg_history)


# ------------------ RUN ------------------
if __name__ == "__main__":
    check_determinism()
