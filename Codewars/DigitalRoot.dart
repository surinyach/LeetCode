int recDigitalRoot(int n) {
  if (n == 0) {
    return n;
  }
  else {
    return n % 10 + digitalRoot(n ~/ 10);
  }
}

int digitalRoot(int n) {
  int res = n;
  while (res ~/ 10 > 0) {
    res = recDigitalRoot(res);
  }
  return res;
}