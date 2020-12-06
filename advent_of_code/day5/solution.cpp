#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>


auto ReadInput() {
    std::ifstream s {"input.txt"};
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(s, line)) {
        lines.push_back(line);
    }
    return lines;
}

// Modifies string in place.
int TranslateSeat(std::string& id) {
    std::ranges::transform(id, id.begin(), [](auto c) { return (c == 'F' || c == 'L')? '0' : '1'; });
    return std::stoi(id, 0, 2);
}

// Arithmetic series up to n.
int sum_to(int n) {
    return n * (n + 1) / 2;
}

int main() {
    auto lines = ReadInput();
    std::vector<int> seats;
    for (auto line : lines) {
        seats.push_back(TranslateSeat(line));
    }
    int max = *std::ranges::max_element(seats);
    std::cout << "Part 1: " << max << std::endl;

    int min = *std::ranges::min_element(seats);
    int expected_sum = sum_to(max) - sum_to(min - 1);
    std::cout << "Part 2: " << expected_sum - std::reduce(seats.begin(), seats.end(), 0) << std::endl;
}
