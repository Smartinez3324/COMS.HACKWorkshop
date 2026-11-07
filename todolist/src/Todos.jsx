import { useState, useEffect } from "react";
import { api } from "./api";

export default function Todos() {
  const [todos, setTodos] = useState([]);   
  const [title, setTitle] = useState("");   
  const [error, setError] = useState("");   
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api("/todos")
      .then(setTodos)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  const addTodo = async (e) => {
    e.preventDefault();               
    setError("");
    try {
      const created = await api("/todos", {
        method: "POST",
        body: JSON.stringify({ title }),
      });
      setTodos([...todos, created]); 
      setTitle("");
    } catch (err) {
      setError(err.message);
    }
  };

  const completeTodo = async (id) => {
    setError("");
    try {
      const updated = await api(`/todos/${id}`, { method: "PUT" });
      setTodos(todos.map((t) => (t.id === id ? updated : t)));
    } catch (err) {
      setError(err.message);
    }
  };

  const deleteTodo = async (id) => {
    setError("");
    try {
      await api(`/todos/${id}`, { method: "DELETE" });
      setTodos(todos.filter((t) => t.id !== id));
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="todos">
      <h1>To-do list</h1>

      <form onSubmit={addTodo}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="What needs doing?"
        />
        <button type="submit">Add</button>
      </form>

      {error && <p className="error">{error}</p>}

      {loading ? (
        <p>Loading...</p>
      ) : todos.length === 0 ? (
        <p className="empty">Nothing here yet. Add something above.</p>
      ) : (
        <ul>
          {todos.map((todo) => (
            <li key={todo.id} className={todo.done ? "done" : ""}>
              <span>{todo.title}</span>
              <div className="actions">
                {!todo.done && (
                  <button onClick={() => completeTodo(todo.id)}>Done</button>
                )}
                <button className="danger" onClick={() => deleteTodo(todo.id)}>
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
