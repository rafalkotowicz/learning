export function isValid(isbn: string): boolean {
  const cleanedIsbn = isbn.replace(/-/g, '');
  const regex = /^[0-9]{9}[0-9X]$/;

  if (!regex.test(cleanedIsbn)) {
    return false;
  }

  let sum = 0;
  for (let i = 0; i < cleanedIsbn.length; i++) {
    const char = cleanedIsbn[i];
    const value = char === 'X' ? 10 : parseInt(char, 10);
    sum += value * (10 - i);
  }

  return sum % 11 === 0;
}
