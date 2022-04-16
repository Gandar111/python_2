class newclass():
     class_variable=3
     def methode(self, attibutte):
          self.class_variable=attibutte
          return self.class_variable*2
projekt= newclass()
l=projekt.methode(28)
print(l)
