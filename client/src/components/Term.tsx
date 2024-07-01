import AddCourseModal from "./AddCourseModal";
import DeleteTermModal from "./DeleteTermModal";

const courses: {code: string; grade: number}[] = [
    {
        code: "MATH 137",
        grade: 87,
    },
    {
        code: "MATH 136",
        grade: 90,
    },
    {
        code: "ECON 101",
        grade: 92,
    },
    {
        code: "CS 136",
        grade: 82,
    }
]

type Props = {
    termId: number;
};

const Term = ({ termId }: Props) => {
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
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {courses.map((course, index) => (
                            <tr key={index}>
                                <td>{course.code}</td>
                                <td>{course.grade}</td>
                                <td>
                                    <button className="btn btn-xs btn-success">Complete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="card-actions justify-end">
                <DeleteTermModal modalId={termId} />
                <AddCourseModal modalId={termId} />
            </div>
        </div>
    </div>
  );
};

export default Term;
