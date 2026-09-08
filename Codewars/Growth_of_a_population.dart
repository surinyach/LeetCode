int nbYear(int p0, double percent, int aug, int p) {
  int years = 0;
  while (p0 < p) {
    int per = p0 * percent ~/ 100;
    p0 = p0 + per + aug;
    years += 1;
  }
  
  return years;
}