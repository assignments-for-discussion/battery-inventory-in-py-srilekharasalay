
def count_batteries_by_usage(cycles):
  lowCount=0
  mediumCount=0
  highCount=0
  for i in cycles:
    if (i<=400):
         lowCount+=1
    elif (i>=400 and i<=919):
         mediumCount+=1
    elif (i>=920):
         highCount+=1
    
  return (lowCount,mediumCount,highCount)
     
    
  


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100,300, 500,600, 900, 1000])
  print(count)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
