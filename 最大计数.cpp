#include <iostream>
using namespace std;

int main() {
    int x, y;
    std::cout << "请输入一个整数：";
    std::cin >> x;
    std::cout << "请输入另一个整数：";
    std::cin >> y;

    for (int i = x; i>0; --i) {
        if (x%i == 0 && y%i == 0) {
            std::cout << x << "和" << y << "的最大公约数是" << i << std::endl;
            break;
        }
    }

    return 0;
}