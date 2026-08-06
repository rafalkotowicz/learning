import java.util.*;

class RelativeDistance {
    private final Map<String, FamilyNode> nodesByName;

    RelativeDistance(Map<String, List<String>> familyTree) {
        this.nodesByName = buildFamilyTree(familyTree);
    }

    int degreeOfSeparation(String personA, String personB) {
        if (personA.equals(personB)) {
            return 0;
        }

        FamilyNode nodeA = nodesByName.get(personA);
        FamilyNode nodeB = nodesByName.get(personB);
        if (nodeA == null || nodeB == null) {
            return -1;
        }

        int aIsAncestorOfB = distanceToAncestor(nodeB, nodeA);
        if (aIsAncestorOfB >= 0) {
            return aIsAncestorOfB;
        }

        int bIsAncestorOfA = distanceToAncestor(nodeA, nodeB);
        if (bIsAncestorOfA >= 0) {
            return bIsAncestorOfA;
        }

        Map<String, Integer> ancestorsOfA = ancestorDistances(nodeA);
        Map<String, Integer> ancestorsOfB = ancestorDistances(nodeB);

        int best = Integer.MAX_VALUE;
        for (Map.Entry<String, Integer> ancestorOfA : ancestorsOfA.entrySet()) {
            Integer distanceFromB = ancestorsOfB.get(ancestorOfA.getKey());
            if (distanceFromB == null) {
                continue;
            }

            int candidate = ancestorOfA.getValue() + distanceFromB - 1;
            if (candidate < best) {
                best = candidate;
            }
        }

        return best == Integer.MAX_VALUE ? -1 : best;
    }

    private int distanceToAncestor(FamilyNode descendant, FamilyNode ancestor) {
        ArrayDeque<FamilyNode> queue = new ArrayDeque<>();
        Map<String, Integer> distance = new HashMap<>();

        queue.add(descendant);
        distance.put(descendant.name, 0);

        while (!queue.isEmpty()) {
            FamilyNode current = queue.remove();
            int currentDistance = distance.get(current.name);

            for (FamilyNode parent : current.parents) {
                if (distance.containsKey(parent.name)) {
                    continue;
                }

                int parentDistance = currentDistance + 1;
                if (parent == ancestor) {
                    return parentDistance;
                }

                distance.put(parent.name, parentDistance);
                queue.add(parent);
            }
        }

        return -1;
    }

    private Map<String, Integer> ancestorDistances(FamilyNode person) {
        ArrayDeque<FamilyNode> queue = new ArrayDeque<>();
        Map<String, Integer> distance = new HashMap<>();

        for (FamilyNode parent : person.parents) {
            queue.add(parent);
            distance.put(parent.name, 1);
        }

        while (!queue.isEmpty()) {
            FamilyNode current = queue.remove();
            int currentDistance = distance.get(current.name);

            for (FamilyNode parent : current.parents) {
                if (distance.containsKey(parent.name)) {
                    continue;
                }

                distance.put(parent.name, currentDistance + 1);
                queue.add(parent);
            }
        }

        return distance;
    }

    private Map<String, FamilyNode> buildFamilyTree(Map<String, List<String>> tree) {
        Map<String, FamilyNode> nodes = new HashMap<>();

        for (Map.Entry<String, List<String>> entry : tree.entrySet()) {
            FamilyNode parent = nodes.computeIfAbsent(entry.getKey(), FamilyNode::new);
            for (String childName : entry.getValue()) {
                FamilyNode child = nodes.computeIfAbsent(childName, FamilyNode::new);
                parent.addChild(child);
                child.addParent(parent);
            }
        }

        return nodes;
    }

    private static final class FamilyNode {
        private final String name;
        private FamilyNode leftChild;
        private FamilyNode rightChild;
        private final List<FamilyNode> parents;

        private FamilyNode(String name) {
            this.name = name;
            this.parents = new ArrayList<>(2);
        }

        private void addChild(FamilyNode child) {
            if (leftChild == null) {
                leftChild = child;
                return;
            }

            if (rightChild == null) {
                rightChild = child;
                return;
            }

            throw new IllegalArgumentException(
                "A parent cannot have more than two children in this binary tree representation."
            );
        }

        private void addParent(FamilyNode parent) {
            if (!parents.contains(parent)) {
                parents.add(parent);
            }
        }
    }
}
