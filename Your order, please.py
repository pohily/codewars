def order(sentence):
  if not sentence:
      return ''
  words = sentence.split()
  result = {}
  for word in words:
      for letter in word:
          if letter.isdigit():
              result[letter] = word
              break
  output = ''
  for i in sorted(result.keys()):
      output += result[i] + ' '
  return output[:-1]