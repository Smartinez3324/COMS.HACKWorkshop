import { useState } from "react";
import "./App.css";

export default function App() {
  const [todos, setTodos] = useState([
    { id: 1, title: "Learn Flask", done: false },
    { id: 2, title: "Build React app", done: true },
  ]);
  const [title, setTitle] = useState(""); // what's typed in the box

  const handleAdd = (e) => {
    e.preventDefault(); // don't reload the page
    if (!title.trim()) return;
    setTodos([...todos, { id: Date.now(), title, done: false }]); // a NEW array
    setTitle("");
  };

  return (
    <div className="todos">
      <h1>To-do list</h1>

      <form onSubmit={handleAdd}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="What needs doing?"
        />
        <button type="submit">Add</button>
      </form>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className={todo.done ? "done" : ""}>
            <span>{todo.title}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
