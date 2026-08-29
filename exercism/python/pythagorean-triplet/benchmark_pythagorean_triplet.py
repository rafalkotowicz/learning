"""Mini benchmark for pythagorean triplet implementations."""

from __future__ import annotations

from time import perf_counter

from pythagorean_triplet import triplets_with_sum as optimized_triplets_with_sum


def baseline_triplets_with_sum(number: int) -> list[list[int]]:
    """Reference O(n^2) implementation used as benchmark baseline."""
    triplets: list[list[int]] = []

    for side_a in range(1, (number // 3) + 1):
        for side_b in range(side_a + 1, ((number - side_a) // 2) + 1):
            side_c = number - side_a - side_b
            if (side_a * side_a) + (side_b * side_b) == (side_c * side_c):
                triplets.append([side_a, side_b, side_c])

    return triplets


def measure_seconds(func, number: int, repeats: int) -> float:
    """Measure total execution time in seconds for repeated function calls."""
    started = perf_counter()
    for _ in range(repeats):
        func(number)
    return perf_counter() - started


def run_benchmark() -> None:
    """Run a small benchmark and print timing comparison."""
    benchmark_plan = [
        (1000, 200),
        (3000, 100),
        (10000, 20),
        (30000, 1),
    ]

    print("number | repeats | baseline[s] | optimized[s] | speedup[x]")
    print("-" * 61)

    for number, repeats in benchmark_plan:
        baseline_result = baseline_triplets_with_sum(number)
        optimized_result = optimized_triplets_with_sum(number)

        if baseline_result != optimized_result:
            raise RuntimeError(f"Result mismatch for number={number}")

        baseline_seconds = measure_seconds(baseline_triplets_with_sum, number, repeats)
        optimized_seconds = measure_seconds(optimized_triplets_with_sum, number, repeats)
        speedup = baseline_seconds / optimized_seconds if optimized_seconds else float("inf")

        print(
            f"{number:>6} | {repeats:>7} | {baseline_seconds:>11.6f} | "
            f"{optimized_seconds:>12.6f} | {speedup:>9.2f}"
        )


if __name__ == "__main__":
    run_benchmark()

