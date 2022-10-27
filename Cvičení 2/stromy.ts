type Nullable<T> = T | null;

class Node<T> {
    left?: Nullable<Node<T>>;
    right?: Nullable<Node<T>>;
    value: T;

    constructor(value: T) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

/*
    Tenhle strom je pěkně scuffed, protože když to tam není seřazený,
    tak se hledání totálně posere.
*/
class Tree<T> {
    root: Nullable<Node<T>>;

    constructor() {
        this.root = null;
    }

    private _insert(node: Node<T>, value: T) {
        if (value > node.value) {
            if (!node.right) node.right = new Node(value);
            else this._insert(node.right, value);
        }
        else {
            if (!node.left) node.left = new Node(value);
            else this._insert(node.left, value);
        }
    }

    insert(value: T) {
        if (this.root == null) {
            this.root = new Node(value);
            return true;
        }

        this._insert(this.root, value); 
    }

    private _find(node: Node<T>, value: T, path: Node<T>[]): Nullable<{value: T, path: Node<T>[]}> {
        if (node.value == value) {
            return ({value, path});
        }

        if (node.left != null && (node.left.value >= value)) {
            return this._find(node.left, value, [...path, node.left]);
        }
        
        if (node.right != null && (node.right.value < value)) {
            return this._find(node.right, value, [...path, node.right]);
        }

        return ({ value: node.value, path });
    }

    find(value: T) {
        if (!this.root) throw new ReferenceError("Tree is empty");

        return this._find(this.root, value, []);
    }
}

// Main Code
const strom = new Tree<number>();
strom.insert(8);
strom.insert(6);
strom.insert(5);
strom.insert(4);
strom.insert(1);

console.log(strom.find(0));