bool validBraces(String braces) {
  const pairs = {
    "[" : "]",
    "{" : "}",
    "(" : ")",
  };
  
  var stack = <String>[];
  for (String c in braces.split('')) {
    if (c == "(" || c == "{" || c == "[") stack.add(c);
    else {
      if (stack.isEmpty) return false; 
      String last = stack.removeLast();
      if (pairs[last] != c) return false;
    }
  }
  
  return stack.isEmpty;
}