import { useState, useEffect } from "react";
import "./App.css";

const API = "http://localhost:5001/api";

export default function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`${API}/todos`)
      .then((res) => res.json())
      .then((data) => setTodos(data));
  }, []);

  const handleAdd = async (e) => {
    e.preventDefault();
    setError("");

    const res = await fetch(`${API}/todos`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });
    const data = await res.json();

    if (!res.ok) {
      setError(data.error);
      return;
    }

    setTodos([...todos, data]);
    setTitle("");
  };

  const handleComplete = async (id) => {
    const res = await fetch(`${API}/todos/${id}`, { method: "PUT" });
    const updated = await res.json();
    setTodos(todos.map((t) => (t.id === id ? updated : t)));
  };

  const handleDelete = async (id) => {
    await fetch(`${API}/todos/${id}`, { method: "DELETE" });
    setTodos(todos.filter((t) => t.id !== id)); // keep everything except that one
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

      {error && <p className="error">{error}</p>}

      {todos.length === 0 && <p className="empty">Nothing here yet.</p>}

      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className={todo.done ? "done" : ""}>
            <span>{todo.title}</span>
            <div className="actions">
              {!todo.done && (
                <button onClick={() => handleComplete(todo.id)}>Done</button>
              )}
              <button className="danger" onClick={() => handleDelete(todo.id)}>
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
