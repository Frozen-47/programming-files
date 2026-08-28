// C++ Program: Matrix Multiplication (2x2 and 3x3)
// Date: 2026-08-28

#include <iostream>
#include <vector>

using namespace std;

void multiplyMatrices(const vector<vector<int>>& A, const vector<vector<int>>& B, vector<vector<int>>& C, int r1, int c1, int c2) {
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            C[i][j] = 0;
            for (int k = 0; k < c1; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    vector<vector<int>> A = {{1, 2}, {3, 4}};
    vector<vector<int>> B = {{5, 6}, {7, 8}};
    vector<vector<int>> C(2, vector<int>(2, 0));

    multiplyMatrices(A, B, C, 2, 2, 2);

    cout << "Resultant Matrix:" << endl;
    for (const auto& row : C) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}
