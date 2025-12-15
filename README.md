# 👾 Pygame Pathfinding Game

A simple, grid-based game built with **Pygame** to explore different pathfinding algorithms. The goal is to make the **Enemy Box (Red)** chase the **Player Box (Blue)** using different pathfinding algorithms.



## 🤖 Enemy AI Strategies Implemented

This project compares three distinct methods for the enemy to find the player:

1.  **Simple Chase:** A non-informed approach where the enemy attempts to move directly toward the player, minimizing the straight-line distance (often inefficient).
2.  **Dijkstra's Algorithm:** An informed algorithm that finds the shortest path by exploring outward from the start, guaranteeing the optimal path. 
3.  **A\* Search Algorithm:** An efficient, informed algorithm that uses a **heuristic** (estimated distance to the goal) to quickly find the optimal path without exploring the entire map. 

## 🚀 Getting Started

### Prerequisites

You need Python and Pygame installed.

```bash
pip install pygame
