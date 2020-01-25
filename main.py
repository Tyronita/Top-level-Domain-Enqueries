def parseCSV(fileName):
  """
  – A dictionary where each key is the first field of a record, and the value corresponding to that key is the second field of that record. If the file does not have the right format, the function returns an empty dictionary.
  """
  if fileName.find('.csv') == -1:
    return {}
  lines = open(fileName).read().split("\n")
  pairs = [tuple(line.split(",")) for line in lines][: -1]
  return dict(pairs) if len(pairs[0])  == 2 else {}

def checkTLD(tld, tldDict):
  """
  Returns True if the TLD corresponds to a valid TLD. Otherwise, it returns False.
  """
  return True if tld in tldDict else False

def extractTLD(websiteURL):
  """
  Returns the Top-Level Domain of a passed URL.
  """
  return websiteURL.split(".")[-1]

def getDescription(tld, tldDict):
  """
  Returns the description of a passed TLD if it exits. Otherwise returns an empty string.
  """
  return tldDict[tld] if checkTLD(tld, tldDict) else ''

def getTopTLD(tld, tldDict, topDict):
  """
  Returns a tuple with two items:
  - the first item is the top ranked website belonging to the TLD;
  - the second item is the rank of that website.
  If the parameter tld is not a correct TLD, or if it corresponds to a TLD that is not in the one million top, the function returns an empty tuple.
  """
  if not checkTLD(tld, tldDict):
    return ()
  for rank in range(1, len(topDict) + 1):
    url = topDict[str(rank)]
    if extractTLD(url) == tld:
      return url, rank

def countTLD(tld, tldDict, topDict):
  """
  An integer representing the number of websites in the 
  top one million that belong to the TLD. If the parameter tld is not a TLD, the function returns -1. 
  """
  if not checkTLD(tld, tldDict):
    return -1
  count = 0
  for rank in range(1, len(topDict) + 1):
    url = topDict[str(rank)]
    if extractTLD(url) == tld:
      count += 1
  return count

# Save the databases to corresponding dictionaries
tldDict = parseCSV("tlds.csv")
topDict = parseCSV("top-1m.csv")

# Main Program
while True:

  # Forces user to enter a valid Top Level Domain
  tld = input("Enter the top-level domain: ").lower()
  while not checkTLD(tld, tldDict):
    tld = input("Not a valid TLD. Try again: ").lower()

  print(f"TLD '.{tld}' description: {getDescription(tld, tldDict)}.")
  print(f"There are {countTLD(tld, tldDict, topDict)} websites in the top 1 million ranked websites with the '.{tld}' TLD.")
  topTld = getTopTLD(tld, tldDict, topDict)
  if topTld:
    topURL, rank = topTld
    print(f"The top ranked URL with the TLD '{tld}' is '{topURL} placed at rank #{str(rank)}.\n")

  # Prompts user asking them if they want to repat
  repeatAgain = input("Do you want to enter another TLD? y/n: ").lower()
  while repeatAgain != "y" and repeatAgain != "n":
    repeatAgain = input("Do you want to enter another TLD? y/n: ").lower()
  if repeatAgain == "n":
    break






