tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree, root, pruned
    i = 0
    for child in branch:
        if isinstance(child, list):
            nalpha, nbeta = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = min(beta, nalpha)
            else:
                alpha = max(alpha, nbeta)
            branch[i] = alpha if depth % 2 == 0 else beta
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
        if alpha >= beta:
            pruned += 1
            break
        i += 1

    if depth == root:
        tree = alpha if root == 0 else beta
    return (alpha, beta)

def alphabeta(in_tree=None, start=root, upper=-15, lower=15):
    global tree, pruned, root
    if in_tree is not None:
        tree = in_tree
    alpha, beta = children(tree, start, upper, lower)
    
    if __name__ == "__main__":
        print("Name: Shekhar Suman")
        print("Roll No: 47")
        print("(alpha, beta):", alpha, beta)
        print("Result:", tree)
        print("Times pruned:", pruned)
    return (alpha, beta, tree, pruned)

if __name__ == "__main__":
    alphabeta()
