#include <fstream>
#include <iostream>
#include <vector>
#include <ranges>
#include <regex>

constexpr int kNumLines = 1000;

auto ParseLine(const std::string& line) {
    std::smatch match;
    std::regex_match(line, match, std::regex {"(\\d+)-(\\d+) (\\w): (\\w+)"});

    int lo = std::atoi(match[1].str().c_str()),
        hi = std::atoi(match[2].str().c_str());
    char a = match[3].str()[0];
    std::string password = match[4].str();

    return std::make_tuple(lo, hi, a, password);
}

auto ReadInput() {
    // A little redundant here, but keeping this function entirely separate for re-use later.
    std::ifstream s {"input.txt"};
    std::vector<std::string> lines;
    lines.reserve(kNumLines);
    std::string line;
    while (std::getline(s, line)) {
        lines.push_back(line);
    }
    return lines;
}

int main() {
    // Is there a better way to get the return type of an auto function without having to pass it input?
    std::vector<decltype(ParseLine(""))> rules;
    rules.reserve(kNumLines);
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