#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <ranges>
#include <regex>
#include <set>
#include <vector>

using Bag = std::string;
using BagList = std::vector<std::tuple<Bag, int>>;


auto parse_line(std::string& line) {
    std::smatch match;
    std::regex_search(line, match, std::regex{"([\\w\\s]*) bags contain"});
    auto bag_description = match[1];

    BagList bags;
    std::regex expression{"(\\d+) ([\\w\\s]*) bags?"};
    auto begin = std::sregex_iterator(line.begin(), line.end(), expression);
    auto end = std::sregex_iterator{};
    for (auto match = begin; match != end; ++match) {
        bags.push_back(std::make_tuple((*match)[2], std::stoi((*match)[1])));
    }
    std::ranges::sort(bags);
    return std::make_tuple(bag_description, bags);
}

int holds_how_many(const Bag& bag, std::map<Bag, BagList> &bag_map) {
    auto children = bag_map[bag];
    int sum = 1;
    for (auto [child, n] : children) {
        sum += n * holds_how_many(child, bag_map);
    }
    return sum;
}

int fits_in_how_many(
    const Bag& bag, 
    std::map<Bag, std::vector<Bag>>& reversed_bag_map,
    std::set<Bag> &visited) {
    auto children = reversed_bag_map[bag];
    int sum = 1;
    for (auto child : children) {
        if (visited.contains(child)) {
            continue;
        }
        visited.insert(child);
        sum += fits_in_how_many(child, reversed_bag_map, visited);
    }
    // TODO: add a marked array.
    return sum;
}

int main() {
    std::ifstream s {"input.txt"};
    std::string line;

    std::map<Bag, BagList> bag_map;
    std::map<Bag, std::vector<Bag>> reversed_bag_map;

    while (std::getline(s, line))
    {
        auto [src, dsts] = parse_line(line);
        bag_map[src] = dsts;
        for (auto [d, n] : dsts) {
            reversed_bag_map[d].push_back(src);
        }
    }
    // Part 1.
    for (auto [k, v] : reversed_bag_map) {
        std::ranges::sort(v);
        std::ranges::unique(v);
    }
    std::set<Bag> visited {};
    std::cout << "Part 1: " 
              << fits_in_how_many("shiny gold", reversed_bag_map, visited) - 1 
              << std::endl;

    // Part 2.
    std::cout << "Part 2: " 
              << holds_how_many("shiny gold", bag_map) - 1 
              << std::endl;

    return 0;
}
