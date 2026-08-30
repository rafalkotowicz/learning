"""Parser dla uproszczonego formatu SGF używanego w testach Exercism."""


TREE_OPEN = "("
TREE_CLOSE = ")"
NODE_START = ";"
VALUE_OPEN = "["
VALUE_CLOSE = "]"
ESCAPE_MARKER = "\\"
NEWLINE_CHARACTER = "\n"
TAB_CHARACTER = "\t"
SPACE_CHARACTER = " "
TREE_MISSING_ERROR = "tree missing"
TREE_WITHOUT_NODES_ERROR = "tree with no nodes"
PROPERTIES_DELIMITER_ERROR = "properties without delimiter"
PROPERTY_UPPERCASE_ERROR = "property must be in uppercase"


class SgfTree:
    """Reprezentuje pojedynczy węzeł drzewa SGF wraz z dziećmi."""

    __hash__ = None

    def __init__(self, properties=None, children=None):
        """Inicjalizuje węzeł z właściwościami i listą dzieci."""
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        """Porównuje dwa drzewa po właściwościach i strukturze dzieci."""
        return (
            isinstance(other, SgfTree)
            and self.properties == other.properties
            and len(self.children) == len(other.children)
            and all(
                child_node == other_child_node
                for child_node, other_child_node in zip(self.children, other.children)
            )
        )

    def __ne__(self, other):
        """Zwraca negację porównania równości."""
        return not self == other


class SgfParser:
    """Rekurencyjny parser drzewa SGF dla formatu z zadania."""

    def __init__(self, source_text):
        """Przygotowuje parser dla wejściowego napisu SGF."""
        self.source_text = source_text
        self.source_length = len(source_text)
        self.position_index = 0

    def parse(self):
        """Parsuje całe wejście i zwraca korzeń drzewa."""
        if not self.source_text or self.source_text[self.position_index] != TREE_OPEN:
            raise ValueError(TREE_MISSING_ERROR)

        parsed_tree = self.parse_game_tree()
        if self.position_index != self.source_length:
            raise ValueError(TREE_MISSING_ERROR)
        return parsed_tree

    def parse_game_tree(self):
        """Parsuje pojedyncze drzewo wraz z wariantami i sekwencją węzłów."""
        self.consume_character(TREE_OPEN)
        if self.peek_character() == TREE_CLOSE:
            raise ValueError(TREE_WITHOUT_NODES_ERROR)

        if self.peek_character() != NODE_START:
            raise ValueError(TREE_MISSING_ERROR)

        root_node = self.parse_node()
        current_node = root_node

        while self.position_index < self.source_length and self.peek_character() != TREE_CLOSE:
            current_character = self.peek_character()
            if current_character == NODE_START:
                next_node = self.parse_node()
                current_node.children.append(next_node)
                current_node = next_node
            elif current_character == TREE_OPEN:
                variation_node = self.parse_game_tree()
                current_node.children.append(variation_node)
            else:
                raise ValueError(TREE_MISSING_ERROR)

        self.consume_character(TREE_CLOSE)
        return root_node

    def parse_node(self):
        """Parsuje pojedynczy węzeł z mapą właściwości."""
        self.consume_character(NODE_START)
        parsed_properties = {}

        while self.position_index < self.source_length:
            if self.peek_character() in f"{NODE_START}{TREE_OPEN}{TREE_CLOSE}":
                break

            property_name = self.parse_property_name()
            if not property_name.isupper():
                raise ValueError(PROPERTY_UPPERCASE_ERROR)

            if self.peek_character() != VALUE_OPEN:
                raise ValueError(PROPERTIES_DELIMITER_ERROR)

            property_values = []
            while self.peek_character() == VALUE_OPEN:
                property_values.append(self.parse_property_value())
            parsed_properties[property_name] = property_values

        return SgfTree(properties=parsed_properties)

    def parse_property_name(self):
        """Parsuje nazwę właściwości jako ciąg znaków alfabetu."""
        name_start = self.position_index
        while self.position_index < self.source_length and self.peek_character().isalpha():
            self.position_index += 1

        if self.position_index == name_start:
            raise ValueError(PROPERTIES_DELIMITER_ERROR)

        return self.source_text[name_start:self.position_index]

    def parse_property_value(self):
        """Parsuje wartość właściwości z obsługą escape i tabulacji."""
        self.consume_character(VALUE_OPEN)
        value_characters = []

        while self.position_index < self.source_length:
            current_character = self.peek_character()
            if current_character == VALUE_CLOSE:
                self.position_index += 1
                return "".join(value_characters)

            if current_character == ESCAPE_MARKER:
                self.position_index += 1
                if self.position_index >= self.source_length:
                    return "".join(value_characters)

                escaped_character = self.peek_character()
                self.position_index += 1

                if escaped_character == NEWLINE_CHARACTER:
                    continue
                if escaped_character == TAB_CHARACTER:
                    value_characters.append(SPACE_CHARACTER)
                    continue
                value_characters.append(escaped_character)
                continue

            self.position_index += 1
            if current_character == TAB_CHARACTER:
                value_characters.append(SPACE_CHARACTER)
            else:
                value_characters.append(current_character)

        return "".join(value_characters)

    def peek_character(self):
        """Podgląda aktualny znak albo pusty napis przy końcu wejścia."""
        if self.position_index >= self.source_length:
            return ""
        return self.source_text[self.position_index]

    def consume_character(self, expected_character):
        """Zużywa oczekiwany znak albo zgłasza błąd składni drzewa."""
        if self.peek_character() != expected_character:
            raise ValueError(TREE_MISSING_ERROR)
        self.position_index += 1


def parse(input_string):
    """Punkt wejścia rozwiązania: parsuje tekst SGF do SgfTree."""
    parser_instance = SgfParser(input_string)
    return parser_instance.parse()
