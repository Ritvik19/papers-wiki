# Papers Explained: CLRS and CLRS-Text Benchmark

Papers Explained: CLRS and CLRS-Text Benchmark

Papers Explained: CLRS and CLRS-Text Benchmark

The CLRS Algorithmic Reasoning Benchmark is a dataset covering classical algorithms from the Introduction to Algorithms textbook, designed…

Papers Explained: CLRS and CLRS-Text Benchmark

The CLRS Algorithmic Reasoning Benchmark is a dataset covering classical algorithms from the Introduction to Algorithms textbook, designed to consolidate progress in learning representations of algorithms with neural networks. It features CLRS-30, containing input-output trajectories for 30 classical algorithms including sorting, searching, dynamic programming, geometric, graph, and string algorithms.

Method

The initial survey of the textbook yielded 94 algorithms and data structures of interest. The goal is to be able to reliably generate ground-truth outputs for large inputs.

As such, NP-hard tasks (and approximation algorithms thereof) have been excluded.
Tasks requiring numerical outputs have been excluded. Evaluating their performance is ambiguous, and may be dependent on the way architectures choose to represent numbers. This excludes most number-theoretic algorithms, linear programming, and max-flow.
Standalone data structures do not directly represent a task. Rather, their target is appropriately updating the internal state of the data structure. Hence, their operations are not included, unless they appear as components of algorithms.
There are representational issues associated with dynamically allocated memory: it may be unclear what is the best way to represent the internal memory storage and its usage in algorithm trajectories. As such, for now, all algorithms that require allocating memory which cannot be directly attached to the set of objects provided at input time are excluded. This excludes algorithms like merge sort and Hierholzer’s algorithm for finding Euler tours or string matching using finite automata.

All of the above applied, we arrive at the 30 algorithms that are selected into CLRS-30, which we categorize as follows:

Sorting: Insertion sort, bubble sort, heapsort, quicksort.
Searching: Minimum, binary search, quickselect.
Divide and Conquer: Maximum subarray (Kadane’s variant).
Greedy: Activity selection, task scheduling.
Dynamic Programming: Matrix chain multiplication, longest common subsequence, optimal binary search tree.
Graphs: Depth-first and breadth-first search, topological sorting, articulation points, bridges, Kosaraju’s strongly-connected components algorithm, Kruskal’s and Prim’s algorithms for minimum spanning trees, Bellman-Ford and Dijkstra’s algorithms for single-source shortest paths (+ directed acyclic graphs version), Floyd-Warshall algorithm for all-pairs shortest paths.
Strings: Naive string matching, Knuth-Morris-Pratt (KMP) string matcher.
Geometry: Segment intersection, Convex hull algorithms: Graham scan, Jarvis’ march.

Implementation, probes and representation

The selected 30 algorithms have been implemented in an idiomatic way, which aligns as closely as possible to the original pseudocode. This allows for automatic generation of input/output pairs for all of them, enabling full control over the input data distribution. Further, the intermediate algorithm trajectory is captured in the form of “hints”, which allow insight into the inner workings of the algorithm.

Most algorithmic data can be represented as graphs, where:

Nodes are the primary objects being manipulated (e.g., elements in a sort, characters in a string, nodes in a graph).
Edges can represent explicit relationships (e.g., adjacency in a graph, predecessor links in a sequence).

For example, sorting treats each element as a node; string matching assigns a node per character.

All information for the benchmark is categorized by:

Stage: Where in the algorithm’s process the feature appears:

Input: The starting values.
Output: The final result.
Hints: Intermediate algorithm states (as described above).

Location: Where the feature lives:

Node: On an item/node.
Edge: On a pair of nodes.
Graph: Global to the whole structure.

Type: The kind of value (and relevant loss when training):

scalar: A floating-point feature.
categorical: A categorical feature (more than two possible classes).
mask: Binary (two-class) feature.
mask one: Exactly one node is active, “one-hot” encoded.
pointer: Points to one of the n nodes, useful for indicating, e.g., a predecessor.

A feature is called a “probe” if it’s a tuple of (stage, loc, type, values).

Every node gets a scalar “position” input, linearly spaced from 0 to 1 by node index. This helps neural networks disambiguate nodes (e.g., if two nodes are otherwise identical) and is especially useful for breaking ties in algorithm steps.

Dataset statistics

For each algorithm in CLRS-30, a canonical set of training, validation, and test trajectories is provided for benchmarking in- and out-of-distribution generalisation. These trajectories are obtained by running the algorithms on randomly sampled inputs that conform to their input specification.

For validation, the aim is to measure in-distribution generalisation. Inputs of 16 nodes are sampled for both, and 1,000 trajectories are generated for training and 32 for validation. For testing, out-of-distribution generalisation is measured by sampling 32 trajectories for inputs of 64 nodes. For algorithms where the output is on the graph stage rather than node or edge, 64× more trajectories are generated in order to equalise the number of targets across tasks.

CLRS is a dataset generator comprising graph execution traces of classical algorithms from the Introduction to Algorithms textbook. CLRS-Text is a textual version of these algorithmic traces. CLRS-Text is capable of procedurally generating trace data for thirty diverse, challenging algorithmic tasks across any desirable input distribution, while offering a standard pipeline in which any additional algorithmic tasks may be created in the benchmark.

Method

Since CLRS was originally designed to train non-autoregressive models, it natively leverages a graph representation of this data. In contrast, CLRS-Text converts the trace data to text. The default conversion function provided is designed with limited context windows in mind. This means that, especially for tasks including information on edges of graphs (O(n²) entries for problems of size n), it is not feasible to print all parts of the algorithm’s trace; instead, the focus is on printing exactly one variable’s trace , the variable which eventually converges to the output. In the concrete case of sorting algorithms, the trace printed is the state of the input array after each step of the algorithm.

The only algorithm in the thirty default algorithms of CLRS for which a trace is not provided is the segment intersection algorithm, as it has O(1) time complexity and therefore does not have atomic steps that converge to the final output. Note that, because the entirety of the algorithm’s state is not printed at every step, it is possible that the trace may remain unchanged in certain steps, for example, when insertion sorting an already-sorted array of n elements, each of the n steps of the trace will be identical. It is useful to encourage the model to produce such traces, as this explicitly indicates to the model the likely “thinking time” needed for solving the task through a chain of thought.

Paper

The CLRS Algorithmic Reasoning Benchmark 2205.15659

The CLRS-Text Algorithmic Reasoning Language Benchmark 2406.04229

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
