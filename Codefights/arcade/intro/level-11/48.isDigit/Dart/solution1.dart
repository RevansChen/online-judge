// Dart

bool isDigit(String symbol) {
    int asc = symbol.codeUnitAt(0);
    return 0x30 <= asc && asc <= 0x39;
}
