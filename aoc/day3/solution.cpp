#include <algorithm>
#include <fstream>
#include <iostream>
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

auto CountTrees(const std::vector<std::string>& grid, int slope_x = 3, int slope_y = 1) {
    // The lack of strided views in C++20 is unfortunate.  The original implementation plan was strides.
    int i {0}, j {0};
    return std::ranges::count_if(
        grid,
        [&](auto row) { return (j++ %  slope_y == 0) && (row[(i++ * slope_x) % row.length()] == '#'); }
    );
}

int main() {
    auto lines = ReadInput();
    std::cout << "Part 1: " << CountTrees(lines) << std::endl;
    std::cout << "Part 2: "
              << CountTrees(lines, 1, 1) * CountTrees(lines, 3, 1) * CountTrees(lines, 5, 1) * CountTrees(lines, 7, 1) *
                 CountTrees(lines, 1, 2)
              << std::endl;
}
