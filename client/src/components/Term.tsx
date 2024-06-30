type Props = {};

const Term = ({}: Props) => {
  return (
    <div className="card shadow-xl">
        <div className="card-body">
            <div className="card-title justify-between">
                <span>1A</span>
                <span>Fall 2023</span>
            </div>
            <div className="overflow-x-auto">
                <table className="table">
                    <thead>
                    <tr>
                        <th>Course</th>
                        <th>Grade</th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>MATH 136</td>
                            <td>90</td>
                        </tr>
                        <tr>
                            <td>MATH 138</td>
                            <td>81</td>
                        </tr>
                        <tr>
                            <td>CS 136</td>
                            <td>82</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div className="card-actions justify-end">
                <button className="btn btn-error">Remove</button>
                <button className="btn btn-secondary">Add Course</button>
            </div>
        </div>
    </div>
  );
};

export default Term;
