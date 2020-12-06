#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>

using Person = std::string;
using Group = std::vector<Person>;

auto ReadInput() {
    std::ifstream s {"input.txt"};
    std::vector<Group> groups;
    Group group;
    Person person;
    while (std::getline(s, person)) {
        if (person.empty()) {
            groups.push_back(group);
            group = Group {};
        } else {
            std::ranges::sort(person);
            group.push_back(person);
        }
    }
    // Last group.
    groups.push_back(group);
    return groups;
}

int main() {
    auto groups = ReadInput();

    auto union_view = std::ranges::transform_view(
        groups,
        [](auto group) {
            auto grand_union = std::reduce(
                group.begin(),
                group.end(),
                group[0],
                [](auto a, auto b) {
                    std::string a_u_b;
                    std::set_union(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(a_u_b));
                    return a_u_b;
                });
            return grand_union.length();
        });

    std::cout << "Part 1: " << std::reduce(union_view.begin(), union_view.end(), 0) << std::endl;


    auto intersection_view = std::ranges::transform_view(
        groups,
        [](auto group) {
            auto grand_intersection = std::reduce(
                group.begin(),
                group.end(),
                group[0],
                [](auto a, auto b) {
                    std::string a_i_b;
                    std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(a_i_b));
                    return a_i_b;
                });
            return grand_intersection.length();
        });

    std::cout << "Part 2: " << std::reduce(intersection_view.begin(), intersection_view.end(), 0) << std::endl;
}
