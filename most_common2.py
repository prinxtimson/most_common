def man_string(alpa):
  d = {}
  if alpa != str(alpa):
    print 'only string input is accepted'
  elif len(alpa) < 3 or len(alpa) > 100:
    print 'Invalid input'
  else:
    for x in alpa:
	  d[x] = d.get(x, 0) + 1
    lst = list(d.items())
    for x in range(0, len(lst)):
      for y in range(0, len(lst)):
        if lst[x][1] < lst[y][1]:
		  pass
        elif lst[x][1] == lst[y][1]:
          if lst[x] < lst[y]:
		    temp = lst[x]
		    lst[x] = lst[y]
		    lst[y] = temp
        else:
		  temp = lst[x]
		  lst[x] = lst[y]
		  lst[y] = temp
    for x, y in lst[:3]:
      print x, y 
	  
	  
	  
	  
	  
man_string('aadadccacdbebde')