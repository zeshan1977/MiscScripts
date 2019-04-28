
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once.


"""
def solution(number):
    newnum=number
    newnewnum=0
    while 0 < newnum <= 11:
      newnum=newnum -1
      res = isMultipleof(newnum,newnum)
      if (res == 1):
         newnewnum = newnewnum+newnum
      else:
          pass
    return newnewnum

def isMultipleof(threeorfive,number):
    if (threeorfive == 3):
        if (number % 3)== 0:
            return 1
        return 0
    elif (threeorfive == 5):
        if (number % 5)== 0:
            return 1
        return 0
    else:
        return -1


if __name__ == "__main__":
    print solution(10)