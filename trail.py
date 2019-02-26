import io
my_list = ['1','2','3']
with io.open('demo.txt', 'w') as file:
  for i in my_list:
    file.write(i)
