Map<String, int> count(String s) {
  
  if (s.length == 0) {
    return {};  
  }
  
  var count = Map<String,int>();
  for (int c = 0; c < s.length; ++c) {
    String letter = s[c];
    count[letter] = (count[letter] ?? 0) + 1;
  }
  
  return count;
}