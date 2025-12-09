use std::collections::HashMap;

#[derive(Debug)]
pub struct Node 
{
    pub x: usize,
    pub y: usize,
    pub parents: Vec<usize>,
	pub count: usize,         // количество путей до этого узла
}

impl Node 
{
    pub fn new(x: usize, y: usize) -> Self 
	{
        Self 
		{
			x,y,parents: Vec::new(), count: 0,
		}
    }

    pub fn add_parent(&mut self, parent_idx: usize) 
	{
        self.parents.push(parent_idx);
    }
}

pub fn add_parents_to_all(nodes: &mut Vec<Node>, grid: &Vec<Vec<char>>) {
    // Карта для быстрого поиска: (x, y) -> индекс в векторе nodes
    let coord_to_idx: HashMap<(usize, usize), usize> = nodes
        .iter()
        .enumerate()
        .map(|(idx, node)| ((node.x, node.y), idx))
        .collect();

    let len = nodes.len();
    for i in 0..len {
        let (x, y) = (nodes[i].x, nodes[i].y);
        if y == 0 { continue; } // Корень S (y=0) не имеет родителей

        let parent_positions = [
            (x, y - 1),                   // Прямо над нами
            (x.saturating_sub(1), y - 1), // Слева по диагонали
            (x + 1, y - 1),               // Справа по диагонали
        ];

        for (px, py) in parent_positions {
            if let Some(&p_idx) = coord_to_idx.get(&(px, py)) {
                let parent_char = grid[py][px];
        
                let is_valid = if px == x {
                    // вертикаль
                    parent_char == '|' || parent_char == 'S'
                } else {
                    // диагональ — только если было раздвоение
                    if parent_char != '^' {
                        false
                    } else {
                        let left_child  = (px.saturating_sub(1), y);
                        let right_child = (px + 1, y);
        
                        coord_to_idx.contains_key(&left_child)
                            && coord_to_idx.contains_key(&right_child)
                    }
                };
        
                if is_valid {
                    nodes[i].add_parent(p_idx);
                }
            }
        }
    }
}

pub fn compute_counts(nodes: &mut Vec<Node>) {
    nodes.sort_by_key(|n| n.y);

    for i in 0..nodes.len() {
        if nodes[i].parents.is_empty() || nodes[i].y == 0 {
            nodes[i].count = 1;
            continue;
        }

        let mut current_sum = 0;
        let p_indices = nodes[i].parents.clone();

        for p_idx in p_indices {
            current_sum += nodes[p_idx].count;
        }

        nodes[i].count = current_sum;
    }

    // ↓↓↓ НИЖНИЙ ОБЩИЙ COUNT ↓↓↓
    let max_y = nodes.last().unwrap().y;

    let total: usize = nodes
        .iter()
        .filter(|n| n.y == max_y)
        .map(|n| n.count)
        .sum();

    println!("Bottom total count = {}", total);
}