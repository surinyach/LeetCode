String createPhoneNumber(List numbers) {
  String res = "(";
  for (int i = 0; i < numbers.length; ++i) {
    if (i == 6) res += "-";
    int n = numbers[i];
    res += "$n";
    if (i == 2) res += ") ";
  }
  return res;
}