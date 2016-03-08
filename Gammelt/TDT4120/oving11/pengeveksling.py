from sys import stdin

def minCoinsGreedy(coins, value):
  s = 0
  i = 0
  while value > 0:
    s += value / coins[i]
    value %= coins[i]
    i += 1
  return s


def minCoinsDynamic(coins, value):
  memo = {0:0}



def canUseGreedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut 
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    for c in coins:
      if c % 5 > 1:
        return False
    return True


coins = sorted(map(int, stdin.readline().split()), reverse=True)
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print minCoinsGreedy(coins, int(line))
else:
    for line in stdin:
        print minCoinsDynamic(coins, int(line))
