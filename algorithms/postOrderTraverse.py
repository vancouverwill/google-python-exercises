

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        # self.val = key
        self.postVal = None

postOrderIndex = 1
# index = 0

def answer(h, q):
    # postOrderIndex = 1
    # index = 0
    def createTree(height) :
        if height < 1 :
            return
        # global index
        # index = index + 1
        node = Node()
        if height > 1  :
            node.left = createTree(height - 1)
            node.right = createTree(height - 1)
        return  node

    # post order traverse through binary tree and set the post values to their post order index
    def postOrderTraverseSetVal(root) :
        if not root:
            return

        postOrderTraverseSetVal(root.left)
        postOrderTraverseSetVal(root.right)
        global postOrderIndex
        root.postVal = postOrderIndex
        postOrderIndex = postOrderIndex+1

    def postOrderTraversePrint(root, printPost = False) :
        if not root:
            return

        postOrderTraversePrint(root.left, printPost)
        postOrderTraversePrint(root.right, printPost)

        if not printPost :
            print root.val
        else :
            print str(root.val) +':'+ str(root.postVal)

    def postOrderTraverseFindParents(parent, root, needle) :
        if not root:
            return
        lParentVal = postOrderTraverseFindParents(root, root.left, needle)
        if lParentVal is not None:
            return lParentVal
        rParentVal = postOrderTraverseFindParents(root, root.right, needle)
        if rParentVal is not None:
            return rParentVal
        if root.postVal == needle :
            if parent is not None :
                return parent.postVal
            else :
                return -1
    treeRoot = createTree(h)

    global postOrderIndex
    postOrderIndex = 1
    postOrderTraverseSetVal(treeRoot)
    # print postOrderIndex

    # postOrderTraversePrint(treeRoot, True)
    output = []
    for i in q:
        output.append(postOrderTraverseFindParents(None, treeRoot, i))
    return output

def main() :
    print 'hello world!'
    print''


    input = [7, 3, 5, 1]
    print input

    # print answer(3, [7, 3, 5, 1])
    # print answer(5, [19, 14, 28])
    print answer(5, [19, 14, 28])

if __name__ == '__main__':
  main()