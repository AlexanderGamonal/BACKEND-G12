import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div>
      <Link to="/tasks">
        <h1>Tasks App</h1>
      </Link>
      <Link to="/tasks-create">create tasks</Link>
    </div>
  );
}
