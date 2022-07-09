export function find(haystack, needle) {
    if (haystack.length === 0 || haystack[0] > needle || haystack[haystack.length - 1] < needle) {
        throw new Error('Value not in array');
    }
    let left = 0;
    let right = haystack.length - 1;
    let searchedIndex;
    while (left <= right) {
        searchedIndex = Math.floor((left + right) / 2);
        if (haystack[searchedIndex] < needle) {
            left = searchedIndex + 1;
        }
        else if (haystack[searchedIndex] > needle) {
            right = searchedIndex - 1;
        }
        else {
            return searchedIndex;
        }
    }
    throw new Error('Value not in array');
}
