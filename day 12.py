file = open("30days30houroperations.txt","w+")
file.write("I have completed 10 days Successfully.\n")
file.close()
file = open("30days30houroperations.txt","a")
file.write("Deepika")
file.close()
file = open("30days30houroperations.txt","r+")
print(file.read())
file.close()
