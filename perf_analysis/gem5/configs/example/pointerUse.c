void tryPointer() {
    int one = 1;
    int *ptraddr = &one;
    int ptrVal = *ptraddr;
}

int main() {
    tryPointer();
    return 1;
}
