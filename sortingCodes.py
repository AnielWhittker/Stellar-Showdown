# merge sort algorithm code snippet
mergeSort = '''#include <vector>

void merge(std::vector<int>& vec, int start, int mid, int end) {
    std::vector<int> left(vec.begin() + start, vec.begin() + mid + 1);
    std::vector<int> right(vec.begin() + mid + 1, vec.begin() + end + 1);
    
    int i = 0;
    int j = 0;
    int k = start;

    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            vec[k] = left[i];
            i++;
        } else {
            vec[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < left.size()) {
        vec[k] = left[i];
        i++;
        k++;
    }

    while (j < right.size()) {
        vec[k] = right[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& vec, int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;
        mergeSort(vec, start, mid);
        mergeSort(vec, mid + 1, end);
        merge(vec, start, mid, end);
    }
}'''