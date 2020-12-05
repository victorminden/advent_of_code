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

auto ReadInput() {
    // A little redundant here, but keeping this function entirely separate for re-use later.
    std::ifstream s {"input.txt"};
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(s, line)) {
        lines.push_back(line);
    }
    return lines;
}

int main() {
    // Is there a better way to get the return type of an auto function without having to pass it input?
    std::vector<decltype(ParseLine(""))> rules;
    for (auto line : ReadInput()) {
        rules.push_back(ParseLine(line));
    }

    int valid_count_part1 = 0, valid_count_part2 = 0;
    for (auto [lo, hi, a, password] : rules) {
        // Part 1.
        int count = std::ranges::count(password, a);
        if (lo <= count && count <= hi) {
            valid_count_part1 += 1;
        }
        // Part 2.
        if ((password[lo - 1] == a) != (password[hi -1] == a)) {
           valid_count_part2 += 1;
        }
    }

    std::cout << "Part 1: " << valid_count_part1 << std::endl;
    std::cout << "Part 2: " << valid_count_part2 << std::endl;
}