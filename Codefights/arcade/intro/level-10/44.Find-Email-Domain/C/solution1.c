char * findEmailDomain(char * address) {
    char *start = address + strlen(address) - 1;
    while (*start != '@') start--;
    return start + 1;
}
