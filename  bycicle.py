bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #list of values
print(bicycles)

#Acess items in the lists
print(bicycles[0])  #"tre
print(bicycles[0].title())  #add a method --> #"Trek"

print(bicycles[-1].title()) #last item --> "Specialized"--> [-2], [-3]

message = "My first bicycle was a " + bicycles[-2].title() + "."
print(message)
