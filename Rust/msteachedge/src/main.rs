use std::cmp::Reverse;
use std::collections::{BTreeMap, BinaryHeap};

type Graph<V> = BTreeMap<V, BTreeMap<V, i32>>;

fn add_edge<V: Ord + Copy>(graph: &mut Graph<V>, v1: V, v2: V, c: i32) {
    graph.entry(v1).or_insert_with(BTreeMap::new).insert(v2, c);
    graph.entry(v2).or_insert_with(BTreeMap::new).insert(v1, c);
}

// selects a start and run the algorithm from it
pub fn prim<V: Ord + Copy + std::fmt::Debug>(graph: &Graph<V>, mst_weight: &mut i32) -> Graph<V> {
    match graph.keys().next() {
        Some(v) => prim_with_start(graph, *v, mst_weight),
        None => BTreeMap::new(),
    }
}

// only works for a connected graph
// if the given graph is not connected it will return the MST of the connected subgraph
pub fn prim_with_start<V: Ord + Copy>(
    graph: &Graph<V>,
    start: V,
    mst_weight: &mut i32,
) -> Graph<V> {
    // will contain the MST
    let mut mst: Graph<V> = Graph::new();
    // a priority queue based on a binary heap, used to get the cheapest edge
    // the elements are an edge: the cost, destination and source
    let mut prio = BinaryHeap::new();

    mst.insert(start, BTreeMap::new());

    for (v, c) in &graph[&start] {
        // the heap is a max heap, we have to use Reverse when adding to simulate a min heap
        prio.push(Reverse((*c, v, start)));
    }

    while let Some(Reverse((dist, t, prev))) = prio.pop() {
        // the destination of the edge has already been seen
        if mst.contains_key(t) {
            continue;
        }

        // the destination is a new vertex
        add_edge(&mut mst, prev, *t, dist);

        *mst_weight += dist;

        for (v, c) in &graph[t] {
            if !mst.contains_key(v) {
                prio.push(Reverse((*c, v, *t)));
            }
        }
    }

    mst
}

// selects a start and run the algorithm from it
pub fn prim_each<V: Ord + Copy + std::fmt::Debug>(
    graph: &Graph<V>,
    u: &V,
    _v: &V,
    w: &i32,
    mst_weight: &mut i32,
) -> Graph<V> {
    match graph.keys().next() {
        Some(v) => prim_each_with_start(graph, u, v, w, mst_weight),
        None => BTreeMap::new(),
    }
}

// only works for a connected graph
// if the given graph is not connected it will return the MST of the connected subgraph
pub fn prim_each_with_start<V: Ord + Copy + std::fmt::Debug>(
    graph: &Graph<V>,
    start: &V,
    v: &V,
    w: &i32,
    mst_weight: &mut i32,
) -> Graph<V> {
    // will contain the MST
    let mut mst: Graph<V> = Graph::new();
    // a priority queue based on a binary heap, used to get the cheapest edge
    // the elements are an edge: the cost, destination and source
    let mut prio_queue = BinaryHeap::new();

    mst.insert(*start, BTreeMap::new());
    add_edge(&mut mst, *start, *v, *w);

    for (v, c) in &graph[start] {
        // the heap is a max heap, we have to use Reverse when adding to simulate a min heap
        // println!("{:?} {:?}", u, c);
        prio_queue.push(Reverse((*c, v, start)));
    }

    for (u, c) in &graph[v] {
        // the heap is a max heap, we have to use Reverse when adding to simulate a min heap
        prio_queue.push(Reverse((*c, u, v)));
    }

    while let Some(Reverse((dist, t, prev))) = prio_queue.pop() {
        // the destination of the edge has already been seen
        // println!("{:?} {:?} {:?}", prev, t, dist);
        if mst.contains_key(t) {
            continue;
        }

        // the destination is a new vertex
        add_edge(&mut mst, *prev, *t, dist);

        *mst_weight += dist;

        for (v, c) in &graph[t] {
            prio_queue.push(Reverse((*c, v, &*t)));
        }
    }

    // println!("{:?}", mst_weight);
    return mst;
}

fn main() {
    use std::io::stdin;

    let mut line = String::new();
    stdin().read_line(&mut line).expect("VE input expected");
    // println!("Line: /{:?}/", line);
    let graph_info = line
        .trim_matches('\n')
        .trim_matches('\r')
        .split(' ')
        .map(|x| {
            x.parse::<i32>()
                .expect("Couldn't parse VE input to i32")
        })
        .collect::<Vec<i32>>();
    // println!("Info: {:?}", graph_info);
    assert_eq!(graph_info.len(), 2);

    let mut graph: Graph<i32> = Graph::new();
    for v in 1..=graph_info[0] {
        graph.insert(v, BTreeMap::new());
    }

    // Edge matrix to mark edges that are computed
    let mut edges = vec![];

    for _e in 0..graph_info[1] {
        line.clear();
        stdin().read_line(&mut line).expect("Edge input expected");
        // println!("Line: /{:?}/", line);
        let parsed_line = line
            .trim_matches('\n')
            .trim_matches('\r')
            .split(' ')
            .map(|x| {
                x.parse::<i32>()
                    .expect("Couldn't parse edge input to i32")
            })
            .collect::<Vec<i32>>();
        // input checking
        match &*parsed_line {
            [uertex, vertex, w] => {
                assert!(uertex <= &graph_info[0]);
                assert!(vertex <= &graph_info[0]);
                add_edge(&mut graph, *uertex, *vertex, *w);
                edges.push((*uertex, *vertex, *w));
            }
            _e => panic!("Error on input! Couldn't match against"),
        }
    }

    let mut _mst: Graph<i32> = Graph::new();

    let mut mst_weights: BTreeMap<(i32, (i32, i32)), i32> = BTreeMap::new();
    let mut mst_weight: i32 = 0;

    // Start with a generic MST to discover minimum edges
    _mst = prim(&graph, &mut mst_weight);

    for ref mut entry in &_mst {
        for (vmst, wmst) in entry.1 {
            mst_weights.insert((*entry.0, (*vmst, *wmst)), mst_weight);
        }
    }

    for (u, v, w) in edges {
        // Run Prim starting from this edge (and vertices)
        if !mst_weights.contains_key(&(u, (v, w))) {
            mst_weight = w;
            _mst = prim_each_with_start(&graph, &u, &v, &w, &mut mst_weight);
            mst_weights.entry((u, (v, w))).or_insert(mst_weight);
        } else {
            mst_weight = mst_weights[&(u, (v, w))];
        }
        for ref mut entry in &_mst {
            for (vmst, wmst) in entry.1 {
                mst_weights
                    .entry((*entry.0, (*vmst, *wmst)))
                    .or_insert(mst_weight);
            }
        }

        println!("{:?}", mst_weight);
    }
}
