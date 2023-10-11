class treenode():
    
    
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        
        if self.data:
            if data<self.data:
              if self.left is None:
                 self.left=node(data)
                 
              else:
                  self.left.insert(data)
                  
                 
                 
                
        
        
        
        
        
        
        
        




        

def main():
    
  n=int(input("ENTER THE NO. ELEMENTS YOU WANT IN THE TREE:"))
  
  
  root=int(input("ENTER THE ROOT FOR THE TREE:"))
  
  tree=treenode(root)
  for i in range(n):
     
    
     el=int(input("ENTER THE VALUE FOR THE NODE :"))
        
     t=treenode(el)
       
     
     if(t.value>tree.value):
         tree.right=t
         
     elif(t.value<tree.value):
         tree.left=t
         
     tree=t
  
  
  inorder_traversal(treenode(root))
  
def inorder_traversal(tree):
    
    inorder_traversal(tree.left)
    print(node.value," ")
    inorder_traversal(tree.right)
    


main()
#inorder_traversal()
    
     
        
       
     



  

#def minmax():
    
