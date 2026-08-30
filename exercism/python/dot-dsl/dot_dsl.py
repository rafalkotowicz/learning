"""Internal DSL objects for constructing graph definitions."""

NODE, EDGE, ATTR = range(3)
MIN_GRAPH_ITEM_LENGTH = 2
NODE_ITEM_LENGTH = 3
EDGE_ITEM_LENGTH = 4
ATTRIBUTE_ITEM_LENGTH = 3


class Node:  # pylint: disable=too-few-public-methods
    """Represents a graph node with optional attributes."""

    def __init__(self, name: str, attrs: dict[str, str]):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.name == other.name and self.attrs == other.attrs

    def __hash__(self) -> int:
        return hash((self.name, tuple(sorted(self.attrs.items()))))


class Edge:  # pylint: disable=too-few-public-methods
    """Represents a graph edge between two nodes."""

    def __init__(self, src: str, dst: str, attrs: dict[str, str]):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)

    def __hash__(self) -> int:
        return hash((self.src, self.dst, tuple(sorted(self.attrs.items()))))


class Graph:  # pylint: disable=too-few-public-methods
    """Represents a graph composed of attributes, nodes, and edges."""

    def __init__(self, data: list[tuple] | None = None):
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.attrs: dict[str, str] = {}

        if data is None:
            return

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for graph_item in data:
            if not isinstance(graph_item, tuple) or len(graph_item) < MIN_GRAPH_ITEM_LENGTH:
                raise TypeError("Graph item incomplete")

            item_type = graph_item[0]

            if item_type == NODE:
                self._add_node(graph_item)
            elif item_type == EDGE:
                self._add_edge(graph_item)
            elif item_type == ATTR:
                self._add_attribute(graph_item)
            else:
                raise ValueError("Unknown item")

    def _add_node(self, graph_item: tuple) -> None:
        if len(graph_item) != NODE_ITEM_LENGTH:
            raise ValueError("Node is malformed")

        node_name, node_attributes = graph_item[1], graph_item[2]
        if not isinstance(node_name, str) or not isinstance(node_attributes, dict):
            raise ValueError("Node is malformed")  # noqa: TRY004

        self.nodes.append(Node(node_name, node_attributes))

    def _add_edge(self, graph_item: tuple) -> None:
        if len(graph_item) != EDGE_ITEM_LENGTH:
            raise ValueError("Edge is malformed")

        edge_source, edge_destination, edge_attributes = graph_item[1], graph_item[2], graph_item[3]
        if (
            not isinstance(edge_source, str)
            or not isinstance(edge_destination, str)
            or not isinstance(edge_attributes, dict)
        ):
            raise ValueError("Edge is malformed")  # noqa: TRY004

        self.edges.append(Edge(edge_source, edge_destination, edge_attributes))

    def _add_attribute(self, graph_item: tuple) -> None:
        if len(graph_item) != ATTRIBUTE_ITEM_LENGTH:
            raise ValueError("Attribute is malformed")

        attribute_name, attribute_value = graph_item[1], graph_item[2]
        if not isinstance(attribute_name, str) or not isinstance(attribute_value, str):
            raise ValueError("Attribute is malformed")  # noqa: TRY004

        self.attrs[attribute_name] = attribute_value
