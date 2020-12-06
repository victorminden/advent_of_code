#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <vector>

using Rule = std::tuple<int, int, char, std::string>;

int main() {
    // Challenge: minimize number of places where types are specified.
    // Assume proper input format.  Living on the edge.
    std::ifstream s {"input.txt"};
    auto [lo, hi, a, password] = Rule {};
    std::vector<decltype(std::make_tuple(lo, hi, a, password))> rules;
    char ignore;
    // No types follow.
    while(s >> lo >> ignore >> hi >> a >> ignore >> password) {
        rules.push_back(std::make_tuple(lo, hi, a, password));
    }

    auto valid_count_part1 = std::ranges::count_if(
        rules,
        [](auto rule) {
            auto [lo, hi, a, password] = rule;
            auto count = std::ranges::count(password, a);
            return lo <= count && count <= hi;
        }
    );
    std::cout << "Part 1: " << valid_count_part1 << std::endl;

    auto valid_count_part2 = std::ranges::count_if(
        rules,
        [](auto rule) {
            auto [lo, hi, a, password] = rule;
            return (password[lo - 1]) == a != (password[hi - 1] == a);
        }
    );
    std::cout << "Part 2: " << valid_count_part2 << std::endl;
}
