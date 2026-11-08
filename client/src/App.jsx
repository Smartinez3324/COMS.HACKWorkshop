import "./App.css";

export default function App() {
  return (
    <div className="todos">
      <h1>To-do list</h1>

      <form>
        <input placeholder="What needs doing?" />
        <button type="button">Add</button>
      </form>

      <ul>
        <li>
          <span>Learn Flask</span>
        </li>
        <li className="done">
          <span>Build React app</span>
        </li>
      </ul>
    </div>
  );
}
