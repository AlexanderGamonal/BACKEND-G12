import PropTypes from 'prop-types';

export function TaskCard({ task }) {
  return (
    <div>
        <h1>{task.title}</h1>
        <p>{task.description}</p>
        <hr />
    </div>
  )
}

TaskCard.propTypes = {
  task: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired
  }).isRequired
};