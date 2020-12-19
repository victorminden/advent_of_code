#include <fstream>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <optional>
#include <ranges>
#include <numeric>


std::optional<int> PartOne(std::ranges::contiguous_range auto values, int target = 2020) {
    // Keep `n` if you find `m` such that `m + n = 2020`.
    auto part1_values = std::ranges::views::filter(
        values,
        [&](int n) { return std::ranges::binary_search(values, target - n); });

    // Assume that there is at most one pair of numbers in `range` summing to `target`.
    // Then there are only two or zero values in `part1_values`.
    if (part1_values.empty()) {
        return std::nullopt;
    }
    return std::accumulate(part1_values.begin(), part1_values.end(), 1, std::multiplies<int>());
}

int main() {
    std::ifstream s {"input.txt"};
    std::vector<int> values {std::istream_iterator<int> {s}, {}};
    std::ranges::sort(values);

    if (auto solution = PartOne(values, 2020)) {
        std::cout << "Part 1: "
                  << *solution
                  << std::endl;
    } else {
        // Part 1 has no solution.
        return 1;
    }

    for (auto v : values) {
        if (auto solution = PartOne(values, 2020 - v)) {
            std::cout << "Part 2: "
                      << *solution * v
                      << std::endl;
            return 0;
        }
    }
    // Part 2 has no solution.
    return 1;
}