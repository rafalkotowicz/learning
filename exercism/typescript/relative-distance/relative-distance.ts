export function degreesOfSeparation(familyTree: Record<string, string[]>, personA: string, personB: string): number {
  const myFamilyTree: FamilyTree = new FamilyTree(familyTree, personA, personB);
  return myFamilyTree.degreesOfSeparation();
}

class FamilyTree {
  familyTree: Record<string, string[]> = {};
  allNodes: Map<string, TreeNode<string>> = new Map();
  personA: string;
  personB: string;

  constructor(familyTree: Record<string, string[]>, personA: string, personB: string) {
    this.familyTree = familyTree;
    this.buildTree();
    this.personA = personA;
    this.personB = personB;
  }

  private buildTree(): void {
    for (const [parent, children] of Object.entries(this.familyTree)) {
      const parentNode: TreeNode<string> = this.allNodes.get(parent) || new TreeNode(parent);
      if (!this.allNodes.has(parent)) { this.allNodes.set(parent, parentNode); }

      let childNode: TreeNode<string>;
      for (const child of children) {
        childNode = this.allNodes.get(child) ?? new TreeNode(child);
        if (!this.allNodes.has(child)) {
          this.allNodes.set(child, childNode);
        }
        childNode.addParent(parentNode);
        parentNode.addChild(childNode);
      }
    }
  }

  degreesOfSeparation(): number {
    const personANode: TreeNode<string> | undefined = this.allNodes.get(this.personA);
    const personBNode: TreeNode<string> | undefined = this.allNodes.get(this.personB);
    if (!personBNode || !personBNode) {
      return -1;
    }

    let path = this.findPathBetweenNodes(personANode, personBNode);
    console.log(path);
    return path ? path.length - 1 : -1;
  }

  findPathBetweenNodes<T>(start: TreeNode<T>, target: TreeNode<T>): T[] | null {
    const path: T[] = [];
    const visited = new Set<TreeNode<T>>();

    function dfs(node: TreeNode<T>): boolean {
      if (!node || visited.has(node)) return false;

      visited.add(node);
      path.push(node.name);

      if (node === target) return true;

      for (const child of node.children) {
        if (dfs(child)) return true;
      }

      if (node.parent && dfs(node.parent)) return true;

      path.pop();
      return false;
    }

    return dfs(start) ? path : null;
  }
}

class TreeNode<T> {
  name: T;
  parent: TreeNode<T> | undefined = undefined;
  children: TreeNode<T>[] = [];

  constructor(value: T) {
    this.name = value;
  }

  addChild(child: TreeNode<T>): void {
    this.children.push(child);
  }

  addParent(parent: TreeNode<T>): void {
    this.parent = parent;
  }

  hasParent(): boolean {
    return this.parent !== undefined;
  }
}
