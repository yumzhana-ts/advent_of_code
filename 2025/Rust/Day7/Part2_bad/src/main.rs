mod helpers;
mod node;
mod tree;
use tree::draw_tree;
use node::add_parents_to_all;
use node::compute_counts;
use std::io;


fn main() -> io::Result<()> 
{
    let grid = helpers::read_matrix("src/mini_input.txt")?;
    let (mut nodes, final_grid) = draw_tree(grid.clone());
    
	add_parents_to_all(&mut nodes, &final_grid);
	
		// 2. Рассчитываем количество временных линий (DP сверху вниз)
	compute_counts(&mut nodes);
	
		// 3. Отладочный вывод
	for node in &nodes {
		println!(
			"Node at ({}, {}) has {} parents, count = {}",
			node.x, node.y, node.parents.len(), node.count
		);
	}

		// 4. ПОЛУЧЕНИЕ ОТВЕТА:
		// Находим максимальный уровень Y (дно манифольда)
	if let Some(max_y) = nodes.iter().map(|n| n.y).max() {
		// Суммируем все временные линии, дошедшие до дна
		let total_timelines: usize = nodes.iter()
			.filter(|n| n.y == max_y)
			.map(|n| n.count)
			.sum();

		println!("\n--- ИТОГО ---");
		println!("Общее количество активных временных линий: {}", total_timelines);
	}
	
	Ok(())
	}