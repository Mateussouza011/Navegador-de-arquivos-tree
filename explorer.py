class Node:
    def __init__(self, name, is_folder=True):
        self.name = name
        self.is_folder = is_folder
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def browse(node, path=[]):
    print("Caminho Atual:", " -> ".join(path + [node.name]))
    if node.is_folder:
        for child in node.children:
            print(child.name)
        print("Digite 'voltar' para retornar à pasta anterior")
        folder_name = input("Digite o nome da pasta para navegar: ")
        if folder_name == 'voltar':
            if path:
                path.pop()
                browse(path.pop())
            else:
                browse(node, path)
        else:
            for child in node.children:
                if child.name == folder_name:
                    browse(child, path + [node.name])


raiz = Node("Raiz")
pasta1 = Node("Pasta 1")
pasta2 = Node("Pasta 2")
pasta3 = Node("Pasta 3")  
subpasta1 = Node("Subpasta 1")
subpasta2 = Node("Subpasta 2")
subpasta3_1 = Node("Subpasta 3_1")  
subpasta3_2 = Node("Subpasta 3_2") 
arquivo1 = Node("Arquivo 1", is_folder=False)
arquivo2 = Node("Arquivo 2", is_folder=False)
arquivo3 = Node("Arquivo 3", is_folder=False)
arquivo4 = Node("Arquivo 4", is_folder=False)
arquivo5 = Node("Arquivo 5", is_folder=False)  
arquivo6 = Node("Arquivo 6", is_folder=False)  

raiz.add_child(pasta1)
raiz.add_child(pasta2)
raiz.add_child(pasta3) 
pasta1.add_child(arquivo1)
pasta1.add_child(subpasta1)
subpasta1.add_child(arquivo2)
subpasta1.add_child(arquivo3)
pasta2.add_child(subpasta2)
subpasta2.add_child(arquivo4)
pasta3.add_child(subpasta3_1)  
pasta3.add_child(subpasta3_2)  
pasta3.add_child(arquivo5)  
pasta3.add_child(arquivo6)  


browse(raiz)
