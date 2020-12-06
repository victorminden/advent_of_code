#include <algorithm>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <vector>

auto ParseLine(const std::string& line) {
    // Format: "(\\d+)-(\\d+) (\\w): (\\w+)"
    int lo, hi;
    char a, ignore;
    std::string password;
    std::istringstream ss {line};
    ss >> lo >> ignore >> hi >> a >> ignore >> password;
    return std::make_tuple(lo, hi, a, password);
}

int main() {
    // Is there a better way to get the return type of an auto function without having to pass it input?
    std::ifstream s {"input.txt"};
    std::string line;
    std::vector<decltype(ParseLine(""))> rules;

    while(std::getline(s, line)) {
        rules.push_back(ParseLine(line));
    }

    int valid_count_part1 = std::ranges::count_if(
        rules,
        [](auto rule) {
            auto [lo, hi, a, password] = rule;
            int count = std::ranges::count(password, a);
            return lo <= count && count <= hi;
        }
    );
    std::cout << "Part 1: " << valid_count_part1 << std::endl;

    int valid_count_part2 = std::ranges::count_if(
        rules,
        [](auto rule) {
            auto [lo, hi, a, password] = rule;
            return (password[lo - 1]) == a != (password[hi - 1] == a);
        }
    );
    std::cout << "Part 2: " << valid_count_part2 << std::endl;
}